# CPDSE Engagement ENG001-SIM — Step 4 Output: Recommendation Synthesis
# Client: Morten Simulated Lindow / CPDSE & ILF, UCPH
# Date: 2026-04-25 | Prompt version: v0.1.0
# Status: AI-synthesised — consultant review pending
---

## Recommendation Summary

The recommendations prioritise structural fixes before technical expansion —
getting existing pipelines reproducible and knowledge documented before building
new capabilities on top of fragile foundations. The single most important action
is containerising the PKPD workflow, because it directly unblocks the
OpenNABMPKPD validation goal and is achievable in weeks with Jonas's current
skills. The 3-18 month roadmap then addresses the two most consequential items:
uncertainty quantification in ML models (which fixes the generalisation
credibility problem) and the Emma succession plan (which is time-critical).
The 18-24 month horizon covers transfer learning, which requires the data
situation to improve before it can be fully exploited. Overall thrust: fix
infrastructure → strengthen ML credibility → build toward industry data access.

---

## Quick Wins (0-3 months)

### Containerise the PKPD workflow
Type: Quick Win
Addresses gap: PKPD pipeline non-reproducibility
Action: Jonas to create a Docker container for the OpenNABMPKPD ODE modelling
environment — capturing Python version, scipy/PyMC dependencies, and a fixed
random seed protocol. Write a single run_estimation.sh script that executes a
full parameter estimation run and produces a deterministic output. Test against
one published GalNAc-siRNA dataset to confirm reproducibility across Emma's
and Jonas's machines.
Who: Jonas (lead), Emma (cross-validation test)
Expected outcome: PKPD parameter estimation runs produce identical outputs
across machines. OpenNABMPKPD validation against published datasets can proceed
with auditable results.
Effort estimate: 2-3 person-weeks (Jonas)
Dependencies: None

### Establish a structured extraction template for OpenOligoLake
Type: Quick Win
Addresses gap: OpenOligoLake manual extraction inconsistency
Action: Emma to design a structured extraction form with mandatory fields,
controlled vocabularies for modification types and conjugate chemistry, and
validation rules that flag implausible values. Apply to the next 50 records as
a pilot; compare inter-annotator agreement between Emma and one master student
on 10 overlapping records.
Who: Emma (lead), Morten (review)
Expected outcome: Extraction inconsistency measurably reduced; inter-annotator
agreement >85% on numeric safety endpoints; new records enter OpenOligoLake
with traceable provenance.
Effort estimate: 2 weeks design + 1 week pilot (Emma)
Dependencies: None

### Retroactively apply model cards to existing models
Type: Quick Win
Addresses gap: Model cards not retroactively applied
Action: Jonas to create model cards for the hepatotox predictor, neurotox
predictor, and any other models in use. Each card: training data, CV results,
known failure modes, intended use, out-of-distribution warnings. Commit to
GitHub alongside model artefacts.
Who: Jonas (lead), Morten (domain accuracy review)
Expected outcome: All models in use have documented failure modes. Safe to
share with industry partners without misleading them about generalisation limits.
Effort estimate: 2-3 person-days total
Dependencies: None — should be done before any Roche data agreement is signed.

### Create a shared visualisation style sheet
Type: Quick Win
Addresses gap: No standardised visualisation templates
Action: Jonas to create a shared cpdse_style.mplstyle matplotlib style file and
a figure template notebook (PK profile, dose-response curve, model card
performance plot, feature importance). Store in group GitHub repo.
Who: Jonas
Expected outcome: All new figures from all team members use consistent style.
Publications look cohesive.
Effort estimate: 2 person-days
Dependencies: None

---

## Strategic Recommendations (3-18 months)

### Emma succession plan for OpenOligoLake
Type: Strategic
Addresses gap: Knowledge concentration risk (Emma thesis transition)
Action: By month 4, Emma to produce a curation handbook (data sources,
extraction decisions including ambiguous cases, schema rationale, QC
procedures). By month 6, identify and onboard a new master student. Emma to
co-curate with successor for at least 2 months before entering full thesis mode.
Who: Emma (handbook), Morten (identify successor), Jonas (technical onboarding)
Expected outcome: OpenOligoLake can continue without Emma. No curation knowledge
lost. Dataset growth continues toward 5,000+ record goal.
Effort estimate: 4 weeks (Emma, handbook); 2 months (co-curation overlap)
Dependencies: None
Sequencing note: Must start by month 3 — the most time-sensitive strategic
recommendation. If left until month 6+, it is too late.

### Implement uncertainty quantification on ML safety models
Type: Strategic
Addresses gap: Uncertainty quantification in ML safety models
Action: Jonas to implement conformal prediction using MAPIE library as wrapper
around existing XGBoost safety models. Produce prediction intervals alongside
point predictions. Evaluate coverage on held-out test set. Retrain hepatotox
predictor with conformal prediction and document coverage-efficiency trade-off
in model card. Apply same pattern to all future OpenOligoFeat models.
Who: Jonas (lead)
Expected outcome: ML safety models produce calibrated prediction intervals.
Out-of-distribution compounds flagged as uncertain. Models become credible for
industry partner validation.
Effort estimate: 2-3 person-weeks (Jonas)
Dependencies: None
Sequencing note: Can start in parallel with quick wins. Must precede any
external model sharing with Roche.

### Standardise Bayesian parameter estimation protocol for PKPD
Type: Strategic
Addresses gap: Inconsistent statistical rigour (PKPD thread)
Action: Jonas and Morten to agree on standard Bayesian workflow for
OpenNABMPKPD: prior specification conventions, convergence diagnostics (R-hat
thresholds, ESS minimums), posterior predictive checks, reporting standards.
Document as a methods appendix template insertable directly into manuscripts.
Who: Jonas (lead), Morten (domain review)
Expected outcome: PKPD parameter estimation statistically rigorous and
consistently reported. Manuscript methods sections writable from template.
Effort estimate: 3-4 person-weeks (Jonas + Morten)
Dependencies: None
Sequencing note: Depends on PKPD containerisation quick win being complete first.

### Begin transfer learning exploration for ML safety models
Type: Strategic
Addresses gap: Absence of transfer learning strategy for data-sparse endpoints
Action: Jonas to run a structured literature review (3-4 days), then fine-tune
ChemBERTa-77M on the OpenOligoLake hepatotox dataset. Compare against XGBoost
baseline using same nested CV framework. Report findings in group meeting before
deciding whether to invest further.
Who: Jonas (lead)
Expected outcome: Evidence-based decision on whether transfer learning improves
performance at current data size.
Effort estimate: 6-8 person-weeks (Jonas)
Dependencies: None
Sequencing note: Start after uncertainty quantification implemented — UQ needed
to properly evaluate whether fine-tuned models are better calibrated, not just
more accurate on training distribution.

---

## 18-24 Month Horizon

### Formalise industry data access pipeline (OpenOligoCommunity)
Addresses gap: External data constraint (indirect)
Action: Once Roche NDAs signed, establish standard data ingestion pipeline —
format specification, quality checks, provenance tracking in OpenOligoLake.
Who: Emma successor + Jonas | Effort: 4-6 weeks
Dependencies: NDAs signed; OpenOligoLake schema stable; Emma succession complete

### OpenOligoLake automated extraction (revisit LLM approach)
Addresses gap: Extraction inconsistency (scaling)
Action: Revisit LLM-assisted extraction using structured output APIs (GPT-4o
or Claude with JSON schema enforcement) + human verification spot-check.
Pilot on 100 records with human gold standard comparison.
Who: Emma successor | Effort: 4-6 weeks pilot
Dependencies: Structured extraction template (quick win) must be stable first.

---

## Watch List

- Transfer learning with pre-trained molecular models: Monitor FS-Mol and
  ADMET-AI benchmarks quarterly. Escalate when oligo-specific datasets appear.
  Revisit at 6-month mark.
- Graph neural networks for oligo property prediction: Revisit when
  OpenOligoLake reaches 3,000+ records.
- Active learning for DBTL loops: Revisit at OpenOligoCommunity first formal
  wet-lab partnership.
- LLM-assisted extraction scaling: Revisit at 12 months.

---

## Competency Model Note

The discovery cascade stochastic process modelling work (Research Q3 /
OpenDiscoveryCascadeModel) sits entirely outside the current CPDSE competency
model. The seven sub-areas do not collectively capture what this work requires —
operations research, stochastic optimisation, and decision theory applied to
multi-stage scientific processes. This is not a gap for the Lindow group; it is
a genuine research contribution that extends beyond the CPDSE model. A possible
future sub-area would be "Quantitative Process Modelling" or "Computational
Decision Science." Worth discussing at the next CPDSE competency model review,
with the Lindow group's work as the motivating example.
