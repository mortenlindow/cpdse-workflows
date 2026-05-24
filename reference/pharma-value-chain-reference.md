# Pharma Value Chain Reference — DS Methods & Tools
# Version: v0.1.1 (AI-drafted, pending MO review)
# Last updated: 2026-05-24
# Notes: Priority stages covered. Remaining stages to be added as encountered
#        in real engagements. [BEYOND REFERENCE] flags from engagements should
#        be incorporated here after consultant review.
---

## How to use this document

This document is the baseline for Step 2 (DS Landscape Analysis). It defines
the CPDSE-recognised established methods and tools for each pharma value chain
stage. When Step 2 encounters methods or tools not listed here, flag them as
[BEYOND REFERENCE]. When work does not map to any sub-area of the PDS Competence
Model (reference/competency-model/), flag as [OUTSIDE MODEL].

Competency tags below use the PDS Competence Model's seven domains. Note that
"Bioinformatics / Cheminformatics" is a pharma *application* layer with no
dedicated PDS domain — such methods are tagged to the closest PDS domain
(usually Exploration, Mining & Analysis or ML & AI) and marked accordingly. See
reference/competency-model-migration-crosswalk.md.

This document versions independently of the prompt documents. Update it after
each real engagement where [BEYOND REFERENCE] items are confirmed valid.

---

## Stage: Target Identification

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

## Stage: Lead Identification

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

## Stage: Lead Optimisation

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

## Stage: Biomarker Development

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

## Stage: Clinical Pharmacology

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

## Stage: Pharmacoepidemiology

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

## Stages not yet covered

The following stages are not yet covered in this document. Add entries as
they are encountered in real engagements:
- Hit Identification
- Candidate Selection
- Preclinical (DMPK, tox)
- Phase I / II / III
- Regulatory (statistical, data)
- Manufacturing (process analytical technology)
- Market Access (HEOR, outcomes research)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2026-04-25 | Initial AI draft. 6 stages covered: Target ID, Lead ID, Lead Opt, Biomarker Dev, Clinical Pharmacology, Pharmacoepidemiology. Oligo-specific notes added to Lead Opt and Clinical Pharmacology. |
| v0.1.1 | 2026-05-24 | Re-tagged all competency mappings from the v0.1.0 7-sub-area model to the PDS Competence Model (7 domains). See reference/competency-model-migration-crosswalk.md. |
