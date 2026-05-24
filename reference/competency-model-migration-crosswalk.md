# Competency model migration crosswalk — v0.1.0 → PDS Competence Model

This maps the old placeholder competency model (7 flat sub-areas, 0–4 self-rating)
onto the **PDS Competence Model** now kept at `reference/competency-model/`
(7 domains → 30 sub-areas → ~123 competencies, rated L1–L5).

Use this when:
- re-tagging existing reference material to the new model, and
- reading any engagement that was **run under the old model** (e.g. ENG001-SIM,
  which stays frozen at v0.1.0 — its tags only make sense via this table).

## Scale change

| Old (0–4) | New (L1–L5) |
|---|---|
| 0 = not relevant | **N/A** — not relevant to our work |
| 1 = aware only | **L1 Awareness** — recognises the concept; cannot yet do it |
| 2 = ad hoc | **L2 Familiarity** — can do it from a template, with someone to ask |
| 3 = reliable | **L3 Proficiency** — independently delivers usable work on standard pharma problems *(target working level)* |
| 4 = could teach | **L4 Mastery** / **L5 Expertise** — handles non-standard cases; sets the standard, teaches, publishes |

Note the old "4 = could teach" collapses two distinct new levels (L4 mastery vs.
L5 expertise). Do not assume an old `4` maps cleanly to L5.

## Sub-area → domain crosswalk

| Old sub-area (v0.1.0) | New home in the PDS model |
|---|---|
| Data Management & Organisation | **Data Acquisition & Management** — Data Collection, Data Curation, Data Organization, Data Quality, Data Security & Re-use, Research Data Management (+ Critical Thinking) |
| Statistical Analysis | **Mathematics & Statistics** — Mathematics, Statistical Thinking, Statistics |
| ML / Predictive Modelling | **ML & AI** — ML & AI Foundations, Model Building & Assessment, Use of AI in Education & Research |
| Bioinformatics / Cheminformatics | **No domain home.** A pharma *application* layer that spans Exploration, Mining & Analysis + ML & AI + Data Acquisition & Management depending on the task. ⚠️ Flag back to the competency-model team — the general PDS model does not carve out domain-specific application areas. |
| Data Visualisation | **Visualization & Presentation** — Creating / Interpreting / Presenting Data Visualization, Visualization Literacy, Data-Informed Decision Making |
| Reproducible Research | **Computing & Programming › Workflow & Reproducibility** |
| Scientific Programming | **Computing & Programming › Programming** (+ Computational Thinking, Computing & Computing Systems) |

## New coverage with no old equivalent

- **Ethics, Legislation & Privacy** (Data Science Ethics, Legislation, Privacy) —
  entirely new; the old model had no ethics/regulatory/privacy axis.
- **Exploration, Mining & Analysis** ((Critical) Evaluation, Analysis,
  Exploration, Integration, Mining) — only partially implied by old Statistical
  Analysis / ML.

## `[OUTSIDE MODEL]` note

ENG001-SIM flagged "Quantitative Process Modelling" (operations research /
stochastic process modelling) as `[OUTSIDE MODEL]`. The new 30 sub-areas still do
**not** cover it, so the finding stands. But the bar for `[OUTSIDE MODEL]` is now
much higher — 123 competencies — so check the full sub-area list in
`reference/competency-model/` before flagging anything new.
