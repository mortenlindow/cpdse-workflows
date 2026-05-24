# CPDSE Service Workflows
Version: v0.2.0 | Last updated: 2026-05-24

## Structure

```
cpdse-service-workflows/
  README.md                            ← this file
  CLAUDE.md                            ← working notes / design decisions
  TODO.md                              ← near-term open items
  engagement-log.md                    ← all engagements, model + prompt versions
  services/
    01-research-strategy/
      intake-questionnaire-blank-v0.2.0.txt
      prompts/
        01-group-profile-synthesis.md  ← Step 1 prompt
        02-ds-landscape-analysis.md    ← Step 2 prompt
        03-gap-assessment.md           ← Step 3 prompt
        04-recommendation-synthesis.md ← Step 4 prompt
      output-templates/
        workshop1-miro-frames.pdf      ← 4-frame PDF for Miro import
        workshop1-facilitation-guide.docx ← consultant session script
  reference/
    README.md                          ← how the 3 models relate + build services
    competency-model/                  ← PDS Competence Model
    pharma-value-chain-model/          ← Pharma Value Chain Model
    pedagogic-practices/               ← Pedagogic Practices (Training from the Back of the Room)
    competency-model-migration-crosswalk.md
  engagements/
    ENG001-MortenLindow/
      intake-questionnaire-ENG001-SIM.txt
      step3-gap-assessment-ENG001-SIM.md
      step4-recommendation-synthesis-ENG001-SIM.md
      strategy-brief-ENG001-SIM.docx  ← client-facing brief
```

## Reference models

Every engagement, whatever the customer trigger, is grounded in three
**reference models** (in `reference/`). Each answers a different question:

| Model | Answers | Summary |
|---|---|---|
| **Pharma Value Chain Model** | **Where** in the drug pipeline? | 2-tier linear: Pre-clinical → Clinical development → On-market → 13 substeps |
| **PDS Competence Model** | **What** data-science capabilities? | 7 domains → 30 sub-areas → ~123 competencies, rated L1–L5 |
| **Pedagogic Practices** | **How** do we build them? | Sharon L. Bowman's 4Cs + Six Trumps |

**Principles:**

- **Each model is self-sufficient** — its doc describes only itself and does
  **not** cross-reference the other models.
- **Relationships live in one place.** How the models relate (*Where × What ×
  How*) and how they compose into service workflows is described in
  [`reference/README.md`](reference/README.md). Cross-model intersections (e.g. a
  stage → competency map) belong there or in the service workflow — never
  hard-coded into an individual model.
- **Independent versioning.** Each model versions on its own `Version:` header +
  changelog; the engagement-log records which version each engagement ran under.

## Pipeline (Service ①)

```
Passive material collection (~1h)
→ Questionnaire sent to client (async, ~30min for client)
→ Meeting 1: walkthrough + amendment (~1h)
→ Step 1: Group Profile Synthesis (AI, ~5min)
→ Step 2: DS Landscape Analysis (AI, ~5min)
→ Step 3: Gap Assessment (AI, ~5min)
→ Step 4: Recommendation Synthesis (AI, ~5min)
→ Consultant QA (~1h)
→ Workshop 1: present findings, align, commit (~2h)
→ Refinement + final report (~1h)
→ Workshop 2: deliver final report + roadmap (~1.5h)
→ Closure document
Total consultant time: ~7-8h per engagement
```

Service ① (Research & DS Strategy) is the only fully designed service. Services
②/③ (specific research consulting, course upgrade, staff focus areas) reuse the
same three reference models — see [`reference/README.md`](reference/README.md).

## Prompt versioning

All prompt documents are versioned independently. When updating a prompt,
increment the version number and log it in engagement-log.md.
The engagement log maps each engagement to the model + prompt versions used,
ensuring reproducibility.

## Status

All three reference models exist (`reference/`). All prompt documents are v0.1.0
AI-drafted, pending expert review before the first real engagement. ENG001-SIM is
a simulated test engagement only. See [`TODO.md`](TODO.md) for near-term work.
