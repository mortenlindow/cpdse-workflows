#!/usr/bin/env python3
"""Validate vocab/ + crosswalk consistency against the canonical model doc.

Source of truth split:
  - vocab/stages.csv         : canonical stage IDs + display names + aliases
  - vocab/domains.csv        : canonical PDS domain IDs + display names
  - vocab/subareas.csv       : canonical PDS sub-area IDs + display names + domain FK
  - vocab/crosswalk.csv      : tool/method -> (stage, domain, sub-area) mappings
  - Pharma_Value_Chain_Model.md : prose; substep headings must FK into stages.csv

Checks:
  1. crosswalk.stage_id        FKs into stages.csv
  2. crosswalk.pds_domain      FKs into domains.csv
  3. crosswalk.pds_subarea (if set) FKs into subareas.csv AND parent domain matches
  4. Model doc substep headings match a stages.csv display_name or alias
  5. stages.csv rows sorted by 'order' ascending
  6. crosswalk.csv rows sorted by (stage order, canonical_tool case-insensitive)
  7. crosswalk.canonical_tool + stage_id pairs are unique (no accidental dupes)

Exit code 0 if clean, 1 if any error. Stdlib only — runs anywhere with python3.
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOCAB = ROOT / "reference" / "vocab"
MODEL_MD = ROOT / "reference" / "pharma-value-chain-model" / "Pharma_Value_Chain_Model.md"

errors = []
def err(msg): errors.append(msg)

def load(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))

stages = load(VOCAB / "stages.csv")
domains = load(VOCAB / "domains.csv")
subareas = load(VOCAB / "subareas.csv")
crosswalk = load(VOCAB / "crosswalk.csv")

stage_ids = {r["id"] for r in stages}
stage_order = {r["id"]: int(r["order"]) for r in stages}
stage_lookup = {}  # display_name + aliases (lower) -> id
for r in stages:
    stage_lookup[r["display_name"].strip().lower()] = r["id"]
    for a in (r.get("aliases", "") or "").split("|"):
        a = a.strip()
        if a:
            stage_lookup[a.lower()] = r["id"]

domain_ids = {r["id"] for r in domains}
subarea_by_id = {r["id"]: r for r in subareas}

# 1-3. Crosswalk FKs
for i, row in enumerate(crosswalk, start=2):
    if row["stage_id"] not in stage_ids:
        err(f"crosswalk.csv:{i}: unknown stage_id '{row['stage_id']}'")
    if row["pds_domain"] not in domain_ids:
        err(f"crosswalk.csv:{i}: unknown pds_domain '{row['pds_domain']}'")
    sub = (row.get("pds_subarea") or "").strip()
    if sub:
        if sub not in subarea_by_id:
            err(f"crosswalk.csv:{i}: unknown pds_subarea '{sub}'")
        elif subarea_by_id[sub]["domain_id"] != row["pds_domain"]:
            err(f"crosswalk.csv:{i}: sub-area '{sub}' belongs to domain "
                f"'{subarea_by_id[sub]['domain_id']}', not '{row['pds_domain']}'")

# 4. Model doc substep headings
heading_re = re.compile(r"^## Substep:\s*(.+?)\s*$", re.MULTILINE)
md_text = MODEL_MD.read_text()
for heading in heading_re.findall(md_text):
    if heading.strip().lower() not in stage_lookup:
        err(f"{MODEL_MD.name}: substep heading '{heading}' has no matching "
            f"stages.csv row (check display_name or aliases)")

# 5. stages.csv sort
orders = [int(r["order"]) for r in stages]
if orders != sorted(orders) or len(set(orders)) != len(orders):
    err("stages.csv: rows must be sorted by 'order' ascending with no duplicates")

# 6. crosswalk.csv sort
expected = sorted(
    enumerate(crosswalk),
    key=lambda kv: (stage_order.get(kv[1]["stage_id"], 999), kv[1]["canonical_tool"].lower())
)
if [i for i, _ in expected] != list(range(len(crosswalk))):
    err("crosswalk.csv: rows must be sorted by (stage order, canonical_tool case-insensitive)")

# 7. Uniqueness of (canonical_tool, stage_id)
seen = set()
for i, row in enumerate(crosswalk, start=2):
    key = (row["canonical_tool"].lower(), row["stage_id"])
    if key in seen:
        err(f"crosswalk.csv:{i}: duplicate (canonical_tool, stage_id) "
            f"= ({row['canonical_tool']}, {row['stage_id']})")
    seen.add(key)

if errors:
    print("VOCAB VALIDATION FAILED:", file=sys.stderr)
    for e in errors:
        print(f"  - {e}", file=sys.stderr)
    sys.exit(1)

print(f"vocab OK: {len(stages)} stages, {len(domains)} domains, "
      f"{len(subareas)} sub-areas, {len(crosswalk)} crosswalk rows.")
