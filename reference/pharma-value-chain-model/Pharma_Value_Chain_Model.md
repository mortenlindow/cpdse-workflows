# Pharma Value Chain Model — DS Methods & Tools
# Version: v0.2.0 (AI-drafted, pending MO review)
# Last updated: 2026-05-24
# Notes: Restructured from the flat v0.1.1 stage list into a 2-tier linear model
#        (3 top-tier steps → 13 substeps). Priority substeps written up; the rest
#        are stubs to be filled as real engagements encounter them. [BEYOND
#        REFERENCE] flags from engagements should be incorporated here after
#        consultant review.
---

## What this is

The CPDSE **Pharma Value Chain Model**: the linear pipeline from target
identification to market access, used to anchor every engagement to the
customer's actual pipeline stage(s). It is one of CPDSE's three reference models
(alongside the PDS Competence Model and Training from the Back of the Room).

The model is **2-tier and linear**:

- **Tier 1 — three top-tier steps:** Pre-clinical → Clinical development → On-market
- **Tier 2 — substeps:** the named pipeline stages within each top-tier step

```
1. PRE-CLINICAL
   Target Identification → Hit Identification → Lead Identification →
   Lead Optimisation → Candidate Selection → Preclinical (DMPK/tox)
2. CLINICAL DEVELOPMENT
   Biomarker Development → Clinical Pharmacology → Phase I/II/III → Regulatory
3. ON-MARKET
   Manufacturing → Market Access (HEOR) → Pharmacoepidemiology
```

## How to use this document

This document is the baseline for Step 2 (DS Landscape Analysis) of the CPDSE
service pipeline. It defines the CPDSE-recognised established methods and tools
for each substep. When Step 2 encounters methods or tools not listed here, flag
them as **[BEYOND REFERENCE]**. When work does not map to any sub-area of the PDS
Competence Model, flag as **[OUTSIDE MODEL]**.

Competency tags below use the PDS Competence Model's seven domains (kept alongside
this model at `reference/competency-model/`). Note that "Bioinformatics /
Cheminformatics" is a pharma *application* layer with no dedicated PDS domain —
such methods are tagged to the closest PDS domain (usually Exploration, Mining &
Analysis or ML & AI) and marked accordingly. See
`reference/competency-model-migration-crosswalk.md`.

This model versions independently of the prompt documents; the `Version:` header +
changelog above is the model version. Update it after each real engagement where
[BEYOND REFERENCE] items are confirmed valid.

---

# Tier 1 · Step 1 — PRE-CLINICAL

## Substep: Target Identification

### Primary DS question
Which biological targets are most likely to be causal for the disease of
interest and tractable for drug intervention?

### Established DS methods and tools
- Genome-wide association study (GWAS) analysis: PLINK, REGENIE, SAIGE
- Mendelian randomisation for causal inference: MR-Base, TwoSampleMR
- Transcriptomic analysis for target expression: DESeq2, edgeR, limma
- Protein-protein interaction network analysis: STRING, BioGRID, Cytoscape
- Literature mining for target evidence: PubMed E-utilities, Europe PMC API
- Knowledge graph integration: OpenTargets Platform, ChEMBL API
- Druggability assessment: DruGAN, DoGSiteScorer

### Competency mapping (PDS domain)
- Mathematics & Statistics: GWAS, MR, differential expression
- Exploration, Mining & Analysis: network analysis, druggability *(bioinformatics application layer)*
- Data Acquisition & Management: knowledge graph integration, literature databases
- ML & AI: causal inference models

---

## Substep: Hit Identification

*Stub — to be written up when first encountered in a real engagement. Covers
primary/HTS screening hit calling, assay QC, and hit triage upstream of
hit-to-lead.*

---

## Substep: Lead Identification

### Primary DS question
Which compounds from a screening library or virtual space show activity
against the validated target?

### Established DS methods and tools
- HTS data analysis and statistical hit identification: R (drc, platetools)
- Dose-response curve fitting: GraphPad, drc (R), scipy
- Virtual screening: AutoDock, Glide, rDock
- Chemical space analysis and clustering: RDKit, ChemBERTa, t-SNE/UMAP
- SMILES handling and molecular representation: RDKit, OpenBabel
- ADMET prediction for early screening: SwissADME, pkCSM, DeepPurpose
- RNA secondary structure prediction (for oligonucleotides): RNAfold, IntaRNA

### Competency mapping (PDS domain)
- Mathematics & Statistics: HTS statistics, dose-response
- Exploration, Mining & Analysis: chemical space, SMILES, ADMET *(cheminformatics application layer)*
- ML & AI: virtual screening, ADMET ML models
- Computing & Programming: pipeline automation

---

## Substep: Lead Optimisation

### Primary DS question
How do structural modifications to a lead compound affect safety, activity,
selectivity, and ADMET properties?

### Established DS methods and tools
**Structure-activity relationship (SAR)**
- QSAR/QSPR modelling: scikit-learn, XGBoost, random forest on molecular descriptors
- Molecular descriptor calculation: RDKit (Morgan fingerprints, physicochemical)
- Matched molecular pair analysis (MMPA): mmpdb
- Multi-parameter optimisation (MPO) scoring: custom implementations

**Uncertainty quantification**
- Conformal prediction: MAPIE library (scikit-learn wrapper)
- Gaussian process uncertainty estimates: GPyTorch, scikit-learn GaussianProcess

**Data standardisation**
- FAIR data principles for compound data
- ChEMBL schema as reference for assay data structure
- SMILES standardisation: RDKit, ChEMBL standardiser

**Oligonucleotide-specific (ASO/siRNA)**
- Position-specific modification annotation and featurisation (custom)
- Oligo-specific safety/toxicity prediction: domain-specific ML models
- GalNAc conjugate chemistry handling: custom featurisers

### Competency mapping (PDS domain)
- ML & AI: QSAR, MPO, safety prediction
- Exploration, Mining & Analysis: molecular descriptors, MMPA, oligo featurisers *(cheminformatics application layer)*
- Mathematics & Statistics: uncertainty quantification, nested CV
- Data Acquisition & Management: FAIR data, ChEMBL schema, SMILES standardisation
- Computing & Programming › Workflow & Reproducibility: model cards, versioned model artefacts

---

## Substep: Candidate Selection

*Stub — to be written up when first encountered in a real engagement. Covers
multi-parameter candidate ranking, developability assessment, and go/no-go
decision support for declaring a development candidate.*

---

## Substep: Preclinical (DMPK, tox)

*Stub — to be written up when first encountered in a real engagement. Covers
in vitro/in vivo DMPK analysis, allometric scaling, and preclinical
toxicology/safety-margin data analysis.*

---

# Tier 1 · Step 2 — CLINICAL DEVELOPMENT

## Substep: Biomarker Development

### Primary DS question
Which biological markers predict disease progression, treatment response,
or patient stratification?

### Established DS methods and tools
- Supervised biomarker discovery: LASSO, elastic net, random forest with SHAP
- Unsupervised patient stratification: k-means, hierarchical clustering, UMAP
- Proteomic/genomic panel selection: stability selection, cross-validation
- Clinical biomarker validation: ROC/AUC analysis, NRI, IDI
- Multi-omics integration: MOFA+, mixOmics

### Competency mapping (PDS domain)
- Mathematics & Statistics: biomarker validation, ROC, NRI
- ML & AI: supervised biomarker discovery, patient stratification
- Exploration, Mining & Analysis: multi-omics integration *(bioinformatics application layer)*
- Data Acquisition & Management: clinical data standards (CDISC, HL7 FHIR)

---

## Substep: Clinical Pharmacology

### Primary DS question
How does the drug behave in the body (PK) and what is the relationship between
exposure and effect (PD)?

### Established DS methods and tools
**Population PK/PD (conventional)**
- NONMEM (industry standard for popPK)
- Monolix (alternative to NONMEM)
- nlmixr2 (R-based, open source popPK/PD)
- Pmetrics (R-based Bayesian nonparametric)

**Mechanistic/systems pharmacology**
- ODE-based systems models: scipy.integrate (Python), deSolve (R)
- Bayesian parameter estimation: PyMC, Stan, brms
- PBPK modelling: PK-Sim (open source), Simcyp (commercial)

**NABM-specific (nucleic acid-based medicines)**
Note: Standard popPK/PD tools are not well-suited to mechanistic NABM
modelling. The field lacks an established standard framework. Key approaches:
- Compartment modelling for tissue distribution (liver, kidney, plasma)
- Intracellular trafficking models (endosomal escape, RISC loading)
- In vitro to in vivo extrapolation (IVIVE) for NABMs
- Multi-scale modelling approaches (biophysical → cellular → tissue) [BEYOND REFERENCE — oligo-specific, not yet standard]

**Parameter estimation and reporting**
- Convergence diagnostics: R-hat, effective sample size (ESS)
- Posterior predictive checks
- NCA analysis: PKNCA (R), Phoenix WinNonlin (commercial)

### Competency mapping (PDS domain)
- Computing & Programming: ODE implementation, parameter estimation
- Mathematics & Statistics: Bayesian workflow, convergence diagnostics
- Data Acquisition & Management: PK dataset standards (CDISC SDTM)
- Visualization & Presentation: PK profiles, concentration-time curves

---

## Substep: Phase I / II / III

*Stub — to be written up when first encountered in a real engagement. Covers
trial design and randomisation, interim/adaptive analysis, survival and
longitudinal modelling, and statistical analysis plans (SAP).*

---

## Substep: Regulatory

*Stub — to be written up when first encountered in a real engagement. Covers
regulatory statistics, submission data standards (CDISC SDTM/ADaM), and
define.xml / reproducible submission packages.*

---

# Tier 1 · Step 3 — ON-MARKET

## Substep: Manufacturing

*Stub — to be written up when first encountered in a real engagement. Covers
process analytical technology (PAT), multivariate statistical process control,
and batch/yield modelling.*

---

## Substep: Market Access (HEOR)

*Stub — to be written up when first encountered in a real engagement. Covers
health economics and outcomes research, cost-effectiveness modelling, and
real-world value evidence.*

---

## Substep: Pharmacoepidemiology

### Primary DS question
What are the real-world effects of drugs in defined patient populations?

### Established DS methods and tools
- Propensity score methods: MatchIt, WeightIt (R)
- Interrupted time series analysis
- Distributed lag models
- Real-world evidence (RWE) database analysis: CPRD, OPTUM, MarketScan
- Causal inference frameworks: dagitty, DoWhy
- Pharmacovigilance signal detection: disproportionality analysis (ROR, PRR)

### Competency mapping (PDS domain)
- Mathematics & Statistics: causal inference, propensity scores
- Data Acquisition & Management: RWE database standards, OMOP CDM
- Computing & Programming: large dataset processing

---

## Coverage status

| Tier 1 | Substep | Status |
|--------|---------|--------|
| Pre-clinical | Target Identification | ✓ written |
| Pre-clinical | Hit Identification | ⬚ stub |
| Pre-clinical | Lead Identification | ✓ written |
| Pre-clinical | Lead Optimisation | ✓ written |
| Pre-clinical | Candidate Selection | ⬚ stub |
| Pre-clinical | Preclinical (DMPK, tox) | ⬚ stub |
| Clinical development | Biomarker Development | ✓ written |
| Clinical development | Clinical Pharmacology | ✓ written |
| Clinical development | Phase I / II / III | ⬚ stub |
| Clinical development | Regulatory | ⬚ stub |
| On-market | Manufacturing | ⬚ stub |
| On-market | Market Access (HEOR) | ⬚ stub |
| On-market | Pharmacoepidemiology | ✓ written |

6 of 13 substeps written; 7 stubs.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2026-04-25 | Initial AI draft. 6 stages covered: Target ID, Lead ID, Lead Opt, Biomarker Dev, Clinical Pharmacology, Pharmacoepidemiology. Oligo-specific notes added to Lead Opt and Clinical Pharmacology. |
| v0.1.1 | 2026-05-24 | Re-tagged all competency mappings from the v0.1.0 7-sub-area model to the PDS Competence Model (7 domains). See competency-model-migration-crosswalk.md. |
| v0.2.0 | 2026-05-24 | Restructured into a 2-tier linear model (3 top-tier steps → 13 substeps). All 7 previously-uncovered stages added as explicit substep stubs. Biomarker Development placed under Clinical development. Content of the 6 written substeps unchanged. |
