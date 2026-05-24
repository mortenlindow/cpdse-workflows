# PDS Competence Model

The Pharmaceutical Data Science (PDS) competence model. Seven top-level domains, 30 sub-areas, ~123 competencies. Each competency is rated on a 5-level scale (Awareness → Expertise) inspired by the Dreyfus model.

The level definitions are deliberately the *same across all competencies*. See [Level_Rubric.md](Level_Rubric.md) for the full L1–L5 behavioural rubric and writing rules. In short:

- **L1 Awareness** — recognises the concept; cannot yet do it.
- **L2 Familiarity** — can do it from a template, with someone to ask.
- **L3 Proficiency** — independently delivers usable work on standard pharma problems. *(Reference level on the radar.)*
- **L4 Mastery** — handles non-standard cases; the person others escalate to.
- **L5 Expertise** — sets the standard; teaches, publishes, or open-sources.

L3 is the **target working level**, but no one is expected to be at L3 in *every* competency. Each role profile picks a subset.

For each sub-area we give a single pooled block (typical stack + 3–5 pharma examples tagged `competency @ level`), then one short indicator sentence per level for each competency. `—` means the level genuinely doesn't apply to that competency.

Tools default to the open-source R/Python ecosystem, with a preference for tidyverse / Hadley Wickham packages on the R side.

---

## Computing & Programming

### Computational Thinking

**Typical stack:** base R, Python stdlib (`itertools`, `functools`, comprehensions), `dplyr` and `purrr` for tidy pipelines; `NumPy`, `SciPy`, `data.table`, and profilers (`profvis`, `microbenchmark`, `timeit`) at higher levels.

**Pharma examples** *(each anchored to one or more competencies at a specific level)*:
- Cohort matching in a pharmacovigilance database — *Algorithmic Thinking @ L3*
- An ETL pipeline for clinical trial data composed from small pure functions — *Functional Thinking @ L3*
- Real-time pharmacokinetic processing from wearables, profiled and tuned — *Algorithmic Thinking @ L4; Complexity Theory @ L4*
- Approximating drug–target interaction scoring when the exact problem is intractable — *Complexity Theory @ L4*
- A team-adopted internal pattern for reproducible pharma data pipelines — *Algorithmic Thinking @ L5; Functional Thinking @ L5*

#### Algorithmic Thinking
- **L1** — Recognise loops, conditionals, and recursion in someone else's code and explain in plain language what it does.
- **L2** — Translate a worked algorithm (e.g. sorting adverse events by severity) into Python or R from a tutorial, and predict the result of small changes.
- **L3** — Design and implement an algorithm for a new pharma task (e.g. deduplicating adverse-event reports across sources) without supervision, and document the assumptions.
- **L4** — Notice when the textbook approach won't scale or won't fit messy real data, and choose or adapt a better one (e.g. swap a quadratic match for a hash join when the patient registry grows).
- **L5** — Define the team's algorithmic patterns, contribute to an open-source pharma toolkit, or set the standard others follow.

#### Functional Thinking
- **L1** — Recognise pure functions, immutability, and `map`/`filter`/`reduce` in code; explain why a transformation is "side-effect free".
- **L2** — Use `purrr::map` or Python comprehensions / `functools` to apply a transformation across a list of patient or dosage records, following an example.
- **L3** — Build a functional pipeline end-to-end for a pharma ETL or analysis task (e.g. clinical data harmonisation), composing small pure functions.
- **L4** — Refactor an imperative or fragile pipeline into a robust functional one, parallelise where worthwhile, and explain the trade-offs to the team.
- **L5** — Architect functional patterns that other teams adopt — shared libraries, internal style guide, or open-source contribution.

#### Complexity Theory
- **L1** — Recognise that some pharma problems (cohort matching, dosing optimisation, sequence alignment) get expensive fast, and tell "feasible" from "intractable" at a high level.
- **L2** — Use `timeit` or `microbenchmark` to measure runtime on a small dataset and notice when growth looks non-linear.
- **L3** — Compare candidate algorithms on big-O grounds and pick the right one for the data size at hand (when to index, when to stream, when a join is the wrong shape).
- **L4** — Recognise NP-hard structure in a real pharma problem (drug–target scoring, scheduling, study design) and choose an approximation, heuristic, or sampling strategy with a defensible guarantee.
- **L5** — Advance the practice — publish, contribute novel heuristics, or set up a standard approach for hard problems that the wider org adopts.

### Computing & Computing Systems

**Typical stack:** local Linux/macOS shell, Python and R runtimes; AWS / GCP / Azure managed services (S3/BigQuery/EFS), containers (Docker), batch and Spark-style frameworks (`pyspark`, `arrow`, `duckdb`, `data.table`) for large data.

**Pharma examples:**
- Running a clinical-trial analysis from a local laptop without breaking reproducibility — *Computing & Computer Fundamentals @ L3*
- Lifting an analysis pipeline into a managed cloud workspace with controlled patient-data access — *Cloud Computing @ L3*
- Recognising when a pharmacovigilance dataset has outgrown the laptop and a big-data system is needed — *Big Data Systems (Concept Introduction) @ L2*
- Running a multi-million-row genomics or claims analysis on Spark / DuckDB / Arrow with sensible partitioning — *Big Data Systems (Application) @ L4*

#### Computing & Computer Fundamentals
- **L1** — Explain what files, processes, memory, and an operating system are, and where electronic health records live in that picture.
- **L2** — Use the shell to navigate, copy, and run scripts; explain the difference between local and shared storage for patient data.
- **L3** — Set up a working pharma analysis environment (Python or R, virtualenv/renv, dependencies) and run analyses reproducibly on a laptop.
- **L4** — Diagnose performance, memory, and permission issues that block a pharma pipeline; choose appropriate hardware and storage for the workload.
- **L5** — Set engineering standards for the team's compute environments and tooling.

#### Cloud Computing
- **L1** — Explain what a cloud provider offers (compute, storage, identity) and why pharma workloads often run there under access controls.
- **L2** — Spin up a managed notebook or VM in a sandbox tenant and run a small analysis, following an internal guide.
- **L3** — Run a real pharma analysis end-to-end in a controlled cloud workspace, including managed storage and access policies.
- **L4** — Design a cost- and access-aware cloud setup for a pharma project: storage tiers, IAM, regions for residency, audit trails.
- **L5** — Define the team's reference cloud architecture for regulated pharma data, or contribute to organisation-level patterns.

#### Big Data Systems (Concept Introduction)
- **L1** — Recognise terms (Spark, Hadoop, MPP, columnar storage, partitioning) and explain at a high level when "big" matters in pharma.
- **L2** — Read an existing big-data pipeline diagram or notebook and explain its main steps.
- **L3** — Decide, given a pharma dataset, whether a single-machine tool (`data.table`, `duckdb`, `arrow`) suffices or a distributed system is warranted.
- **L4** — — *(merges with Big Data Systems (Application) at this level)*
- **L5** — — *(merges with Big Data Systems (Application) at this level)*

#### Big Data Systems (Application)
- **L1** — — *(introduced via the Concept Introduction competency)*
- **L2** — Run a small Spark, BigQuery, or DuckDB job on a sample dataset following an example.
- **L3** — Implement a pharma analysis on a large dataset (claims, registries, omics) using a distributed engine, with sensible partitioning and joins.
- **L4** — Tune real workloads — diagnose skew, broadcast joins, push-down predicates, choose file formats — for cost and latency on realistic pharma data.
- **L5** — Architect the team's big-data patterns and platform choices for pharma scale.

### Programming

**Typical stack:** Python (with `numpy`, `pandas`, `pytest`), R (`tidyverse`, `data.table`, `testthat`); Quarto / R Markdown / Jupyter for literate analysis; LLM coding assistants (Copilot, Claude, Cursor) at L2+; profilers and benchmarks (`profvis`, `microbenchmark`, `timeit`, `cProfile`) at L3+.

**Pharma examples:**
- A first script to summarise a small clinical trial table — *Getting Started @ L1; Data and Variables @ L2*
- A reusable function library for adverse-event coding lookups — *Functions @ L3; Libraries @ L3*
- A test suite catching a regression in a dose-conversion routine before production — *Testing and Debugging @ L3*
- Speeding up a slow PK/PD simulation by 50× through profiling and vectorisation — *Code Optimization @ L4*
- Reviewing and constraining LLM-generated analysis code for pharma compliance — *LLM Assisted Coding @ L4*

#### Getting Started
- **L1** — Recognise what code is and what an interpreter does; open a notebook and run an example.
- **L2** — Run and edit a short pharma script (e.g. summarise a CSV of adverse events) following a tutorial.
- **L3** — Set up a working analysis environment (Python or R, package manager, IDE) and produce a small reproducible script for a real pharma question.
- **L4** — — *(skill is fully covered by L3; further mastery shows up in other Programming competencies)*
- **L5** — —

#### Data and Variables
- **L1** — Recognise basic data types (numbers, strings, booleans, dates) in pharma data.
- **L2** — Read a CSV/Excel/SAS file into Python or R and inspect types, missing values, and basic statistics.
- **L3** — Choose appropriate data structures (data frame, dict, list, factor) for a pharma analysis and avoid common type-coercion bugs (date parsing, factor encoding).
- **L4** — Design clean schemas for messy real-world pharma data and explain trade-offs (long vs. wide, factor vs. character, numeric precision).
- **L5** — Set conventions the team uses for types, encodings, and date/time handling across pharma projects.

#### Libraries
- **L1** — Recognise that R/Python rely on packages and know a few core ones (`tidyverse`, `pandas`).
- **L2** — Install and load packages, follow examples from their docs to apply them to pharma data.
- **L3** — Choose appropriate libraries for a task (e.g. `survival` vs. `flexsurv`; `pandas` vs. `polars`) and combine them in an analysis.
- **L4** — Evaluate libraries by quality, license, maintenance, and validation status — relevant for pharma reproducibility and compliance.
- **L5** — Author or maintain an internal package, or contribute to a relevant open-source package used in pharma.

#### Functions
- **L1** — Recognise function definitions and calls; explain inputs and outputs.
- **L2** — Write a small function (e.g. unit conversion for dosages) following an example.
- **L3** — Decompose a pharma analysis into well-named, testable functions with clear inputs and outputs.
- **L4** — Design APIs that survive change — sensible defaults, documented edge cases, careful handling of missing data.
- **L5** — Set the team's standards for function design and API style.

#### Loops and Branching
- **L1** — Recognise `for`/`while` loops and `if`/`else` branches in pharma code.
- **L2** — Write loops and conditionals to iterate over a small list of records and apply rules.
- **L3** — Replace ad hoc loops with vectorised, mapped, or grouped operations where appropriate (`dplyr`, `purrr`, `pandas` `groupby`, `numpy`).
- **L4** — Choose the right control-flow shape for performance and clarity on real pharma data sizes; avoid common pitfalls (in-place mutation, off-by-one, hidden coercions).
- **L5** — — *(further mastery shows up in Code Optimization)*

#### Testing and Debugging
- **L1** — Recognise an error traceback and read it to find the failing line.
- **L2** — Add `print` / `browser()` / a debugger and walk through a function on a small example.
- **L3** — Write unit tests (`pytest`, `testthat`) for pharma analysis code; reproduce a bug with a minimal example before fixing it.
- **L4** — Set up CI for an analysis package, including tests against representative pharma fixtures, and use coverage and property-based testing where it pays off.
- **L5** — Define the team's testing standards and validation expectations for code that touches regulated pharma data.

#### LLM Assisted Coding
- **L1** — Recognise what an LLM coding assistant can and can't do, and the data-handling implications for pharma code.
- **L2** — Use an assistant to scaffold simple scripts and explain code; verify the output against documentation.
- **L3** — Use LLM assistants effectively for everyday pharma analysis work — generating code, refactoring, writing tests — while reading and validating every diff.
- **L4** — Constrain assistants for sensitive pharma contexts: ground them in real schemas, set up guardrails, audit and review generated code with a sceptical eye.
- **L5** — Define the team's policy and patterns for LLM-assisted coding in regulated pharma settings.

#### Code Optimization
- **L1** — Recognise that some code is "slow" and that this can matter (cost, latency, deadlines).
- **L2** — Time a small piece of pharma code with `timeit` or `microbenchmark` and read the result.
- **L3** — Profile a real pharma analysis, identify the hot spot, and apply standard fixes (vectorisation, indexing, avoiding repeated I/O).
- **L4** — Re-architect a slow pharma pipeline (memory layout, parallelism, batching, columnar formats) for an order-of-magnitude speed-up while preserving correctness.
- **L5** — Set the team's performance standards and tooling for compute-heavy pharma workloads.

### Workflow & Reproducibility

**Typical stack:** Git, GitHub/GitLab; Quarto / R Markdown / Jupyter; `renv`, `uv`/`venv`, `conda`; Make / `targets` / Snakemake / Nextflow for pipelines; pre-commit hooks, code style (`ruff`, `lintr`, `styler`, `black`).

**Pharma examples:**
- A clinical analysis that runs end-to-end from raw inputs to a Quarto report with one command — *Reproducible Analysis @ L3*
- A pull-request review that catches a silent data-filter change before it reaches a regulator — *Source Code (Version) Control Systems @ L3; Collaboration @ L3*
- An internal style guide and pre-commit setup adopted across pharma teams — *Documentation and Code Standards @ L5*
- A `targets`/Nextflow pipeline that re-derives a regulatory submission deterministically months later — *Reproducible Analysis @ L4*

#### Documentation and Code Standards
- **L1** — Recognise the difference between commented and uncommented code, and what a docstring is.
- **L2** — Add docstrings, README, and inline comments to a small pharma script, following examples.
- **L3** — Apply a style guide and lint/format tools across an analysis, and write documentation that lets a colleague reproduce the work.
- **L4** — Establish documentation patterns for a pharma project (analysis plan, data dictionary, decision log) and review others' work against them.
- **L5** — Define and own the team's coding and documentation standards.

#### Source Code (Version) Control Systems
- **L1** — Recognise what Git is and read a commit history.
- **L2** — Clone, commit, push, and open a pull request on a small project, following a guide.
- **L3** — Use branches, pull requests, and code review fluently for everyday pharma analysis work; resolve typical merge conflicts.
- **L4** — Design a branching, review, and release strategy for a regulated pharma project (audit trail, signed commits, protected branches, traceable releases).
- **L5** — Set Git/CI conventions for the team or contribute to organisation-level standards.

#### Reproducible Analysis
- **L1** — Recognise reasons that an analysis might not reproduce (random seed, hidden state, missing dependencies, non-deterministic inputs).
- **L2** — Run someone else's analysis from a clean checkout following the README, and report what's missing.
- **L3** — Build a literate, reproducible analysis (Quarto / R Markdown / Jupyter + locked environment) that another analyst can re-run from raw inputs.
- **L4** — Design a pipeline (`targets`, Snakemake, Nextflow, Make) that re-derives a regulatory or publication-grade output deterministically, with tests and provenance.
- **L5** — Define reproducibility standards for the team's regulated pharma work.

#### Collaboration
- **L1** — Recognise the basic etiquette of shared codebases (don't commit to main, write a clear commit message).
- **L2** — Open a small pull request, respond to review comments, and merge once approved.
- **L3** — Review peers' pharma code with substantive, kind feedback; coordinate work across two or three contributors on the same analysis.
- **L4** — Lead a multi-person pharma analysis: scope, divide work, set up review and merge norms, unblock teammates.
- **L5** — Shape the collaboration culture across pharma analytics teams.

---

## Data Acquisition & Management

### Critical Thinking

**Typical stack:** general-purpose tooling — notebooks, dashboards, structured analysis-plan templates; bias and quality checklists.

**Pharma examples:**
- Spotting that an apparent treatment effect is driven by a coding change in the source EHR — *Critical Thinking when working with data @ L4*
- Recognising that a registry over-represents a particular site or population — *Awareness of high level issues and challenges associated with data @ L3*
- Writing a "pre-analysis questions" doc that surfaces likely biases before the analysis begins — *Critical Thinking when working with data @ L3*

#### Critical Thinking when working with data
- **L1** — Recognise that data can be wrong, biased, or misleading even when it looks complete.
- **L2** — Apply a checklist to a pharma dataset: where did it come from, how was it collected, what's missing, what's been transformed.
- **L3** — Routinely interrogate a pharma dataset before analysis — origin, biases, exclusions, lineage — and document assumptions.
- **L4** — Recognise non-obvious data issues (informative missingness, regime change, coding drift, label leakage) and adjust analyses or design.
- **L5** — Define the team's habits and rituals for sceptical data work.

#### Awareness of high level issues and challenges associated with data
- **L1** — Recognise common high-level pharma data challenges: missingness, fragmentation across sources, regulatory constraints, confounding.
- **L2** — Describe these challenges as they appear in a specific pharma dataset.
- **L3** — Anticipate these challenges in a new project and plan for them in the analysis design.
- **L4** — Map the data landscape for a pharma question across sources (clinical, real-world, genomic, regulatory) and reason about gaps.
- **L5** — Set strategy for how the org acquires, integrates, and reasons about pharma data over time.

### Data Collection

**Typical stack:** REDCap and similar EDC platforms; surveys; web/API ingestion (`httr2`, `requests`); registries (ClinicalTrials.gov, GBD, EMA); literature search tools.

**Pharma examples:**
- Designing a CRF that yields analysable data first time — *Data collection tools and methods @ L3*
- Pulling structured trial outcomes from ClinicalTrials.gov by API — *Data collection tools and methods @ L3*
- Building a search strategy across PubMed, Embase, and EU CTR for a meta-analysis — *Repositories and search methods @ L3*

#### Data types
- **L1** — Distinguish numeric, categorical, ordinal, date/time, and free-text data; recognise structured vs. unstructured.
- **L2** — Classify the variables in a pharma dataset and pick appropriate summaries.
- **L3** — Choose the right type and encoding for each variable in a new pharma dataset, including dates, units, and missingness conventions.
- **L4** — Design data type strategy for non-trivial pharma data (longitudinal, hierarchical, sparse, free text + codes).
- **L5** — Define standards for variable typing across the team's pharma datasets.

#### Data collection tools and methods
- **L1** — Recognise the main pharma data collection methods: EDC, eCOA, surveys, APIs, registries, sensors.
- **L2** — Use one of these tools (e.g. REDCap or an HTTP API) to collect a small pharma dataset following an example.
- **L3** — Design and implement a data collection plan for a pharma study: instrument, fields, validation, exports.
- **L4** — Adapt collection to non-standard contexts (devices, multi-language eCOA, partner data, real-world streaming) and ensure quality at source.
- **L5** — Define the team's playbook for pharma data collection across study types.

#### Repositories and search methods
- **L1** — Recognise the main pharma repositories (PubMed, ClinicalTrials.gov, EMA/FDA portals, EGA, dbGaP, GBD, real-world data vendors).
- **L2** — Run a basic search in one of them and download a structured result.
- **L3** — Build a reproducible, documented search strategy across multiple sources for a real pharma question.
- **L4** — Combine and deduplicate across repositories with awareness of bias and gaps; use programmatic APIs where it pays off.
- **L5** — Set the team's standards for systematic search and acquisition of pharma evidence.

### Data Curation

**Typical stack:** `dplyr`, `tidyr`, `pandas`, `polars`, `data.table`; controlled vocabularies (MedDRA, SNOMED CT, LOINC, ATC, RxNorm, ICD); validation tools (`pointblank`, `pandera`, `great_expectations`).

**Pharma examples:**
- Standardising adverse-event terms via MedDRA across studies — *Data standardization and transformation @ L3*
- Reshaping a long-format lab dataset into per-patient summaries — *Data conversion (between types) @ L3*
- Cleaning a pooled real-world dataset with ~30 source-specific quirks — *Data Cleaning @ L4*

#### Data standardization and transformation
- **L1** — Recognise that the same concept can be encoded many ways across pharma sources (units, codes, formats).
- **L2** — Apply a mapping table or controlled vocabulary to a small dataset following an example.
- **L3** — Standardise a real pharma dataset using accepted vocabularies (MedDRA, ATC, LOINC, SNOMED) and document the mappings.
- **L4** — Design transformation strategies for messy multi-source pharma data with conflicting encodings and partial mappings.
- **L5** — Define the team's standardisation patterns and govern shared vocabularies and crosswalks.

#### Data conversion (between types)
- **L1** — Recognise that converting between types (date, numeric, factor, character) can lose or distort information.
- **L2** — Convert types in a small dataset using `as.*` / `pd.to_*` functions, checking before and after.
- **L3** — Convert real pharma data between common shapes (long ↔ wide, JSON ↔ tabular, EAV ↔ wide) with explicit checks.
- **L4** — Handle non-trivial conversions (units, time zones, schema evolution) with auditable logic.
- **L5** — — *(further mastery covered by Standardization and by Integration in EMA)*

#### Data Cleaning
- **L1** — Recognise common data quality issues — duplicates, impossible values, encoding errors, missing data patterns.
- **L2** — Apply standard cleaning steps to a small pharma dataset following a checklist.
- **L3** — Clean a real pharma dataset end-to-end with documented decisions, validations, and a record of what was changed and why.
- **L4** — Design cleaning logic for messy real-world or pooled pharma data, including informative missingness and regime change.
- **L5** — Set the team's standards and tooling for pharma data cleaning.

### Data Organization

**Typical stack:** relational databases (PostgreSQL, SQLite, DuckDB); columnar formats (Parquet, Arrow); CDISC SDTM/ADaM; metadata standards (Dublin Core, schema.org, CDISC Define-XML).

**Pharma examples:**
- Organising a study into clear "raw / intermediate / analysis" layers — *Basic data organization methods and tools @ L3*
- Designing a study-data SQL schema that survives protocol amendments — *Database systems @ L4*
- Authoring a Define-XML / data dictionary for a regulatory submission — *Creation and use of meta data @ L4*

#### Basic data organization methods and tools
- **L1** — Recognise the difference between flat files, spreadsheets, and databases; know that "tidy data" is a thing.
- **L2** — Lay out a small pharma project's files and folders following a template.
- **L3** — Organise a pharma project into raw / intermediate / analysis layers with a clear file naming and folder convention.
- **L4** — Design data organisation for a multi-study, multi-team pharma programme.
- **L5** — Set the team's standards for project and data layout.

#### Database systems
- **L1** — Recognise SQL, tables, joins, and indexes; explain why a database is sometimes better than CSV files.
- **L2** — Run basic SELECT/JOIN queries against a pharma data warehouse following examples.
- **L3** — Design and use a relational schema (or a DuckDB/SQLite store) for a real pharma project, with appropriate keys and indexes.
- **L4** — Tune queries on real pharma data; choose between relational, columnar, and document stores; reason about transactions and concurrency.
- **L5** — Define the team's data-platform patterns for pharma analytics.

#### Creation and use of meta data
- **L1** — Recognise what metadata is — variable definitions, units, provenance, controlled vocabularies — and why pharma needs it.
- **L2** — Read and use a data dictionary or codebook for a pharma dataset.
- **L3** — Author a usable data dictionary for a real pharma dataset, including variable definitions, units, and provenance.
- **L4** — Apply CDISC Define-XML / SDTM/ADaM metadata for regulated submissions, or equivalent in another regime.
- **L5** — Define the team's metadata standards across studies.

### Data Quality

**Typical stack:** data validation frameworks (`pointblank`, `pandera`, `great_expectations`); checklists and quality dashboards; provenance tooling.

**Pharma examples:**
- A validation suite that fails the build when a study CSV ships a duplicate USUBJID — *Data quality characteristics @ L3; Data Assessment @ L3*
- Rejecting a third-party real-world dataset whose source-coding drift can't be explained — *Assessment of data sources(trustworthiness) @ L4*
- A signed-off quality report for a regulatory submission — *Evaluation of the quality of datasets @ L4*

#### Data quality characteristics
- **L1** — Recognise the standard quality dimensions: completeness, accuracy, consistency, timeliness, validity, uniqueness, provenance.
- **L2** — Describe these characteristics for a small pharma dataset.
- **L3** — Define quality criteria and acceptance thresholds for a real pharma dataset and check them.
- **L4** — Tailor quality definitions to the analytic purpose (a dataset can be "good enough" for one question and not another).
- **L5** — Set the team's data-quality framework and acceptance criteria.

#### Data Assessment
- **L1** — Recognise basic data-profiling outputs (missingness, ranges, frequency tables).
- **L2** — Run a profiling tool on a pharma dataset and read the report.
- **L3** — Run a structured assessment of a real pharma dataset and report findings to stakeholders.
- **L4** — Design assessment that catches subtle issues — drift, leakage, informative missingness, source-coding change.
- **L5** — Set the team's standards and tooling for pharma data assessment.

#### Assessment of data sources(trustworthiness)
- **L1** — Recognise that data sources differ in trustworthiness (e.g. peer-reviewed registry vs. scraped web data).
- **L2** — Describe a pharma data source's origin, governance, and known issues.
- **L3** — Assess a candidate pharma data source for fitness for a specific question — provenance, licence, coverage, biases.
- **L4** — Lead a vendor or partner data assessment for a regulated pharma context, including audits and contractual checks.
- **L5** — Define the team's vendor/source qualification framework.

#### Evaluation of the quality of datasets
- **L1** — Recognise that "quality" is dataset-and-purpose specific.
- **L2** — Apply a quality scoring template to a small pharma dataset.
- **L3** — Produce a written quality evaluation of a pharma dataset for a specific analytic purpose.
- **L4** — Sign off (or reject) a dataset for regulated use with a defensible report; recommend remediation.
- **L5** — Set the team's evaluation standards and review process.

### Data Security & Re-use

**Typical stack:** access control (IAM, role-based access); secure storage (encrypted S3/Azure Blob); pseudonymisation/tokenisation; FAIR principles; DOI / data citation tooling; data-sharing platforms (Vivli, YODA, EGA, dbGaP, controlled-access registries).

**Pharma examples:**
- Pseudonymising a clinical dataset before sharing with an external statistician — *Data classification, risk assessment, storage and backup @ L3*
- Depositing trial data in Vivli with a DOI for downstream re-use — *Data preservation and FAIR principles @ L3; Methods and platforms for sharing data @ L3*
- Setting an org-wide policy for trial-data sharing under EMA Policy 0070 — *Data preservation and FAIR principles @ L5*

#### Data classification, risk assessment, storage and backup
- **L1** — Recognise data classification levels (public, internal, sensitive, regulated) and what each means for handling.
- **L2** — Apply the right storage and access controls to a small pharma dataset following policy.
- **L3** — Classify and protect a real pharma dataset: pseudonymisation, access control, encryption at rest, backups, retention.
- **L4** — Design risk-aware storage architectures for sensitive pharma data, with defensible audit trails.
- **L5** — Define the team's classification and security framework.

#### Data preservation and FAIR principles
- **L1** — Recognise the FAIR principles (Findable, Accessible, Interoperable, Reusable).
- **L2** — Apply FAIR-aligned conventions (DOIs, persistent IDs, controlled vocabularies) to a small pharma dataset.
- **L3** — Make a real pharma dataset FAIR within its access constraints and deposit it in an appropriate repository.
- **L4** — Lead the FAIR-ification of a programme's data assets, including legacy datasets.
- **L5** — Define the team's FAIR-by-default standards and tooling.

#### Methods and platforms for sharing data
- **L1** — Recognise the main pharma data-sharing platforms (Vivli, YODA, EGA, dbGaP, in-house) and their access models.
- **L2** — Submit or request a small dataset through one of these platforms, following the platform's guide.
- **L3** — Share or obtain a real pharma dataset through the right platform with appropriate consent, agreements, and controls.
- **L4** — Design sharing strategy for a study or programme balancing transparency, IP, consent, and regulation.
- **L5** — Set the team's sharing strategy and engage with platform/standards bodies.

#### Widely-accepted data citation methods
- **L1** — Recognise data citation as a practice and recognise DOIs for datasets.
- **L2** — Cite a pharma dataset correctly in a report or paper following examples.
- **L3** — Mint and use DOIs / persistent identifiers for the team's pharma datasets and apply them in publications and submissions.
- **L4** — — *(further mastery is rare and folds into FAIR / Sharing competencies)*
- **L5** — —

### Research Data Management

**Typical stack:** Data Management Plan templates (DCC, NIH, Horizon Europe); CDISC where relevant; lab notebooks and ELN tooling.

**Pharma examples:**
- A study-level DMP that survives an EMA inspection — *Data management plans @ L4*
- A repeatable DMP template adopted across the team — *Data management plans @ L5*

#### Data management plans
- **L1** — Recognise what a Data Management Plan is and why funders and regulators require one.
- **L2** — Fill in a DMP template for a small pharma project from a worked example.
- **L3** — Author a complete, realistic DMP for a real pharma study and execute against it.
- **L4** — Author and maintain DMPs for regulated pharma studies through the full lifecycle, including amendments and audits.
- **L5** — Define the team's DMP templates, processes, and reviews.

---

## Ethics, Legislation & Privacy

### Data Science Ethics

**Typical stack:** organisational ethics codes; bias-detection tooling (`fairlearn`, `aequitas`); environmental footprint estimators (`codecarbon`); pharma-specific ethics guidance (CIOMS, Declaration of Helsinki).

**Pharma examples:**
- Catching that a model under-serves an under-represented patient subgroup — *Bias in data science and algorithms @ L4*
- Choosing between two analysis pipelines on energy/cost grounds at comparable accuracy — *Environmental and social sustainability of data science practices @ L3*
- Deciding not to ship a feature because of a foreseeable downstream harm — *Ethical dilemmas in pharmaceutical data science @ L4*

#### Concepts in data science ethics
- **L1** — Recognise the core concepts: consent, privacy, fairness, accountability, transparency, dual use.
- **L2** — Describe these concepts as they apply to a specific pharma project.
- **L3** — Apply ethics frameworks routinely in pharma project decisions and document the reasoning.
- **L4** — Recognise non-obvious ethical issues (proxy variables, group privacy, deployment harms) and act on them.
- **L5** — Lead the team's ethics practice and contribute to organisation- or industry-level standards.

#### Bias in data science and algorithms
- **L1** — Recognise sources of bias: sampling, measurement, label, deployment, historical.
- **L2** — Apply a bias checklist to a pharma dataset or model output.
- **L3** — Quantify and report subgroup performance and bias for a real pharma model, and act on the results.
- **L4** — Diagnose and mitigate bias in non-trivial pharma settings (intersectional subgroups, label noise, deployment shift).
- **L5** — Set the team's standards for bias measurement and mitigation in pharma analytics.

#### Environmental and social sustainability of data science practices
- **L1** — Recognise that compute, storage, and modelling choices have environmental and social costs.
- **L2** — Estimate the energy or compute cost of a pharma analysis using simple tooling.
- **L3** — Choose between approaches partly on sustainability grounds in pharma projects (right-sized models, efficient pipelines, regional compute).
- **L4** — Lead sustainability-aware design for compute-heavy pharma workloads.
- **L5** — Set the team's sustainability practices.

#### Ethical dilemmas in pharmaceutical data science
- **L1** — Recognise common pharma-specific dilemmas (off-label inference, drug repurposing risks, consent for secondary use, dual-use research).
- **L2** — Describe a pharma dilemma and the relevant stakeholders.
- **L3** — Reason through a real pharma dilemma using an ethics framework, document the decision, and consult appropriately.
- **L4** — Lead the resolution of complex pharma ethics dilemmas with cross-functional input (clinical, legal, patient advocacy).
- **L5** — Help shape organisational or industry positions on pharma data ethics.

### Legislation

**Typical stack:** GDPR, HIPAA, GxP, EMA/FDA guidance, ICH E6/E9, EU AI Act; country-specific health-data laws; copyright and licensing frameworks.

**Pharma examples:**
- Choosing a lawful basis under GDPR for a real-world data study — *Central legal and regulatory frameworks @ L3*
- Negotiating data licences for a multi-source meta-analysis — *Copyright and intellectual property concerns @ L3*
- Preparing for an EMA inspection of an analysis pipeline — *Central legal and regulatory frameworks @ L4*

#### Central legal and regulatory frameworks
- **L1** — Recognise the main frameworks (GDPR, HIPAA, GxP, ICH, EMA/FDA guidance, EU AI Act) and what they govern.
- **L2** — Identify which frameworks apply to a given pharma project at a high level.
- **L3** — Apply the relevant frameworks routinely in a pharma analytics project — design choices, documentation, controls.
- **L4** — Lead compliance for a complex pharma project involving multiple jurisdictions or evolving regulation (e.g. EU AI Act applied to a clinical model).
- **L5** — Engage with regulators and shape the team's compliance posture.

#### Copyright and intellectual property concerns
- **L1** — Recognise that data, code, and models can be subject to copyright, licensing, patents, and trade secrets.
- **L2** — Read a dataset or library licence and explain what it permits.
- **L3** — Apply correct licensing and IP handling to a real pharma project (data, code, model artefacts).
- **L4** — Negotiate or design IP arrangements for collaborative pharma work and unusual data uses.
- **L5** — Define the team's IP and licensing strategy.

### Privacy

**Typical stack:** pseudonymisation/de-identification tools; access control and audit; informed-consent platforms; differential privacy and synthetic data tooling at higher levels; AI transparency documentation (model cards, datasheets, EU AI Act records).

**Pharma examples:**
- Proper de-identification of a registry dataset before secondary analysis — *Knowledge and compliance with privacy and data security regulations @ L3*
- An informed-consent process designed for a digital biomarker sub-study — *Design and implementation of respectful and legal informed consent processes @ L4*
- A model card and risk assessment for an AI tool used in clinical operations — *Ensure that AI systems used are transparent and aligned with legal and ethical norms @ L4*

#### Knowledge and compliance with privacy and data security regulations
- **L1** — Recognise the main privacy regulations relevant to pharma (GDPR, HIPAA, country-specific health-data laws) at a high level.
- **L2** — Apply standard privacy controls (access, encryption, pseudonymisation) to a small dataset following policy.
- **L3** — Run a real pharma project under the relevant privacy regulations end-to-end, with documented controls.
- **L4** — Design privacy strategy for a complex pharma project (multi-jurisdiction, real-world data, partner sharing).
- **L5** — Set the team's privacy practices and engage with DPOs and regulators.

#### Design and implementation of respectful and legal informed consent processes
- **L1** — Recognise the elements of valid informed consent for pharma research.
- **L2** — Read an existing consent form / process and identify its main elements.
- **L3** — Implement a consent process for a pharma study that meets legal and ethical requirements and is genuinely respectful.
- **L4** — Design consent for novel pharma contexts (digital biomarkers, secondary use, dynamic consent, vulnerable populations).
- **L5** — Define the team's consent standards and contribute to organisational practice.

#### Act with integrity when handling sensitive data
- **L1** — Recognise that sensitive pharma data (patient identifiers, genomics, mental health) requires elevated care.
- **L2** — Follow the team's handling rules for sensitive data in a small project.
- **L3** — Routinely apply sensitivity-appropriate handling — minimisation, segregation, access logs, secure transfer — across pharma work.
- **L4** — Lead the integrity practice on a sensitive pharma programme, including audits and incident response.
- **L5** — Set the team's integrity expectations and culture.

#### Application of legal and ethical standards to ensure responsible and competent data handling
- **L1** — Recognise that legal and ethical standards translate into concrete handling requirements.
- **L2** — Apply the team's standard checklist to a small pharma dataset.
- **L3** — Operate consistently within applicable legal and ethical standards on a real pharma project, with traceable decisions.
- **L4** — Resolve novel cases where standards are silent or in tension, with appropriate consultation.
- **L5** — Define and maintain the team's combined legal-and-ethical handling framework.

#### Ensure that AI systems used are transparent and aligned with legal and ethical norms
- **L1** — Recognise the AI-specific transparency expectations (intended use, limitations, risk class under EU AI Act, model cards).
- **L2** — Read or fill out a model card for an existing AI tool.
- **L3** — Document an AI system used in a pharma context: purpose, data, evaluation, limitations, risks, monitoring.
- **L4** — Design and govern AI deployment in pharma to meet evolving regulation (EU AI Act, FDA guidance) and internal ethics review.
- **L5** — Set the team's AI governance standards and engage externally.

#### Continuously update knowledge of ethical, legal, and technological developments in PDS
- **L1** — Recognise that ethics, law, and tech are moving fast in PDS and that yesterday's answer may not still hold.
- **L2** — Follow at least one credible source (newsletter, regulator update, professional body) regularly.
- **L3** — Maintain working knowledge across ethics, law, and tech and bring relevant updates into the team's practice.
- **L4** — Lead horizon-scanning for the team and translate developments into concrete changes.
- **L5** — Help shape the field externally — talks, working groups, publications.

---

## Exploration, Mining & Analysis

### (Critical) Evaluation

**Typical stack:** statistical and ML evaluation tooling (`tidymodels`, `scikit-learn` metrics, `dowhy`, `causalml`); reproducibility tools; bias and robustness checklists; sensitivity analysis frameworks.

**Pharma examples:**
- Stating, before unblinding, the assumptions a trial analysis depends on — *Study design & assumptions @ L3*
- Distinguishing association from causation in a real-world effectiveness analysis — *Association & inference @ L3; Causal inference & sensitivity @ L4*
- Showing that a predictive model degrades on a held-out hospital and choosing not to deploy — *Transportability & fairness @ L4; Limitations & Uncertainty @ L4*

#### Study design & assumptions
- **L1** — Recognise that every analysis rests on assumptions about design and data.
- **L2** — Read a study protocol or analysis plan and list its main assumptions.
- **L3** — State and check the assumptions of a real pharma analysis explicitly.
- **L4** — Adapt designs and assumption-checking when reality differs from the protocol (missing strata, protocol deviations, regime change).
- **L5** — Set the team's standards for documenting and challenging assumptions.

#### Association & inference
- **L1** — Recognise the difference between association and causation; recognise statistical inference as a distinct activity.
- **L2** — Run a basic association test on a pharma dataset following an example.
- **L3** — Choose appropriate inferential methods for a real pharma question and interpret them honestly.
- **L4** — Handle non-trivial inference (clustering, multiple comparisons, time-varying confounders) competently.
- **L5** — Set the team's inference standards.

#### Causal inference & sensitivity
- **L1** — Recognise that observational pharma data alone usually doesn't give causal answers; recognise core ideas (confounding, counterfactuals, DAGs).
- **L2** — Read a DAG and a propensity-score analysis and explain its logic.
- **L3** — Apply standard causal inference methods (matching, IPTW, instrumental variables, target trial emulation) to a real pharma question.
- **L4** — Run defensible sensitivity analyses (E-values, tipping-point, negative controls) and act on them.
- **L5** — Lead causal-methods practice in the team or contribute to the field.

#### Model evaluation & robustness
- **L1** — Recognise basic evaluation metrics (accuracy, AUC, calibration, RMSE) and what they do and don't tell you.
- **L2** — Compute standard metrics on a small pharma model following an example.
- **L3** — Evaluate a real pharma model with appropriate metrics, calibration, and held-out data; report transparently.
- **L4** — Stress-test a pharma model — subgroup performance, distribution shift, adversarial inputs — and decide whether it should ship.
- **L5** — Set the team's model-evaluation standards for pharma.

#### Reproducibility
- **L1** — Recognise that an analysis must be reproducible to be trustworthy.
- **L2** — Re-run a peer's pharma analysis from a clean checkout.
- **L3** — Make a real pharma analysis reproducible end-to-end (env, seeds, pipeline, data lineage).
- **L4** — Achieve reproducibility under hard constraints (controlled-access data, regulated environments, multi-team handoffs).
- **L5** — Set the team's reproducibility expectations and tooling.

#### Limitations & Uncertainty
- **L1** — Recognise that every pharma analysis has limitations and that point estimates without uncertainty are usually misleading.
- **L2** — Add confidence intervals or prediction intervals to a small pharma analysis.
- **L3** — Communicate limitations and uncertainty honestly in real pharma analyses to mixed audiences.
- **L4** — Quantify and propagate uncertainty in non-trivial pharma settings (Bayesian, bootstrap, simulation, decision analysis).
- **L5** — Set the team's standards for communicating limitations and uncertainty.

#### Transportability & fairness
- **L1** — Recognise that a model fit on one pharma population may not work on another, and that this matters for fairness.
- **L2** — Compare a pharma model's performance across two subgroups or sites following an example.
- **L3** — Routinely evaluate transportability and subgroup fairness for real pharma models, and act on findings.
- **L4** — Diagnose and address transportability and fairness problems in deployment (recalibration, domain adaptation, refusal-to-deploy).
- **L5** — Set the team's transportability and fairness standards.

### Analysis

**Typical stack:** R (`tidyverse`, `survival`, `tidymodels`, `flexsurv`, `nlmixr`/`mrgsolve`), Python (`pandas`, `scikit-learn`, `lifelines`, `statsmodels`); domain-specific PK/PD tools (NONMEM, Monolix where applicable).

**Pharma examples:**
- A pre-specified hypothesis test for a primary trial endpoint — *Hypothesis testing @ L3*
- A population PK/PD model fit to a phase-2 study — *PK/PD & exposure-response @ L4; Modelling @ L4*
- A survival analysis of time-to-progression with competing risks — *Survival analysis @ L4*
- Feature selection for a high-dimensional biomarker model with proper resampling — *Feature selection & dimensionality reduction @ L4; Resampling design & class imbalance @ L4*

#### Qualitative and quantitative analysis
- **L1** — Recognise the difference between qualitative and quantitative methods and when each is appropriate.
- **L2** — Run basic descriptive analyses on a small pharma dataset following an example.
- **L3** — Choose and apply qualitative or quantitative methods appropriately to a real pharma question.
- **L4** — Combine qualitative and quantitative evidence (e.g. clinician interviews + outcomes data) into a coherent pharma analysis.
- **L5** — Set the team's standards for mixed-methods pharma analysis.

#### Hypothesis testing
- **L1** — Recognise null/alternative hypotheses, type I/II error, p-values, and confidence intervals.
- **L2** — Run a t-test, χ², or simple regression test on a pharma sample following an example.
- **L3** — Choose and run an appropriate test for a real pharma question and interpret it honestly (effect size, CIs, multiplicity).
- **L4** — Handle non-trivial testing (group sequential, multiple endpoints, non-inferiority, Bayesian alternatives) competently.
- **L5** — Set the team's standards for hypothesis testing in pharma.

#### PK/PD & exposure-response
- **L1** — Recognise the basic concepts: absorption, distribution, metabolism, elimination, exposure–response.
- **L2** — Read and interpret a basic PK/PD plot or model output.
- **L3** — Fit standard PK/PD models with appropriate tooling on a real pharma dataset and interpret the results.
- **L4** — Build population PK/PD or exposure–response models that inform real dosing decisions; handle data quirks and covariates.
- **L5** — Lead PK/PD modelling practice in the team or contribute to methods development.

#### Modelling
- **L1** — Recognise statistical modelling as a distinct activity from raw analysis or ML.
- **L2** — Fit a linear or logistic model to a small pharma dataset following an example.
- **L3** — Choose and fit appropriate models (mixed-effects, GLM, GAM, survival) for real pharma questions and validate them.
- **L4** — Handle non-trivial modelling (hierarchical, longitudinal, joint models, missing-data methods) on real pharma data.
- **L5** — Set the team's modelling standards or contribute to methods.

#### Survival analysis
- **L1** — Recognise survival data, censoring, hazard, and Kaplan–Meier curves.
- **L2** — Fit a Kaplan–Meier curve and a Cox model on a pharma sample following an example.
- **L3** — Choose and apply standard survival methods to real pharma data (Cox, parametric, stratified) and check assumptions.
- **L4** — Handle non-trivial survival analyses (competing risks, time-varying covariates, joint longitudinal–survival, frailty) on real pharma data.
- **L5** — Set the team's standards for time-to-event analysis.

#### Feature selection & dimensionality reduction
- **L1** — Recognise why high-dimensional pharma data needs reduction (multicollinearity, overfitting, interpretability).
- **L2** — Run PCA or basic regularisation on a pharma sample following an example.
- **L3** — Choose appropriate selection / reduction methods for a real pharma model and interpret them.
- **L4** — Apply principled selection (stability, nested CV, domain-informed) to high-dimensional pharma data without leaking information.
- **L5** — Set the team's standards for feature engineering and reduction in pharma ML.

#### Resampling design & class imbalance
- **L1** — Recognise cross-validation, bootstrap, and class imbalance as concepts.
- **L2** — Run k-fold CV and a simple class-rebalancing step on a pharma model following an example.
- **L3** — Design appropriate resampling for a real pharma problem (grouped CV, stratified, time-aware) and address imbalance honestly.
- **L4** — Handle non-trivial resampling pitfalls — leakage, dependent samples, rare events — and choose calibration strategies.
- **L5** — Set the team's resampling and validation standards.

### Exploration

**Typical stack:** EDA tooling — `tidyverse`/`pandas`/`polars`, `ggplot2`/`plotly`, `skimr`/`pandas-profiling`/`ydata-profiling`; clustering and dimensionality reduction libraries (`uwot`, `umap-learn`, `scikit-learn`, `dbscan`); time-series tooling.

**Pharma examples:**
- A first-pass profiling report on a new real-world dataset that surfaces three blocking issues — *Profiling & quality @ L3*
- Reframing a stalled "predict adherence" project as a cohort-definition problem — *Problem framing @ L4*
- UMAP + clustering on a multi-omics cohort that suggests a novel sub-phenotype — *Clustering & proximity analyses @ L4; High-dimensional screening @ L4*

#### Profiling & quality
- **L1** — Recognise that EDA / profiling comes before modelling.
- **L2** — Generate a profiling report on a pharma dataset and read it.
- **L3** — Run a thorough profiling pass on a real pharma dataset and turn findings into analysis decisions.
- **L4** — Design profiling that catches subtle problems (drift, informative missingness, source-coding change).
- **L5** — Set the team's EDA standards and tooling.

#### Problem framing
- **L1** — Recognise that the framing of a question shapes the answer and the data needed.
- **L2** — Restate a pharma question in analytic terms (target, population, time horizon, outcome) following examples.
- **L3** — Frame a real pharma question into a tractable analysis with clear scope, exclusions, and metrics.
- **L4** — Reframe stuck or ill-posed pharma questions into ones that can be answered with the available evidence.
- **L5** — Coach the team on framing and shape how problems enter the pipeline.

#### Clustering & proximity analyses
- **L1** — Recognise clustering as a way to find structure in unlabelled pharma data.
- **L2** — Run k-means or hierarchical clustering on a pharma sample following an example.
- **L3** — Choose and apply appropriate clustering methods for real pharma data and validate the results.
- **L4** — Handle hard cases — high-dimensional, mixed-type, large-scale — with stable, interpretable clusters.
- **L5** — Lead clustering practice in the team or contribute methods.

#### Distributional statistical data analysis (EDA)
- **L1** — Recognise distributions, summary statistics, and the value of looking before testing.
- **L2** — Plot distributions and compute summaries on a pharma sample following an example.
- **L3** — Run distributional EDA on real pharma data and let it inform method choice.
- **L4** — Detect non-trivial distributional issues (mixture, heavy tails, regime change, censoring) and adapt analysis.
- **L5** — Set EDA standards in the team.

#### High-dimensional screening
- **L1** — Recognise the multiple-comparisons and dimensionality challenges in pharma omics and similar data.
- **L2** — Run a basic screen with multiple-comparison correction following an example.
- **L3** — Run a defensible high-dimensional screen on real pharma data with appropriate controls.
- **L4** — Apply principled high-dimensional methods (sparsity, knockoffs, FDR, stability selection) to pharma data.
- **L5** — Lead high-dimensional analytics practice or contribute methods.

#### Time-aware EDA
- **L1** — Recognise that time-indexed pharma data (vitals, claims, dosing, adverse events) needs time-aware EDA.
- **L2** — Plot time-series and rolling summaries for a small pharma sample.
- **L3** — Run time-aware EDA on real pharma data — seasonality, drift, gaps, censoring — and act on it.
- **L4** — Handle complex temporal pharma data (irregular sampling, multiple time scales, survival/longitudinal mixes).
- **L5** — Set the team's standards for temporal EDA.

#### Cohort & episode definition
- **L1** — Recognise that cohorts and episodes have to be explicitly defined; small definition changes can move results.
- **L2** — Apply an existing cohort/episode definition to a pharma dataset following an example.
- **L3** — Define a real pharma cohort or episode (inclusion/exclusion, index date, look-back, follow-up) and document trade-offs.
- **L4** — Handle non-trivial definitions (target trial emulation, competing exposures, multi-source consistency).
- **L5** — Set the team's cohort/episode standards and review process.

### Integration

**Typical stack:** ETL tooling (`dplyr`, `pandas`, `polars`, `dbt`); record linkage (`reclin2`, `recordlinkage`); ontology mapping (OHDSI / OMOP CDM, FHIR); provenance and lineage tooling.

**Pharma examples:**
- Linking a clinical trial dataset with insurance claims for follow-up outcomes — *Data integration & harmonisation @ L4; Provenance, lineage, & linkage @ L4*
- Mapping a study dataset to OMOP for cross-org analytics — *Standards & interoperability @ L4*
- Engineering pharma-specific features (washout windows, dose intensity, switching) for a model — *Feature engineering (domain specific) @ L3*

#### Data integration & harmonisation
- **L1** — Recognise that real pharma analyses usually combine sources that don't agree on definitions.
- **L2** — Join two small pharma datasets on a known key, checking row counts and unmatched records.
- **L3** — Integrate real pharma sources end-to-end with documented harmonisation choices and quality checks.
- **L4** — Lead harmonisation across messy multi-source pharma data with conflicting encodings, partial overlap, and quality issues.
- **L5** — Set the team's integration patterns.

#### Standards & interoperability
- **L1** — Recognise the main pharma standards (CDISC SDTM/ADaM, OMOP, FHIR, HL7, MedDRA) and what they cover.
- **L2** — Map a small pharma dataset to one standard following an example.
- **L3** — Apply standards correctly in a real pharma project (submission, common data model, partner exchange).
- **L4** — Lead a standards adoption or migration (e.g. a real OMOP migration of legacy studies) and engage with standards bodies.
- **L5** — Define the team's standards strategy.

#### Feature engineering (domain specific)
- **L1** — Recognise that pharma features (washout, dose intensity, treatment switching, time on therapy) need domain-aware construction.
- **L2** — Implement a small pharma feature following a worked example.
- **L3** — Engineer pharma-specific features for a real model with clear definitions, time-respect, and unit tests.
- **L4** — Design feature sets that survive deployment shifts and respect causal structure (no leakage, no future information).
- **L5** — Set the team's feature-engineering patterns and shared feature stores.

#### Provenance, lineage, & linkage
- **L1** — Recognise provenance and lineage as separate concerns from analysis logic.
- **L2** — Read a lineage diagram for an existing pharma pipeline.
- **L3** — Maintain provenance and lineage for a real pharma analysis end-to-end (raw → derived → results) and link records across sources.
- **L4** — Design lineage and linkage that meets regulatory expectations and survives data refreshes and retroactive corrections.
- **L5** — Set the team's lineage and linkage architecture.

### Mining

**Typical stack:** classic mining (`arules`, `mlxtend`); NLP (`spaCy`, `udpipe`, `tidytext`, transformers); graph analytics (`igraph`, `networkx`, `tidygraph`); time-series and process mining (`prophet`, `tsfeatures`, `pm4py`).

**Pharma examples:**
- Mining adverse-event term co-occurrence in spontaneous reports — *Pattern/association rule mining @ L3*
- Information extraction from oncology pathology reports — *Text mining (NLP) & information extraction @ L4*
- Treatment-pathway analysis from claims using process mining — *Time-series & process mining @ L4*

#### Sources identification
- **L1** — Recognise the main mineable pharma sources (EHR, claims, registries, literature, social media, sensor streams).
- **L2** — Describe a single pharma source: structure, biases, access route.
- **L3** — Identify and qualify the right mining sources for a real pharma question.
- **L4** — Combine multiple sources into a defensible mining design with awareness of biases and gaps.
- **L5** — Set the team's source-identification practice.

#### Pattern/association rule mining
- **L1** — Recognise association rules and itemset / co-occurrence mining.
- **L2** — Run a small `arules`/`mlxtend` analysis on a pharma sample following an example.
- **L3** — Apply association mining to a real pharma question (co-prescribing, AE co-occurrence) with appropriate filters and interpretation.
- **L4** — Handle non-trivial mining (rare events, hierarchical items, statistical correction) on real pharma data.
- **L5** — — *(further mastery folds into broader Mining or Modelling competencies)*

#### Text mining (NLP) & information extraction
- **L1** — Recognise NLP tasks relevant to pharma: classification, NER, normalisation to ontologies.
- **L2** — Run a basic NLP pipeline (tokenisation, NER) on pharma text following an example.
- **L3** — Apply NLP to a real pharma question (extracting outcomes, adverse events, eligibility from clinical text) with evaluation.
- **L4** — Handle hard pharma NLP — domain adaptation, noisy text, multilingual data, weak supervision, LLM-assisted extraction with validation.
- **L5** — Lead pharma NLP practice or contribute methods.

#### Graph/network-based mining
- **L1** — Recognise graphs / networks (drug–target, co-prescription, citation) as a mining substrate.
- **L2** — Build and visualise a small pharma graph following an example.
- **L3** — Run graph algorithms (centrality, community detection) on real pharma networks and interpret results.
- **L4** — Apply advanced graph methods (graph ML, link prediction) to real pharma problems with careful evaluation.
- **L5** — Lead graph-analytics practice in the team.

#### Time-series & process mining
- **L1** — Recognise time-series forecasting and process mining as distinct disciplines.
- **L2** — Fit a basic time-series model or run a simple process-mining tool on pharma data following an example.
- **L3** — Apply time-series or process mining to a real pharma question (treatment pathways, adverse-event trends, sensor signals).
- **L4** — Handle hard cases — irregular sampling, regime change, multiple time scales, complex pathways — defensibly.
- **L5** — Set the team's standards for temporal and process analytics.

---

## ML & AI

### ML & AI Foundations

**Typical stack:** `scikit-learn`, `tidymodels`, `xgboost`/`lightgbm`/`catboost`, PyTorch / Keras / `torch` for R; `mlflow` / `wandb` for tracking; standard reinforcement-learning toolkits where relevant.

**Pharma examples:**
- A supervised model predicting 30-day readmission, with proper evaluation — *Supervised learning @ L3*
- Discovering subtypes in a pooled biomarker dataset — *Unsupervised learning @ L4*
- A deep model for medical image segmentation in pathology — *Deep Learning @ L4*

#### ML algorithms
- **L1** — Recognise the major algorithm families: linear/logistic, tree-based, kernel methods, neural nets, clustering.
- **L2** — Train a default `scikit-learn` / `tidymodels` model on a pharma sample following an example.
- **L3** — Choose and tune an appropriate algorithm for a real pharma problem with honest evaluation.
- **L4** — Choose between algorithms on real pharma data based on data shape, interpretability, regulation, and deployment constraints.
- **L5** — Set the team's algorithm patterns and contribute to methods.

#### AI versus ML
- **L1** — Distinguish AI, ML, statistics, and rule-based systems at a high level.
- **L2** — Place a given pharma tool in the right bucket and explain why.
- **L3** — Communicate the distinction clearly to non-technical pharma stakeholders and use it to set realistic expectations.
- **L4** — — *(skill is conceptual; further mastery shows up in other ML/AI competencies)*
- **L5** — —

#### Supervised learning
- **L1** — Recognise classification and regression as supervised tasks; recognise train/validation/test splits.
- **L2** — Train and evaluate a basic classifier or regressor on a pharma sample following an example.
- **L3** — Build a real supervised pharma model end-to-end with appropriate evaluation, calibration, and reporting.
- **L4** — Handle hard supervised cases (rare outcomes, censoring, label noise, distribution shift) on real pharma data.
- **L5** — Set the team's standards for supervised pharma modelling.

#### Unsupervised learning
- **L1** — Recognise unsupervised tasks (clustering, density estimation, anomaly detection, dimensionality reduction).
- **L2** — Run a basic unsupervised method on a pharma sample following an example.
- **L3** — Apply unsupervised methods to a real pharma question and validate the results sensibly.
- **L4** — Handle complex unsupervised problems on real pharma data (mixed types, high dimensions, weak labels).
- **L5** — Lead unsupervised-methods practice in the team.

#### Deep Learning
- **L1** — Recognise deep learning and the main architectures (CNNs, transformers, RNNs).
- **L2** — Train a small model in PyTorch / Keras on a pharma sample following an example.
- **L3** — Build a real deep model for a pharma task (imaging, sequence, signal) with appropriate evaluation.
- **L4** — Handle hard deep-learning cases on pharma data — domain shift, limited labels, regulation, validation — credibly.
- **L5** — Lead deep-learning practice in the team or contribute methods.

#### Reinforcement learning
- **L1** — Recognise RL and where it might apply in pharma (adaptive trials, dynamic treatment regimes, dosing).
- **L2** — Read a published pharma RL example and explain its setup.
- **L3** — Apply RL to a tractable pharma simulation problem (e.g. dosing optimisation in silico) with honest evaluation.
- **L4** — Lead an RL pharma application with proper safety, evaluation, and translational thinking.
- **L5** — — *(rare; folds into research / methods leadership)*

### Model Building & Assessment

**Typical stack:** explainability and interpretation tooling (`shap`, `lime`, `iml`, `tidymodels` parsnip + workflows); robust evaluation harnesses; uncertainty quantification (`conformalInference`, Bayesian tooling); optimisation theory awareness.

**Pharma examples:**
- A SHAP analysis that reveals a model relying on a leaky proxy variable — *Model interpretation @ L4; Challenges for machine learning @ L4*
- A sensitivity analysis varying preprocessing choices to test robustness — *Model assessment and sensitivity analysis @ L4*
- A held-out external-site evaluation that decides whether to deploy — *Importance of robust evaluation @ L4*

#### Model interpretation
- **L1** — Recognise that model behaviour can and should be inspected, not taken on trust.
- **L2** — Run a SHAP/LIME / variable-importance analysis on a small pharma model following an example.
- **L3** — Interpret a real pharma model with appropriate methods and explain it to stakeholders honestly.
- **L4** — Use interpretation to spot real problems (leakage, spurious features, subgroup failure) and act on them.
- **L5** — Set the team's interpretation practice for pharma ML.

#### Model assessment and sensitivity analysis
- **L1** — Recognise that single point-estimates of performance hide a lot.
- **L2** — Run a basic sensitivity check (e.g. swap a hyperparameter) on a pharma model following an example.
- **L3** — Build assessment and sensitivity analysis into real pharma modelling: bootstrap, subgroup, design choices.
- **L4** — Stress-test pharma models systematically (data quirks, design choices, distribution shift) and report defensibly.
- **L5** — Set the team's assessment and sensitivity standards.

#### Importance of robust evaluation
- **L1** — Recognise that evaluation choices can swing conclusions and that robust evaluation is non-negotiable in pharma.
- **L2** — Apply a robust evaluation template (held-out, CV, calibration, subgroup) to a small pharma model.
- **L3** — Design robust evaluation for a real pharma model and report it transparently.
- **L4** — Handle non-trivial evaluation contexts (external sites, prospective use, regulatory expectations) credibly.
- **L5** — Set the team's evaluation standards.

#### Challenges for machine learning
- **L1** — Recognise common ML failure modes — overfitting, leakage, distribution shift, label noise, bias.
- **L2** — Spot one of these failure modes in a pharma example following a checklist.
- **L3** — Diagnose and mitigate these failure modes in real pharma models.
- **L4** — Anticipate failure modes from project design and instrument for them ahead of time.
- **L5** — Set the team's defensive ML practices for pharma.

#### Learning algorithms as principled optimization approaches
- **L1** — Recognise that ML algorithms are usually solving an optimisation problem with assumptions and trade-offs.
- **L2** — Read a loss function and explain what it is optimising on a pharma example.
- **L3** — Choose and modify loss functions / regularisers appropriately for a real pharma problem.
- **L4** — Reason about optimisation behaviour in pharma ML (convergence, identifiability, conditioning) and act on it.
- **L5** — Contribute methods or set the team's principled-optimisation practice.

### Use of AI in Education & Research

**Typical stack:** general-purpose LLMs (Claude, GPT-class) and coding assistants; retrieval-augmented setups for pharma corpora; evaluation tooling for AI outputs; internal usage policies.

**Pharma examples:**
- Drafting an analysis plan with an LLM and editing it with a sceptical reviewer's eye — *Efficient prompting @ L3; What can AI be used for? What can it not be used for? @ L3*
- Recognising and correcting LLM hallucinations in a literature summary — *Common misconceptions about generative AI @ L3*
- An internal policy that distinguishes safe and unsafe LLM use cases for pharma work — *What can AI be used for? What can it not be used for? @ L5*

#### What can AI be used for? What can it not be used for?
- **L1** — Recognise the general capabilities and limits of current AI (LLMs and others) at a high level.
- **L2** — Place a candidate pharma use case on a "good fit / poor fit / unsafe" map following examples.
- **L3** — Decide AI use case-by-case in real pharma work, with clear rationale and guardrails.
- **L4** — Lead AI strategy for a pharma team, balancing value, safety, and regulation.
- **L5** — Define organisational policy and engage externally on responsible AI use in pharma.

#### Efficient prompting
- **L1** — Recognise that prompting affects output quality.
- **L2** — Use a simple prompting template (role, task, constraints, examples) on a pharma task following an example.
- **L3** — Routinely produce useful pharma outputs with LLMs through structured prompting, retrieval, and verification.
- **L4** — Engineer prompts and small workflows that survive deployment in pharma settings (evaluation, guardrails, retrieval grounding).
- **L5** — Set the team's prompting and AI-workflow patterns.

#### Common misconceptions about generative AI
- **L1** — Recognise common misconceptions: that LLMs "know" things, that fluent text means correct text, that bigger model means safer model.
- **L2** — Spot a misconception in a pharma example following a checklist.
- **L3** — Routinely correct misconceptions in pharma colleagues' use of generative AI.
- **L4** — Help non-technical pharma audiences calibrate their trust in generative AI in their actual workflows.
- **L5** — Lead the team's communication and education on generative-AI realities.

---

## Mathematics & Statistics

### Mathematics

**Typical stack:** pen-and-paper / whiteboard; `numpy`/`scipy.linalg`, `sympy`, R `Matrix`; optimisation libraries (`optim`, `scipy.optimize`, `cvxpy`).

**Pharma examples:**
- Reasoning about why a gradient-based optimiser fails to converge on a particular PK model — *Multivariate calculus @ L4; Optimization @ L4*
- Hand-deriving the linear-algebra structure behind a PCA on omics data — *Advanced linear algebra @ L4*
- Setting up a constrained optimisation for a dosing-decision problem — *Optimization @ L3*

#### Set theory and basic logic
- **L1** — Recognise basic set operations and Boolean logic.
- **L2** — Apply them to filter / combine pharma datasets following examples.
- **L3** — Reason fluently about sets, logic, and conditions when defining cohorts, exclusions, and rules.
- **L4** — — *(further mastery shows up in cohort definition and data-engineering competencies)*
- **L5** — —

#### Quantitative reasoning
- **L1** — Recognise basic quantitative concepts (rates, proportions, percentages, units, magnitudes).
- **L2** — Compute and sense-check basic quantities for a pharma dataset.
- **L3** — Reason quantitatively about real pharma data — sanity-check numbers, spot magnitude errors, communicate clearly.
- **L4** — Build quantitative intuition for non-trivial pharma problems (rates, exposures, hazards, costs).
- **L5** — Coach the team on quantitative thinking.

#### Basic calculus and linear algebra plus matrices
- **L1** — Recognise vectors, matrices, derivatives, and integrals as objects.
- **L2** — Compute basic operations (matrix multiply, derivative of a polynomial) following examples.
- **L3** — Apply basic linear algebra and calculus comfortably to pharma analytics (regression, transformations, gradients).
- **L4** — — *(progresses into Multivariate calculus, Advanced linear algebra)*
- **L5** — —

#### Basic differentiation and integration
- **L1** — Recognise differentiation and integration as concepts.
- **L2** — Compute simple derivatives and integrals following examples.
- **L3** — Apply basic differentiation and integration where they show up in pharma analyses (rate calculations, AUC).
- **L4** — — *(progresses into Multivariate calculus)*
- **L5** — —

#### Partial derivatives
- **L1** — Recognise partial derivatives and gradients.
- **L2** — Compute partial derivatives of small functions following examples.
- **L3** — Use partial derivatives in pharma analyses — gradient-based fitting, sensitivity, marginal effects.
- **L4** — Reason about gradient behaviour in non-trivial pharma models (identifiability, conditioning).
- **L5** — — *(rare; subsumed by Optimization / Multivariate calculus mastery)*

#### Multivariate calculus
- **L1** — Recognise multivariate calculus concepts (Jacobians, Hessians, chain rule).
- **L2** — Apply them to small problems following examples.
- **L3** — Use multivariate calculus where pharma modelling needs it (gradient methods, delta method, sensitivity).
- **L4** — Diagnose and fix optimisation/inference issues in pharma models that come from calculus structure.
- **L5** — Contribute methods or coach the team on multivariate methods.

#### Advanced linear algebra
- **L1** — Recognise advanced concepts (eigendecomposition, SVD, projections, pseudo-inverses).
- **L2** — Apply them in small pharma problems following examples.
- **L3** — Use them confidently in pharma analyses (PCA, latent models, regularisation).
- **L4** — Reason about numerical conditioning and stability for real pharma matrices (ill-conditioned designs, sparse covariates).
- **L5** — Contribute methods or coach the team.

#### Optimization
- **L1** — Recognise optimisation problems (objective, constraints, variables) and standard solvers.
- **L2** — Solve a small constrained / unconstrained problem with `scipy.optimize` or R `optim` following examples.
- **L3** — Formulate and solve real pharma optimisation problems (dose finding, design optimisation, model fitting).
- **L4** — Choose between solvers and formulations for hard pharma optimisation; diagnose convergence issues; handle non-convexity.
- **L5** — Contribute methods or coach the team on pharma optimisation.

### Statistical thinking

**Typical stack:** the same R/Python statistical stack as Statistics; the differentiator is mindset and habits (study design, uncertainty, falsifiability).

**Pharma examples:**
- Reframing a "how big is X?" pharma question into a falsifiable, prespecified analysis — *Statistical thinking @ L3*
- Coaching a junior on the difference between "the data says" and "the model says" — *Statistical thinking @ L4*

#### Statistical thinking
- **L1** — Recognise statistical thinking as a habit (think about variability, design, and uncertainty before computing).
- **L2** — Apply a basic checklist (population, sample, design, uncertainty) to a pharma question.
- **L3** — Routinely think statistically about real pharma problems — what could vary, what's prespecified, what's exploratory.
- **L4** — Coach others to think statistically and shape pharma project design accordingly.
- **L5** — Embody and propagate statistical thinking as a culture in the team or org.

### Statistics

**Typical stack:** R (`stats`, `tidymodels`, `survival`, `lme4`, `brms`, `rstanarm`), Python (`statsmodels`, `pingouin`, `pymc`); design-of-experiments tooling.

**Pharma examples:**
- A descriptive table that meets ICH E9 expectations for a CSR — *Descriptive statistics @ L3*
- A prespecified hypothesis test for a primary trial endpoint with multiplicity adjustment — *Hypothesis testing @ L3*
- A mixed-effects model with sensible random structure for repeated measures — *Statistical modeling (incl. regression) and model assessment @ L4*
- A factorial DOE for a process-development study with proper randomisation — *Design of experiments (DOE)... @ L4*

#### Descriptive statistics
- **L1** — Recognise mean, median, variance, quantiles, frequency tables, and when each is appropriate.
- **L2** — Produce a basic descriptive table for a pharma dataset following a template.
- **L3** — Produce regulatory-grade descriptive summaries (Table 1, baseline characteristics, AE summaries) for real pharma data.
- **L4** — Tailor descriptive analysis to the audience and decision; spot non-trivial issues hiding in summary statistics.
- **L5** — — *(further mastery folds into other Statistics competencies)*

#### Variability, uncertainty, sampling error, and inference
- **L1** — Recognise variability and sampling error as distinct from systematic error.
- **L2** — Compute and report SEs and CIs on a small pharma sample following examples.
- **L3** — Quantify and communicate uncertainty in real pharma analyses appropriately.
- **L4** — Handle non-trivial uncertainty (clustered, time-varying, hierarchical, Bayesian).
- **L5** — Set the team's standards for reporting uncertainty.

#### Basic probability theory and randomness
- **L1** — Recognise probability concepts: events, conditional probability, independence, distributions.
- **L2** — Compute basic probabilities and simulate random draws following examples.
- **L3** — Apply probability reasoning fluently to pharma analyses (risk, hazard, predictive distributions).
- **L4** — Reason about non-trivial probability structures in pharma data (joint, hierarchical, censored).
- **L5** — Contribute methods or coach the team.

#### Hypothesis testing
- **L1** — Recognise null/alternative hypotheses, type I/II error, p-values, confidence intervals.
- **L2** — Run a basic test (t, χ², simple regression) on a pharma sample following an example.
- **L3** — Choose and interpret hypothesis tests honestly for real pharma questions (effect sizes, CIs, multiplicity).
- **L4** — Handle non-trivial pharma testing (group sequential, multiple endpoints, non-inferiority, Bayesian).
- **L5** — Set the team's standards for hypothesis testing.

#### Statistical modeling (incl. regression) and model assessment
- **L1** — Recognise regression and modelling as a way to relate variables under uncertainty.
- **L2** — Fit a linear/logistic regression on a pharma sample following an example.
- **L3** — Build and assess real pharma models (GLM, mixed-effects, GAM, survival) with appropriate diagnostics.
- **L4** — Handle non-trivial modelling — hierarchical, longitudinal, joint, missing-data — with credible assumptions and assessment.
- **L5** — Set the team's modelling standards or contribute to methods.

#### Design of experiments (DOE). Nonsampling error, biases, confounding, and causal inference
- **L1** — Recognise the difference between sampling and non-sampling error; recognise confounding and bias as concepts.
- **L2** — Read a DOE / RCT design and explain its logic.
- **L3** — Apply DOE principles and standard bias/confounding adjustments to real pharma analyses.
- **L4** — Lead complex pharma study design — adaptive trials, factorial DOE, target trial emulation — and reason rigorously about non-sampling error.
- **L5** — Set the team's design standards or contribute methods.

---

## Visualization & Presentation

### Creating Data Visualization

**Typical stack:** R `ggplot2`, `plotly`, `gt`/`gtsummary`; Python `matplotlib`, `seaborn`, `altair`, `plotly`; design tools (Figma) at higher levels; accessibility checks.

**Pharma examples:**
- A pre-trial figure mockup that forces clarification of the primary outcome — *Doing data visualization @ L3*
- A survival KM plot with risk table that meets journal expectations — *Doing data visualization @ L3*
- A team style guide for pharma figures (palette, typography, accessibility) — *Critiqueing data visualization @ L4; Doing data visualization @ L5*

#### Evaluation of data visualization
- **L1** — Recognise good and bad practice in pharma figures (axis abuse, misleading scales, chart-junk, accessibility issues).
- **L2** — Apply an evaluation checklist to an existing pharma figure.
- **L3** — Evaluate pharma figures critically against purpose, audience, and standards.
- **L4** — Lead figure review for a pharma project or publication, with substantive feedback.
- **L5** — Set the team's evaluation standards.

#### Critiqueing data visualization
- **L1** — Recognise that critique is a craft, not just opinion.
- **L2** — Give structured critique on a pharma figure following a template.
- **L3** — Provide actionable critique on real pharma figures, balancing form and message.
- **L4** — Coach others to critique well; resolve disagreements between figure authors and stakeholders.
- **L5** — Set the team's critique culture.

#### Doing data visualization
- **L1** — Recognise the basic chart types and when each is appropriate.
- **L2** — Make a competent pharma chart (KM curve, forest plot, waterfall) using `ggplot2` / `matplotlib` following an example.
- **L3** — Produce publication- or report-grade pharma figures end-to-end with appropriate annotations and uncertainty.
- **L4** — Design figure systems for non-trivial pharma communication (style guide, interactive dashboards, accessibility).
- **L5** — Set the team's visualisation standards or contribute open-source tooling.

### Data-Informed Decision Making

**Typical stack:** decision-analysis frameworks (expected value, decision trees, value-of-information); dashboarding (`shiny`, `streamlit`, `dash`); structured pre-mortems / decision logs.

**Pharma examples:**
- Reducing a noisy dashboard to the three numbers that drive a go/no-go decision — *Prioriting information garnered from data @ L3*
- A decision memo that turns a complex evidence set into a recommendation with explicit uncertainty — *Converting data into actionable information @ L4*
- Comparing trial-design options on expected value, risk, and timeline — *Weighing the merit and impacts of possible solutions/decisions @ L4*

#### Prioriting information garnered from data
- **L1** — Recognise that not all data points are decision-relevant.
- **L2** — Filter a pharma dashboard down to the few KPIs that actually inform the decision following a template.
- **L3** — Decide what to surface and what to hide for real pharma decisions, and justify it.
- **L4** — Design information architecture for non-trivial pharma decision processes (governance committees, regulators, leadership).
- **L5** — Set the team's standards for decision-relevant reporting.

#### Converting data into actionable information
- **L1** — Recognise that "data" and "actionable information" are not the same thing.
- **L2** — Translate a pharma analysis into a recommendation following a template.
- **L3** — Produce decision memos / recommendations from real pharma analyses with explicit assumptions and uncertainty.
- **L4** — Translate complex pharma evidence (mixed quality, conflicting sources) into a defensible recommendation.
- **L5** — Set the team's standards for evidence-to-action work.

#### Weighing the merit and impacts of possible solutions/decisions
- **L1** — Recognise that pharma decisions involve trade-offs (efficacy, safety, cost, time, IP, regulatory).
- **L2** — List trade-offs for a pharma decision following a template.
- **L3** — Run a structured comparison of options for a real pharma decision (decision tree, expected value, sensitivity).
- **L4** — Lead complex pharma decision analyses with cross-functional input and explicit value of information.
- **L5** — Set the team's decision-analysis practice.

### Interpreting Data Visualizations

**Typical stack:** the consumer side of the same R/Python visualisation libraries; literacy frameworks (e.g. ASA, ICH-aligned reporting standards).

**Pharma examples:**
- Spotting that a forest plot's apparent treatment effect is driven by one small subgroup — *Interpretation of data from one data visualisation @ L3*
- Reconciling a clinical-trial figure with a real-world analysis that disagrees — *Integration of data from data visualisation(s) with other data @ L4; Identification of discrepancies within data @ L4*

#### Interpretation of data from one data visualisation
- **L1** — Recognise the elements of a chart (axes, units, sample size, uncertainty).
- **L2** — Read a basic pharma chart and state what it does and doesn't show.
- **L3** — Interpret real pharma figures correctly, including uncertainty and limitations.
- **L4** — Spot non-obvious issues in pharma figures (selection effects, axis abuse, hidden subgroup heterogeneity).
- **L5** — Coach the team on critical reading.

#### Integration of data from data visualisation(s) with other data
- **L1** — Recognise that figures are one input among many in a pharma decision.
- **L2** — Combine a chart with one other piece of evidence to reach a small conclusion following an example.
- **L3** — Integrate evidence across multiple pharma figures and other data sources for real decisions.
- **L4** — Reconcile conflicting figures and data sources in a defensible way.
- **L5** — Set the team's evidence-integration practice.

#### Identification of discrepancies within data
- **L1** — Recognise that figures and data summaries sometimes disagree, and that this is a signal.
- **L2** — Spot a discrepancy between two pharma views following an example.
- **L3** — Investigate and explain discrepancies in real pharma data (definitions, time windows, exclusions).
- **L4** — Resolve hard discrepancies that involve multiple sources, definitions, or analysts.
- **L5** — Set the team's standards for discrepancy investigation.

### Presenting Data Visualization

**Typical stack:** Quarto / R Markdown / Reveal.js / PowerPoint / Keynote; storyboarding; accessibility tooling; audience-research basics.

**Pharma examples:**
- Reworking a slide for a regulator vs. a board audience without changing the underlying data — *Audience needs @ L3*
- A 30-second narrative that lands a complex pharma analysis with a non-technical executive — *Data communication @ L4*

#### Intended outcome identification and selection
- **L1** — Recognise that every pharma figure has an intended outcome (decision, persuasion, exploration, record).
- **L2** — State the intended outcome for a pharma figure following a template.
- **L3** — Choose the right figure and framing for a real pharma communication based on intended outcome.
- **L4** — Adapt outcome-driven figure choice across complex pharma communications (regulatory, scientific, executive).
- **L5** — Set the team's standards for purpose-driven visualisation.

#### Audience needs
- **L1** — Recognise that pharma audiences differ (clinicians, statisticians, regulators, executives, patients).
- **L2** — Adapt a pharma figure for a different audience following examples.
- **L3** — Tailor real pharma figures to specific audiences without distorting the message.
- **L4** — Communicate the same pharma evidence credibly across radically different audiences.
- **L5** — Coach the team on audience-aware communication.

#### Data communication
- **L1** — Recognise that good data communication is a craft of its own.
- **L2** — Present a small pharma analysis using a clear narrative arc following a template.
- **L3** — Communicate real pharma analyses clearly and honestly to mixed audiences in writing and speech.
- **L4** — Land complex pharma evidence in high-stakes settings (regulators, leadership, public).
- **L5** — Set the team's communication standards and coach others.

### Visualization Literacy

**Typical stack:** basic chart-grammar references (Wilkinson / Wickham); accessibility (color, contrast, alt-text); cognitive-load awareness.

**Pharma examples:**
- Catching that a colour palette in a pharma poster fails for colour-blind reviewers — *Visualization Literacy @ L3*
- Helping a clinical colleague choose a chart type that matches the question — *Visualization Literacy @ L3*

#### Visualization Literacy
- **L1** — Recognise standard chart types and the basic grammar of graphics.
- **L2** — Match common pharma data shapes to appropriate chart types following examples.
- **L3** — Apply visualisation literacy in real pharma work — chart choice, colour, accessibility, honesty.
- **L4** — Spot and correct subtle literacy issues across a pharma project's figures.
- **L5** — Coach the team and set literacy standards.
