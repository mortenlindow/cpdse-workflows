# Controlled vocabulary + crosswalk

This directory is the **system of record** for the IDs and names that everything
else in the repo references. It exists to enforce one principle:

> Vocab names are CSV-canonical. Rationale and prose are MD-canonical.
> Overlap (tool lists) is CSV-canonical with MD as commentary.

## Files

| File | What it owns | Authored by |
|---|---|---|
| `stages.csv` | The 14 pharma value-chain substep IDs, display names, tier, order, aliases | Human (this commit; updated when the model doc changes) |
| `domains.csv` | The 7 PDS domain IDs + display names | Human |
| `subareas.csv` | The 30 PDS sub-area IDs + their domain FK | Human |
| `crosswalk.csv` | Long-format `tool/method → (stage, domain, sub-area)` mappings | Curated; Claude proposes, humans review in PRs |

`crosswalk.csv` columns: `canonical_tool, type, aliases, stage_id, pds_domain,
pds_subarea, weight, confidence, source, flag, notes`. One row per
`(tool × stage × competency)` mapping; a tool that appears in two stages gets
two rows.

`source` carries provenance (e.g., `pharma_value_chain_model:v0.8.0`). `flag`
holds `BEYOND_REFERENCE` / `OUTSIDE_MODEL` — these are first-class outputs that
feed model improvement, not error states.

## How to update

1. **Edit the canonical model doc** (`reference/pharma-value-chain-model/Pharma_Value_Chain_Model.md`)
   for narrative changes.
2. **If a stage / domain / sub-area is renamed, added, or removed**, edit the
   matching `vocab/*.csv` in the same commit. The validator enforces that the
   model doc's `## Substep:` headings match `stages.csv`.
3. **If a new tool / method appears**, add a row to `crosswalk.csv`. Keep it
   sorted by (stage order, canonical_tool case-insensitive).
4. Run `python3 scripts/validate-vocab.py` (or just `git commit` if the
   pre-commit hook is installed). It will refuse stale references, broken FKs,
   and out-of-order rows.

## What the validator checks

See `scripts/validate-vocab.py`. In short:

- crosswalk FKs into `stages.csv`, `domains.csv`, `subareas.csv`
- sub-area's parent domain matches the row's `pds_domain` (no mis-pairings)
- model doc `## Substep:` headings resolve via display name or alias
- `stages.csv` and `crosswalk.csv` are deterministically sorted
- no duplicate `(canonical_tool, stage_id)` rows

## Roadmap (not done yet)

- **Cross-file name check** — extend the validator to scan `CLAUDE.md`,
  `README.md`, prompts, site, intake questionnaire for stage names and require
  every match to resolve via `stages.csv`. This is the natural next step; it
  would have caught every cross-file rename hunt this codebase has already had
  to do by grep.
- **Coverage table autogen** — the table at the bottom of the model doc is pure
  data and a clean autogen target (vocab → table, between HTML-comment markers).
  Keep prose human-authored; generate only that one block.
- **`type` enum** for `crosswalk.csv` (currently free-text: `tool`, `method`,
  `database`, `standard`, `metric`). Worth tightening once usage settles.

## When flat files run out

Promotion path, when concurrent edits / automated writes / queries demand it:

- structured flat files (today, git as the database)
- ↓ same schema
- SQLite / DuckDB (load on demand for analytics / heatmap aggregation)
- ↓ same schema
- Postgres behind CPDSElogic (write/serve layer)

The schema is the durable thing. Storage is swappable.
