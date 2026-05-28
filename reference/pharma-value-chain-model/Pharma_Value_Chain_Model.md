# Pharma Value Chain Model — DS Methods & Tools
# Version: v0.8.0 (AI-drafted, pending MO review)
# Last updated: 2026-05-25
# Notes: Renamed "Pharmacoepidemiology" → "Pharmacovigilance & Pharmacoepidemiology"
#        and expanded the pharmacovigilance DS methods (spontaneous-reporting
#        disproportionality, BCPNN/MGPS, NLP on case narratives, ICSR de-dup), which
#        were previously compressed to one line. PV detects signals, PE evaluates
#        them; trial safety stays in Phase I/II/III and RMP/REMS in Regulatory. Still
#        14 substeps, all in the 3-part form (Primary DS question → Key questions →
#        Established DS methods and tools). [Earlier: v0.7.0 added Formulation & Drug
#        Product Development (CMC); v0.6.0 merged Candidate Selection into Lead
#        Optimisation and renamed Preclinical → Nonclinical Safety & DMPK.] [BEYOND
#        REFERENCE] flags from engagements should be incorporated here after review.
---

## What this is

The CPDSE **Pharma Value Chain Model**: the linear pipeline from disease
understanding to market access, used to anchor every engagement to the
customer's actual pipeline stage(s). It is one of CPDSE's reference models.

The model is **2-tier and linear**:

- **Tier 1 — three top-tier steps:** Pre-clinical → Clinical development → On-market
- **Tier 2 — substeps:** the named pipeline stages within each top-tier step

```
1. PRE-CLINICAL
   Disease Understanding → Target Identification → Modality Selection →
   Lead Identification → Lead Optimisation & Candidate Selection →
   Nonclinical Safety & DMPK → Formulation & Drug Product Development (CMC)
2. CLINICAL DEVELOPMENT
   Biomarker Development → Clinical Pharmacology → Phase I/II/III → Regulatory
3. ON-MARKET
   Manufacturing → Market Access (HEOR) → Pharmacovigilance & Pharmacoepidemiology
```

## How to use this document

This document is the baseline for Step 2 (DS Landscape Analysis) of the CPDSE
service pipeline. It defines the CPDSE-recognised established methods and tools
for each substep. When Step 2 encounters methods or tools not listed here, flag
them as **[BEYOND REFERENCE]**.

Every substep follows the same 3-part form:
1. **Primary DS question** — the single high-level question, the one-line compression.
2. **Key questions** — the fuller set of more specific scientific and strategic
   questions a group is actually trying to answer at that stage. These are the
   discussion anchors for Meeting 1 and Workshop 1 — they sit above the DS methods
   and frame *why* a given method matters.
3. **Established DS methods and tools** — the CPDSE-recognised methods and tooling
   used to answer those questions.

This model versions independently of the prompt documents; the `Version:` header +
changelog above is the model version. Update it after each real engagement where
[BEYOND REFERENCE] items are confirmed valid.

---

# Tier 1 · Step 1 — PRE-CLINICAL

## Substep: Disease Understanding

### Primary DS question
What is the disease, who does it affect, and where is the unmet medical need
that a new therapy could address?

### Key questions
- Where is the unmet medical need?
- What is the pathophysiology?
- Who are the patients?
- What tissue and cell types are involved?
- What molecular pathways are involved?

### Established DS methods and tools
- Disease epidemiology and burden-of-illness analysis: real-world data, registries
- Patient stratification / subtype discovery: clustering on omics, EHR phenotyping
- Pathophysiology and pathway mapping: pathway enrichment (Reactome, KEGG, WikiPathways)
- Cell-type and tissue involvement: single-cell RNA-seq, expression atlases
  (Human Protein Atlas, GTEx, Tabula Sapiens)
- Literature and evidence mining for unmet need: PubMed E-utilities, Europe PMC API
- Knowledge-graph evidence integration: Open Targets Platform

---

## Substep: Target Identification

### Primary DS question
Which biological targets are most likely to be causal for the disease of
interest and tractable for drug intervention?

### Key questions
- Are there genetic fingerprints (causal genetic signals) pointing to a target?
- What targets are already validated or being worked on?
- What disease models exist?

### Established DS methods and tools
- Genome-wide association study (GWAS) analysis: PLINK, REGENIE, SAIGE
- Mendelian randomisation for causal inference: MR-Base, TwoSampleMR
- Transcriptomic analysis for target expression: DESeq2, edgeR, limma
- Protein-protein interaction network analysis: STRING, BioGRID, Cytoscape
- Literature mining for target evidence: PubMed E-utilities, Europe PMC API
- Knowledge graph integration: OpenTargets Platform, ChEMBL API
- Druggability assessment: DruGAN, DoGSiteScorer

---

## Substep: Modality Selection

### Primary DS question
Given the target and what it takes to engage it, which therapeutic modality is
the right one to pursue?

### Key questions
- What makes a "good" target?
- Where is the target (tissue, cell, sub-cellular compartment)?
- What type of molecule is the target?
- What needs to happen to the target (inhibit, degrade, modulate, knock down)?
- What can reach it?
- Biomarker vs target — what are we actually acting on?
- What modalities are available, and how mature are they?
- What route of administration (RoA) would be best?
- What duration of action (DoA) would be best?
- What cost of goods (CoG) is acceptable?
- How fast do we need to be?
- What is the competitive situation?

### Established DS methods and tools
- Target localisation and accessibility analysis: expression atlases, subcellular
  localisation prediction
- Modality feasibility and developability scoring across candidate modalities
  (small molecule, antibody, oligonucleotide, etc.)
- Target product profile (TPP) modelling: RoA, DoA, CoG constraints as decision criteria
- Competitive and patent landscape analysis: clinical trial and patent databases
- Druggability/ligandability assessment carried over from Target Identification

*This stage is decision-oriented as much as analytical; several questions are
strategic rather than method-driven.*

---

## Substep: Lead Identification

### Primary DS question
Which compounds from a screening library or virtual space show genuine activity
against the validated target?

### Key questions
- How do you confirm your lead hits are genuine and not artefacts?
- How do you handle screening at scale?
- How do you confirm selectivity across your hit series?

### Established DS methods and tools
- HTS data analysis and statistical hit identification: R (drc, platetools)
- Dose-response curve fitting: GraphPad, drc (R), scipy
- Virtual screening: AutoDock, Glide, rDock
- Chemical space analysis and clustering: RDKit, ChemBERTa, t-SNE/UMAP
- SMILES handling and molecular representation: RDKit, OpenBabel
- ADMET prediction for early screening: SwissADME, pkCSM, DeepPurpose
- RNA secondary structure prediction (for oligonucleotides): RNAfold, IntaRNA

---

## Substep: Lead Optimisation & Candidate Selection

*Candidate selection (development-candidate nomination) is the go/no-go gate that
ends lead optimisation, so it lives here rather than as a separate substep: the
ranking and decision methods operate on the same optimised series.*

### Primary DS question
How do structural modifications improve a lead's safety, activity, selectivity,
and ADMET — and which optimised compound has the best overall balance to be
nominated as the development candidate?

### Key questions
- How potent does a starting compound need to be to be worth pursuing?
- How do you rank molecules across competing properties (potency vs. safety vs.
  PK vs. manufacturability)?
- Does anything actually work in a test (in vitro/in vivo confirmation)?
- What is important in the in silico phase of the design process?
- How confident are we in each predicted property — what is the risk of
  late-stage failure?
- Which single compound (or small set) do we nominate, and is there a credible
  backup?

### Established DS methods and tools
**Structure-activity relationship (SAR)**
- QSAR/QSPR modelling: scikit-learn, XGBoost, random forest on molecular descriptors
- Molecular descriptor calculation: RDKit (Morgan fingerprints, physicochemical)
- Matched molecular pair analysis (MMPA): mmpdb
- Multi-parameter optimisation (MPO) / desirability scoring across the property set

**Uncertainty quantification**
- Conformal prediction: MAPIE library (scikit-learn wrapper)
- Gaussian process uncertainty estimates: GPyTorch, scikit-learn GaussianProcess

**Data standardisation**
- FAIR data principles for compound data
- ChEMBL schema as reference for assay data structure
- SMILES standardisation: RDKit, ChEMBL standardiser

**Candidate nomination (the go/no-go gate)**
- Probabilistic / Bayesian candidate ranking with uncertainty propagation
- Decision analysis against the target product profile (TPP) defined at Modality Selection
- Portfolio / risk modelling: probability of technical success (PTS) estimation
- Trade-off visualisation: radar/spider plots, Pareto-front analysis
- Developability inputs (solubility, permeability, stability) drawn from
  Nonclinical Safety & DMPK rather than re-modelled here

**Oligonucleotide-specific (ASO/siRNA)**
- Position-specific modification annotation and featurisation (custom)
- Oligo-specific safety/toxicity prediction: domain-specific ML models
- GalNAc conjugate chemistry handling: custom featurisers
- Developability liabilities at nomination: immunostimulation, off-target
  hybridisation, sequence motifs

---

## Substep: Nonclinical Safety & DMPK

### Primary DS question
Does the candidate have an acceptable pharmacokinetic and safety profile in
preclinical models to justify first-in-human dosing?

### Key questions
- What is the ADME profile (absorption, distribution, metabolism, excretion)?
- What is the safety margin between efficacious and toxic exposure?
- How do animal results translate to a predicted human dose and exposure?
- What are the dose-limiting toxicities, and which organs are at risk?
- Is exposure at the intended site of action sufficient and sustained?

### Established DS methods and tools
- Non-compartmental analysis (NCA) of in vivo PK: PKNCA (R), Phoenix WinNonlin
- Allometric scaling / interspecies extrapolation for human dose prediction
- PBPK modelling for first-in-human dose projection: PK-Sim, Simcyp
- In vitro–in vivo extrapolation (IVIVE) of clearance and metabolism
- Exposure–response and safety-margin analysis (NOAEL, MABEL)
- Dose–response / benchmark-dose modelling: drc (R), BMD software
- Toxicogenomics and histopathology data analysis
- Oligonucleotide-specific: tissue accumulation kinetics, hybridisation-dependent
  off-target toxicity screening

---

## Substep: Formulation & Drug Product Development (CMC)

*Placed at the end of Pre-clinical because a drug product must exist before
first-in-human dosing, but formulation/CMC is really a parallel workstream: it
begins at candidate nomination (preformulation), iterates through the clinic, and
continues into commercial **Manufacturing**. This substep owns the
formulation-specific DS methods; molecule-level developability sits upstream in
Lead Optimisation & Candidate Selection, and process control sits downstream in
Manufacturing.*

### Primary DS question
How do we turn the development candidate into a stable, manufacturable drug
product that delivers the right exposure by the intended route?

### Key questions
- Which formulation and excipients give adequate solubility, bioavailability, and
  physical/chemical stability?
- How does the formulation affect in vivo exposure (and how do we predict it
  before dosing humans)?
- What is the shelf life, and which conditions limit it?
- For the chosen route, what delivery system reaches the target tissue?
- How few experiments can establish a robust formulation design space?

### Established DS methods and tools
- Design of Experiments (DoE) for formulation: mixture designs, response-surface
  methodology (Design-Expert, JMP)
- Dissolution modelling and in vitro–in vivo correlation (IVIVC)
- Physiologically-based biopharmaceutics modelling (PBBM) for bioavailability,
  food effect, and dose selection: GastroPlus, Simcyp
- Stability / shelf-life prediction: Arrhenius kinetics, ASAPprime
- Excipient-compatibility screening and prediction (ML on compatibility data)
- Delivery-system optimisation: nanoparticle / LNP lipid-ratio, encapsulation
  efficiency, and particle-size modelling (DoE + ML)
- Developability inputs (solubility, permeability, solid-state stability) are
  drawn from Lead Optimisation & Candidate Selection; QbD design-space and
  process-control methods are shared with Manufacturing
- Oligonucleotide-specific: LNP and GalNAc delivery-system formulation; liver-
  tropism and tissue-targeting design [BEYOND REFERENCE — oligo delivery, not yet standard]

---

# Tier 1 · Step 2 — CLINICAL DEVELOPMENT

## Substep: Biomarker Development

### Primary DS question
Which biological markers are validated and qualified to predict treatment
response or stratify patients in the clinic?

### Key questions
- Which candidate markers track treatment response or progression in patients?
- Is the biomarker analytically valid and reproducible across cohorts and platforms?
- How small a panel can we use while retaining predictive performance?
- Does the biomarker actually predict the clinical endpoint, not merely correlate?
- Is the biomarker qualified for its context of use (surrogate endpoint,
  companion diagnostic, enrichment)?

### Established DS methods and tools
- Supervised biomarker discovery: LASSO, elastic net, random forest with SHAP
- Proteomic/genomic panel selection: stability selection, cross-validation
- Clinical biomarker validation & qualification: ROC/AUC, NRI, IDI, decision-curve analysis
- Surrogate-endpoint and companion-diagnostic evaluation
- Exploratory patient stratification and multi-omics integration (clustering, UMAP,
  MOFA+, mixOmics) live upstream in **Disease Understanding**; this substep
  consumes those subtypes rather than re-deriving them

---

## Substep: Clinical Pharmacology

### Primary DS question
How does the drug behave in the body (PK) and what is the relationship between
exposure and effect (PD)?

### Key questions
- What dose and schedule produce the target exposure?
- How does exposure relate to both efficacy and toxicity (the therapeutic window)?
- How does PK vary across patients (covariates: weight, renal/hepatic function)?
- Does the drug reach its site of action at adequate concentrations?
- How do we extrapolate from preclinical and early clinical data to the dose?

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

---

## Substep: Phase I / II / III

### Primary DS question
Is the drug safe, and does it produce a clinically meaningful benefit in patients
at a well-defined dose?

### Key questions
- What is the safe, tolerable dose range and the recommended Phase 2 dose?
- Does the drug show efficacy on clinical endpoints versus control?
- Which patients respond best (subgroups, biomarkers)?
- Is the trial adequately powered, and when should we look at the data?
- Can the trial adapt (dose, sample size, stopping) on accumulating evidence?

### Established DS methods and tools
- Trial design and sample-size / power calculations
- Randomisation and stratification schemes
- Dose-finding designs: 3+3, CRM, BOIN (model-based dose escalation)
- Adaptive / group-sequential designs and interim analyses (alpha spending)
- Survival analysis (Kaplan–Meier, Cox PH) and longitudinal mixed models (MMRM)
- Bayesian adaptive designs and predictive probability of success
- Estimands framework (ICH E9 R1), multiplicity control, and missing-data
  sensitivity analyses, all captured in the Statistical Analysis Plan (SAP)
- Tools: SAS, R (survival, nlme, rpact), East

---

## Substep: Regulatory

### Primary DS question
Can we assemble defensible, standards-compliant evidence that a regulator will
accept to approve the drug?

### Key questions
- Do analyses meet regulatory statistical and data-standard requirements?
- Are datasets traceable, reproducible, and submission-ready?
- What is the benefit–risk balance across the totality of evidence?
- How do we handle multiplicity, missing data, and sensitivity analyses defensibly?
- Is the documentation complete and auditable?

### Established DS methods and tools
- CDISC data standards: SDTM (tabulation), ADaM (analysis-ready), define.xml
- Reproducible, validated analysis pipelines (double programming, validation)
- Structured benefit–risk assessment frameworks
  (trial-level multiplicity, missing-data, and estimand choices are set upstream
  in Phase I/II/III; Regulatory packages and re-presents them to standard)
- Integrated summaries of safety and efficacy (ISS / ISE); meta-analysis across studies
- Tools: SAS (regulatory default), validated R ({pharmaverse} packages),
  Pinnacle 21 for CDISC compliance

---

# Tier 1 · Step 3 — ON-MARKET

## Substep: Manufacturing

### Primary DS question
Is the manufacturing process consistent, in control, and capable of producing
product within specification at scale?

### Key questions
- Is the process in a state of statistical control?
- Which process parameters drive the critical quality attributes (CQAs)?
- Can we predict and prevent out-of-specification batches?
- How do we ensure batch-to-batch consistency and yield?
- Can quality be assessed in real time rather than only by end-product testing?

### Established DS methods and tools
- Statistical process control (SPC): control charts, Cpk/Ppk capability indices
- Multivariate SPC and batch monitoring: PCA, PLS (SIMCA)
- Process analytical technology (PAT): NIR/Raman spectroscopy chemometrics
- Design of experiments (DoE) for process characterisation; Quality by Design (QbD)
- Design-space / proven-acceptable-range modelling
- Predictive batch/yield modelling and soft sensors
- Tools: JMP, SIMCA, Minitab, Python/R for chemometrics

---

## Substep: Market Access (HEOR)

### Primary DS question
Does the drug deliver enough value, at an acceptable cost, to justify
reimbursement and adoption?

### Key questions
- Is the drug cost-effective versus the current standard of care?
- What is the budget impact for a payer?
- How do trial outcomes translate to long-term and quality-of-life outcomes?
- What real-world evidence supports the value proposition?
- How does value vary across patient subgroups and jurisdictions?

### Established DS methods and tools
- Cost-effectiveness analysis: Markov models, discrete-event simulation, decision trees
- ICER / QALY modelling and budget-impact models
- Indirect treatment comparison / network meta-analysis (absent head-to-head data)
- Survival extrapolation for long-term outcomes (parametric / flexible models)
- Probabilistic sensitivity analysis (Monte Carlo)
- Real-world evidence for effectiveness and value
- Tools: R (heemod, hesim), TreeAge, Excel-based models

---

## Substep: Pharmacovigilance & Pharmacoepidemiology

*Two coupled post-market disciplines with distinct DS toolkits: pharmacovigilance
**detects** safety signals (largely from spontaneous-reporting data),
pharmacoepidemiology **evaluates** and quantifies real-world effects (largely from
observational cohort / claims data). A detected signal typically triggers a formal
pharmacoepidemiology study. Trial safety monitoring sits upstream in Phase I/II/III;
risk management plans / REMS sit in Regulatory.*

### Primary DS question
What are the real-world safety signals and effects of the drug once it is in
routine use in defined patient populations?

### Key questions
- Are there emerging safety signals that warrant investigation?
- Are there rare or long-term adverse effects not seen in trials?
- What are the real-world effectiveness and safety in routine use?
- How do we control confounding in observational data?
- How does the drug perform in subpopulations excluded from trials?

### Established DS methods and tools
**Pharmacovigilance (signal detection)**
- Disproportionality analysis on spontaneous-report databases (FAERS, VigiBase,
  EudraVigilance): PRR, ROR
- Bayesian signal detection: BCPNN, MGPS / EBGM
- NLP on adverse-event narratives, literature, and social media for signal mining
- Individual case safety report (ICSR) de-duplication and triage

**Pharmacoepidemiology (signal evaluation & real-world effects)**
- Propensity score methods: MatchIt, WeightIt (R)
- Causal inference frameworks: dagitty, DoWhy
- Interrupted time series analysis; distributed lag models
- Real-world evidence (RWE) database analysis: CPRD, OPTUM, MarketScan

---

## Coverage status

| Tier 1 | Substep | Status |
|--------|---------|--------|
| Pre-clinical | Disease Understanding | ✓ written |
| Pre-clinical | Target Identification | ✓ written |
| Pre-clinical | Modality Selection | ✓ written |
| Pre-clinical | Lead Identification | ✓ written |
| Pre-clinical | Lead Optimisation & Candidate Selection | ✓ written |
| Pre-clinical | Nonclinical Safety & DMPK | ✓ written |
| Pre-clinical | Formulation & Drug Product Development (CMC) | ✓ written |
| Clinical development | Biomarker Development | ✓ written |
| Clinical development | Clinical Pharmacology | ✓ written |
| Clinical development | Phase I / II / III | ✓ written |
| Clinical development | Regulatory | ✓ written |
| On-market | Manufacturing | ✓ written |
| On-market | Market Access (HEOR) | ✓ written |
| On-market | Pharmacovigilance & Pharmacoepidemiology | ✓ written |

14 of 14 substeps written; 0 stubs. All substeps follow the 3-part form
(Primary DS question → Key questions → Established DS methods and tools).

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v0.1.0 | 2026-04-25 | Initial AI draft. 6 stages covered: Target ID, Lead ID, Lead Opt, Biomarker Dev, Clinical Pharmacology, Pharmacoepidemiology. Oligo-specific notes added to Lead Opt and Clinical Pharmacology. |
| v0.1.1 | 2026-05-24 | Re-tagged all competency mappings from the v0.1.0 7-sub-area model to the PDS Competence Model (7 domains). See competency-model-migration-crosswalk.md. |
| v0.2.0 | 2026-05-24 | Restructured into a 2-tier linear model (3 top-tier steps → 13 substeps). All 7 previously-uncovered stages added as explicit substep stubs. Biomarker Development placed under Clinical development. Content of the 6 written substeps unchanged. |
| v0.3.0 | 2026-05-24 | Made the model self-sufficient: removed the per-substep "Competency mapping (PDS domain)" blocks and all PDS Competence Model cross-references (incl. the [OUTSIDE MODEL] flag, a competency-model concern). Cross-model intersections will be defined separately later. Methods/tools content unchanged. |
| v0.4.0 | 2026-05-24 | Added Disease Understanding (new, before Target ID) and Modality Selection (new, replacing the Hit Identification stub) as written substeps. Added a "Key questions" block to the five early Pre-clinical substeps, sourced from the CPDSE early-pipeline question board. Now 14 substeps, 8 written. |
| v0.5.0 | 2026-05-24 | Filled in all 6 remaining stubs (Candidate Selection, Preclinical DMPK/tox, Phase I/II/III, Regulatory, Manufacturing, Market Access). Normalised every substep to the same 3-part form by adding a "Key questions" block to the three written substeps that lacked one (Biomarker Development, Clinical Pharmacology, Pharmacoepidemiology). All 14 substeps now written; 0 stubs. |
| v0.6.0 | 2026-05-24 | Redundancy pass (14→13 substeps). Merged Candidate Selection into **Lead Optimisation & Candidate Selection** (nomination is the gate ending lead opt; removed the duplicated MPO / developability / TPP methods). Renamed "Preclinical (DMPK, tox)" → **Nonclinical Safety & DMPK** (removes the clash with the Pre-clinical tier name). De-duplicated method lists: exploratory stratification / multi-omics now sit only in Disease Understanding (Biomarker Development consumes them); estimands / multiplicity / missing-data now sit only in Phase I/II/III (Regulatory packages them to standard). |
| v0.7.0 | 2026-05-24 | Added **Formulation & Drug Product Development (CMC)** as the last Pre-clinical substep (13→14). Owns the formulation-specific DS methods (DoE/mixture designs, dissolution/IVIVC, PBBM, shelf-life kinetics, excipient compatibility, LNP/GalNAc delivery optimisation) that were previously unrepresented; cross-references developability (upstream, Lead Opt & Candidate Selection) and QbD/process control (downstream, Manufacturing) rather than duplicating them. |
| v0.8.0 | 2026-05-25 | Renamed "Pharmacoepidemiology" → **Pharmacovigilance & Pharmacoepidemiology** (still 14 substeps) and made the two post-market disciplines co-equal. Expanded the pharmacovigilance DS methods — spontaneous-reporting disproportionality (FAERS/VigiBase/EudraVigilance, PRR/ROR), Bayesian signal detection (BCPNN, MGPS/EBGM), NLP on case narratives/literature, ICSR de-duplication — which were previously a single line. Noted PV's tendrils: trial safety in Phase I/II/III, RMP/REMS in Regulatory. |
</content>
</invoke>
