# CPDSE Service Workflow — Prompt Document
# Service: Research & DS Strategy (①)
# Pipeline Step: 2 — DS Landscape Analysis
# Version: v0.1.0 (AI-drafted, pending expert review)
# Author: AI draft / MO review
# Notes: Initial draft — not yet tested on a real engagement.
---

## PURPOSE

Map the group's work to the pharma value chain, then characterise the DS
landscape for their relevant stages — what established methods and tools
comparable groups use, and what is emerging. Flag anything that sits outside
the CPDSE competency model ([OUTSIDE MODEL]) or beyond the reference document
([BEYOND REFERENCE]). This output feeds into Step 3 (Gap Assessment).

---

## INPUTS

### Input 1 — Step 1 Output (Group Profile)
The full structured markdown output from Pipeline Step 1. Pay particular
attention to:
- ## Research Domain & Questions (value chain mapping)
- ## Current DS Tools & Methods
- ## Data Types & Sources

### Input 2 — Pharma Value Chain Reference Document
The current version of pharma-value-chain-reference.md. This document defines
the CPDSE-recognised methods and tools for each pipeline stage. Treat it as
the baseline — anything not in it should be flagged [BEYOND REFERENCE].

---

## ANALYTICAL FRAME

### Value chain mapping
Map the group's work to one or more of the following stages. Assign a
PRIMARY stage and, if applicable, SECONDARY stages. Justify the mapping
in 2-3 sentences. If the work spans stages or does not fit cleanly, note
this explicitly — do not force a mapping.

Standard stages: Target Identification | Target Validation | Hit Identification |
Lead Identification | Lead Optimisation | Candidate Selection | Preclinical |
Clinical Pharmacology | Phase I | Phase II | Phase III | Regulatory |
Manufacturing | Market Access | Pharmacoepidemiology | Biomarker Development

### Open landscape first
Before mapping to the CPDSE competency model, characterise what comparable
groups do in the relevant stages WITHOUT reference to the model. Use the
pharma value chain reference document and your domain knowledge. This produces
an honest landscape that the model can then be mapped onto — rather than
forcing the landscape into the model's categories.

### Competency model mapping
After the open landscape, map specific methods and tools to the seven CPDSE
competency sub-areas:
- Data Management & Organisation
- Statistical Analysis
- ML / Predictive Modelling
- Bioinformatics / Cheminformatics
- Data Visualisation
- Reproducible Research
- Scientific Programming

Flag explicitly:
- [OUTSIDE MODEL] — work that does not map to any sub-area
- [BEYOND REFERENCE] — methods/tools not in the pharma-value-chain-reference.md

---

## OUTPUT FORMAT

Produce output as structured markdown with the exact sections below.

## Value Chain Mapping
[Primary stage, secondary stages, mapping rationale, mapping confidence level]

## DS Landscape — [Primary Stage]
### Established Methods & Tools
[Paragraph: what comparable groups use. Source from reference doc and domain
knowledge. Do not evaluate the client group here.]
### Emerging Practices
[Bullet list: what is increasingly used but not yet standard. Flag as horizon
items for Step 4.]

## DS Landscape — [Secondary Stage(s)]
[Same structure. One section per secondary stage.]

## Competency Model Map
[Bullet list: specific method/tool → competency sub-area. Include [OUTSIDE MODEL]
and [BEYOND REFERENCE] flags where applicable.]

## Landscape Gaps and Caveats
[Bullet list: where the reference document is insufficient for this group's
specific domain. Each [DATA GAP] from Step 1 that affects the landscape
analysis. [BEYOND REFERENCE] and [OUTSIDE MODEL] items with brief notes on
their significance for the CPDSE model.]

---

## CONSTRAINTS

The model MUST NOT:

1. Skip the open landscape step — always characterise the landscape before
   mapping to the CPDSE model.
2. Force everything into the seven CPDSE sub-areas — [OUTSIDE MODEL] flags
   are important outputs, not failures.
3. Treat [BEYOND REFERENCE] as a gap for the client group — it may simply
   mean the reference document needs updating.
4. Make gap judgements about the client group — those belong in Step 3.
5. Invent landscape content not grounded in the reference document or domain
   knowledge.

---

## PROMPT ASSEMBLY INSTRUCTIONS

[SYSTEM]
You are a pharmaceutical data science expert supporting the CPDSE
(Centre for Pharmaceutical Data Science Education) service pipeline.
Your task is to map a research group's work to the pharma value chain
and characterise the DS landscape for their relevant stages. Use the
pharma value chain reference document as the baseline. Flag [BEYOND REFERENCE]
for anything not in it. Flag [OUTSIDE MODEL] for anything that does not map
to the seven CPDSE competency sub-areas. Do not make gap judgements.
Follow the output format exactly.

[USER]
## Group Profile (Step 1 Output)
{paste full Step 1 output here}

## Pharma Value Chain Reference
{paste current pharma-value-chain-reference.md here}

## Task
Produce the DS Landscape Analysis following the analytical frame and output
format specified. Begin with ## Value Chain Mapping.
