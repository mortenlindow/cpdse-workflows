#!/usr/bin/env python3
"""Parse PDS_Competence_Model_Full_Rethought.md into model.json.

Structure of the source file:
  ## Domain
  ### Sub-area
  #### Competency
  - **Level 1: Awareness**
    **Concept**: ...
    ...
  - **Level 2: Familiarity** ...
  ...

Output:
  { "levels": ["Awareness","Familiarity","Proficiency","Mastery","Expertise"],
    "domains": [
      { "name": str,
        "subareas": [
          { "name": str,
            "competencies": [
              { "id": "1.1.1", "name": str,
                "descriptions": ["...","...","...","...","..."]   # one per level
              }
            ]
          }
        ]
      }
    ]
  }
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "PDS_Competence_Model_Full_Rethought.md"
OUT = Path(__file__).resolve().parent / "model.json"

LEVEL_RE = re.compile(r"^\s*-\s+\*\*Level\s+(\d):\s*([^*]+?)\*\*\s*$")
CONCEPT_RE = re.compile(r"^\s*\*\*Concept\*\*:\s*(.+?)\s*$")
# New short-form rubric line: "- **L3** — description text"
SHORT_RE = re.compile(r"^\s*-\s+\*\*L([1-5])\*\*\s*[—\-–]\s*(.+?)\s*$")
# Intro level definition: "- **L1 Awareness** — recognises the concept; cannot yet do it."
LEVELDEF_RE = re.compile(r"^\s*-\s+\*\*L([1-5])\s+([A-Za-z]+)\*\*\s*[—–\-]\s*(.+?)\s*$")
# Sub-area pooled blocks
STACK_RE = re.compile(r"^\*\*Typical stack:?\*\*\s*(.+?)\s*$")
EXAMPLES_HEADER_RE = re.compile(r"^\*\*Pharma examples")
EXAMPLE_RE = re.compile(r"^-\s+(.+?)\s+[—–]\s+\*(.+?)\*\s*$")
TAG_RE = re.compile(r"^(.+?)\s+@\s+L([1-5])$")
# Strip a trailing italic aside like "*(Reference level on the radar.)*"
ASIDE_RE = re.compile(r"\s*\*\([^)]*\)\*\s*$")

LEVEL_NAMES = ["Awareness", "Familiarity", "Proficiency", "Mastery", "Expertise"]

SKIP_DOMAIN_HEADINGS = {"Level Definitions"}


def parse_tags(raw_tags: str) -> list[dict]:
    """Split 'Algorithmic Thinking @ L3; Functional Thinking @ L5' into tag dicts."""
    tags: list[dict] = []
    for piece in raw_tags.split(";"):
        tm = TAG_RE.match(piece.strip())
        if tm:
            tags.append({"competency": tm.group(1).strip(), "level": int(tm.group(2))})
    return tags


def parse(md_text: str) -> dict:
    domains: list[dict] = []
    level_defs: list[dict] = []
    current_domain: dict | None = None
    current_subarea: dict | None = None
    current_comp: dict | None = None
    current_level: int | None = None
    in_examples = False
    domain_idx = subarea_idx = comp_idx = 0

    for raw in md_text.splitlines():
        line = raw.rstrip()

        if line.startswith("## ") and not line.startswith("### "):
            in_examples = False
            name = line[3:].strip()
            if name in SKIP_DOMAIN_HEADINGS:
                current_domain = current_subarea = current_comp = None
                continue
            domain_idx += 1
            subarea_idx = 0
            current_domain = {"name": name, "subareas": []}
            domains.append(current_domain)
            current_subarea = current_comp = None
        elif line.startswith("### "):
            in_examples = False
            if current_domain is None:
                continue
            subarea_idx += 1
            comp_idx = 0
            current_subarea = {"name": line[4:].strip(), "stack": "", "examples": [], "competencies": []}
            current_domain["subareas"].append(current_subarea)
            current_comp = None
        elif line.startswith("#### "):
            in_examples = False
            if current_subarea is None:
                continue
            comp_idx += 1
            cid = f"{domain_idx}.{subarea_idx}.{comp_idx}"
            current_comp = {"id": cid, "name": line[5:].strip(), "descriptions": [""] * 5}
            current_subarea["competencies"].append(current_comp)
            current_level = None
        else:
            # Intro level definitions (before the first domain).
            if not domains:
                ld = LEVELDEF_RE.match(line)
                if ld:
                    short = ASIDE_RE.sub("", ld.group(3)).strip()
                    level_defs.append({"level": int(ld.group(1)), "name": ld.group(2).strip(), "short": short})
                    continue

            # Sub-area pooled blocks (typical stack + pharma examples).
            if current_subarea is not None and current_comp is None:
                stk = STACK_RE.match(line)
                if stk:
                    current_subarea["stack"] = stk.group(1).strip()
                    in_examples = False
                    continue
                if EXAMPLES_HEADER_RE.match(line):
                    in_examples = True
                    continue
                if in_examples:
                    ex = EXAMPLE_RE.match(line)
                    if ex:
                        current_subarea["examples"].append(
                            {"text": ex.group(1).strip(), "tags": parse_tags(ex.group(2))}
                        )
                        continue
                    if line.startswith("- "):
                        current_subarea["examples"].append({"text": line[2:].strip(), "tags": []})
                        continue

            sm = SHORT_RE.match(line)
            if sm and current_comp is not None:
                idx = int(sm.group(1)) - 1
                if 0 <= idx < 5:
                    current_comp["descriptions"][idx] = sm.group(2).strip()
                current_level = None
                continue
            m = LEVEL_RE.match(line)
            if m and current_comp is not None:
                current_level = int(m.group(1))
                continue
            cm = CONCEPT_RE.match(line)
            if cm and current_comp is not None and current_level is not None:
                idx = current_level - 1
                if 0 <= idx < 5:
                    current_comp["descriptions"][idx] = cm.group(1).strip()
                current_level = None

    return {"levels": LEVEL_NAMES, "levelDefs": level_defs, "domains": domains}


def main() -> int:
    if not SRC.exists():
        print(f"missing source: {SRC}", file=sys.stderr)
        return 1
    model = parse(SRC.read_text(encoding="utf-8"))
    OUT.write_text(json.dumps(model, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    n_dom = len(model["domains"])
    n_sub = sum(len(d["subareas"]) for d in model["domains"])
    n_comp = sum(len(s["competencies"]) for d in model["domains"] for s in d["subareas"])
    print(f"wrote {OUT}: {n_dom} domains, {n_sub} sub-areas, {n_comp} competencies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
