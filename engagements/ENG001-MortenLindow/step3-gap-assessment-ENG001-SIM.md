# CPDSE Engagement ENG001-SIM — Step 3 Output: Gap Assessment
# Client: Morten Simulated Lindow / CPDSE & ILF, UCPH
# Date: 2026-04-25 | Prompt version: v0.1.0
# Status: AI-synthesised — consultant review pending
---

## Gap Assessment Summary

The Lindow group has a technically strong but structurally fragile DS profile.
The dominant gap theme is reproducibility infrastructure — the group has the
right analytical methods in place but cannot consistently reproduce results
across machines or team members, which directly undermines their ability to
publish credible models and attract industry data partners. This structural gap
cuts across all three active research threads simultaneously. The most
constraining single gap relative to stated goals is dataset sparsity for oligo
safety modelling, but this is an external constraint that cannot be closed
through DS capability alone — it requires partnership strategy. The second most
constraining is PKPD workflow fragility, which is both internally solvable and
actively blocking the OpenNABMPKPD validation goal. Gap profile: ~60% structural,
~40% technical — structural fixes will have disproportionate leverage.

---

## Structural Gaps

### PKPD pipeline non-reproducibility
Type: Structural
Competency sub-area: Reproducible Research (+ Scientific Programming)
Impact: High — OpenNABMPKPD validation against 3+ independent datasets requires
reproducible parameter estimation runs; currently they are not, meaning results
cannot be reliably reported or audited.
Effort to close: Low — Docker container + fixed random seed protocol is a 2-3
week task for Jonas.
Urgency: Active — currently costs time on every PKPD run.
Evidence: Q6: "PKPD runs not yet reproducible across machines due to random seed
issues and environment dependencies"; Q8: Reproducible Research [2]; Q11:
"Docker planned next semester"

### OpenOligoLake manual extraction inconsistency
Type: Structural
Competency sub-area: Data Management (+ Reproducible Research)
Impact: High — extraction inconsistencies produce unknown systematic biases in
ML training data.
Effort to close: Medium — structured extraction template design and validation
is 3-4 weeks plus ongoing process discipline.
Urgency: Active — inconsistencies accumulate with every new paper curated.
Evidence: Q6: "Excel-based extraction... still some manual steps introducing
inconsistencies"; Q11: "piloting structured extraction form"

### Knowledge concentration risk (Emma thesis transition)
Type: Structural
Competency sub-area: Data Management (+ Reproducible Research)
Impact: High — Emma is sole lead on OpenOligoLake curation and ML featurisation;
exit in ~12 months without successor risks continuity and tacit knowledge loss.
Effort to close: Medium — 4-8 week process if started now.
Urgency: Near-term — must start within 3-6 months.
Evidence: Q12: "Emma entering thesis writing phase in ~12 months — OpenOligoLake
continuity at risk without succession planning"

### Inconsistent statistical rigour across workflows
Type: Structural
Competency sub-area: Statistical Analysis
Impact: Medium — nested CV implemented for ML but formal statistical testing
inconsistent; Bayesian methods partial; affects publication credibility.
Effort to close: Medium — ~2 weeks for Jonas to establish group standards.
Urgency: Near-term — not blocking current work but bottleneck at manuscript stage.
Evidence: Q8: Statistical Analysis [2], "Basic stats and nested CV done; Bayesian
partial; formal testing inconsistent"

---

## Technical Gaps

### Uncertainty quantification in ML safety models
Type: Technical
Competency sub-area: ML/Predictive Modelling (+ Statistical Analysis)
Impact: High — without prediction intervals, models produce confidently wrong
predictions on out-of-distribution compounds; direct technical cause of the
generalisation problem flagged in Q1.
Effort to close: Medium — conformal prediction via MAPIE library; Jonas can
implement in 2-3 weeks.
Urgency: Active — existing hepatotox predictor has the problem now.
Evidence: Q1: "initial hepatotox predictor does not generalise well to newer
chemistries"; Step 2 landscape: "conformal prediction increasingly used"

### Absence of transfer learning strategy for data-sparse endpoints
Type: Technical
Competency sub-area: ML/Predictive Modelling
Impact: High — public oligo safety data acknowledged as fundamental bottleneck;
transfer learning from broader chemical datasets is the established field
approach not currently in use.
Effort to close: High — 6-10 week ramp-up for Jonas on pre-trained molecular
models (ChemBERTa or similar) plus implementation.
Urgency: Near-term — most tractable path to better generalisation.
Evidence: Q10: "dataset size is the fundamental bottleneck"; Step 2: "transfer
learning... active strategy for addressing data sparsity"

### No standardised visualisation templates
Type: Technical | Competency: Data Visualisation
Impact: Low | Effort: Low | Urgency: Near-term
Evidence: Q8: [2], "functional plots; no standard templates; inconsistent styles"

### Model cards not retroactively applied
Type: Technical | Competency: Reproducible Research
Impact: Medium | Effort: Low | Urgency: Near-term
Evidence: Q8: "model cards are a recent addition not retroactively applied"

---

## Horizon Items

- Transfer learning with pre-trained molecular models (ChemBERTa, MolBERT):
  Monitor FS-Mol and ADMET-AI benchmarks quarterly. Revisit at 6 months.
- Graph neural networks for oligo property prediction: Not meaningful at
  current dataset sizes. Revisit when OpenOligoLake reaches 3,000+ records.
- Active learning for DBTL loops: Revisit at first formal industry wet-lab
  partnership.
- LLM-assisted extraction scaling: Monitor structured output API quality on
  numerical scientific data. Revisit at 12 months.

---

## Outside Model Items

- Discovery cascade stochastic process modelling (Research Q3 /
  OpenDiscoveryCascadeModel): Does not map to any of the seven CPDSE sub-areas.
  Closest is Statistical Analysis but substantially understates scope. Work draws
  on operations research, stochastic process modelling, decision theory applied
  to multi-stage scientific processes. Genuine novel research direction, not a
  gap. Potential future CPDSE sub-area: "Quantitative Process Modelling" or
  "Computational Decision Science."

---

## Gap Assessment Caveats

- [DATA GAP] ML landscape comparison based on published academic benchmarks only
  — true industry gap may be larger than assessed.
- [DATA GAP] Q8 ratings are self-reported — statistical analysis gap in
  particular may be overstated or understated. Consultant should probe in W1.
- PKPD gap assessment assumes Jonas has Docker competence — inferred from
  background, not confirmed.
- Knowledge concentration risk assumes Emma is sole custodian of curation
  decisions — if Jonas has been reviewing choices, risk is lower than assessed.
