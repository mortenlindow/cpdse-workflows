# CPDSE Service Workflows
Version: v0.3.0 | Last updated: 2026-05-24

## Positioning

> "Pharma is full of data. But not of data science. We are here to change that."

**Methodology:** To improve capabilities in **PharmaValueChain** we train and
catalyse **Data Science Competencies** using **Training From the Back of the
Room** practices. (The verbal compression of the three reference models below.)

## Structure

```
cpdse-service-workflows/
  README.md                            ← this file
  CLAUDE.md                            ← working notes / design decisions
  TODO.md                              ← near-term open items
  engagement-log.md                    ← all engagements, model + prompt versions
  services/
    README.md                          ← the 3 customer-facing workflow types
    01-research-strategy/              ← Research type — built workflow
      intake-questionnaire-blank-v0.2.0.txt
      prompts/
        01-group-profile-synthesis.md  ← Step 1 prompt
        02-ds-landscape-analysis.md    ← Step 2 prompt
        03-gap-assessment.md           ← Step 3 prompt
        04-recommendation-synthesis.md ← Step 4 prompt
      output-templates/
        workshop1-miro-frames.pdf      ← 4-frame PDF for Miro import
        workshop1-facilitation-guide.docx ← consultant session script
    educational/                       ← Educational type (stub)
    internal/                          ← Internal self-improvement (stub)
  reference/
    README.md                          ← how the 3 models relate + build services
    competency-model/                  ← PDS Competence Model
    pharma-value-chain-model/          ← Pharma Value Chain Model
    pedagogic-practices/               ← Pedagogic Practices (Training from the Back of the Room)
    competency-model-migration-crosswalk.md
    value streams - DRAFT.pdf          ← source Miro board export (2026-04-26)
  engagements/
    ENG001-MortenLindow/
      intake-questionnaire-ENG001-SIM.txt
      step3-gap-assessment-ENG001-SIM.md
      step4-recommendation-synthesis-ENG001-SIM.md
      strategy-brief-ENG001-SIM.docx  ← client-facing brief
```

## Reference models

Every engagement, whatever the customer, is grounded in three **reference
models** (in `reference/`). Each answers a different question — and what stays
constant across all customer journeys is exactly this grounding, which is CPDSE's
consistency advantage.

| Model | Answers | Summary |
|---|---|---|
| **Pharma Value Chain Model** | **Where** in the drug pipeline? | 2-tier linear: Pre-clinical → Clinical development → On-market → 14 substeps |
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

## Workflow types & customer journeys

Customer-facing work is organised into **three workflow types** (hub:
[`services/README.md`](services/README.md)). They group five concrete customer
triggers ("journeys"), captured originally on the value-stream board
(`reference/value streams - DRAFT.pdf`). Each journey is described by what brings
the customer to us, what we gather, what we do, what we hand over, the impact, the
return for CPDSE, and the contribution to the mission.

### Research
*Customers: researchers, research groups, departments.*

**Research & DS Strategy** — the fully designed, built workflow (see the Pipeline
below).

| Stage | Content |
|---|---|
| Customer problem | "My research group wants to make better use of PDS." |
| Input to us | **Passive:** lab website, current grants, publications. **Active:** PI fills questionnaire + Meeting 1 walkthrough interview. |
| Our work | Run the research DS strategy workflow (Steps 1–4 of the AI pipeline); conduct 2 workshops. |
| Our output | Recommendation document with commitments (the strategy brief .docx). |
| Impact for customer | Concrete commitments to improve. |
| Value for us | **Portfolio of happy customers** (referrals between PIs in adjacent groups) + **learning about practical challenges** (every `[BEYOND REFERENCE]` / `[OUTSIDE MODEL]` flag improves our reference docs). |
| Value for overall purpose | More PDS in research helps on the longer term. |

**Specific Research Consulting** — *in design.* Time-based, not fixed-scope.

| Stage | Content |
|---|---|
| Customer problem | "I have a specific research question and need help." |
| Input to us | Structured interview with AI to assess needs and current competencies; live interview with human; workplan and agreement. |
| Our work | According to workplan and agreed time allocation. |
| Our output | As agreed in workplan. |
| Impact for customer | DS research problem solved; learned something. |
| Value for us | Portfolio of happy customers. |
| Value for overall purpose | A *little* bit more pharma data research. |

### Educational
*Customers: teachers, course owners, curriculum leaders, and their staff.* All
**in design.**

**Course Upgrade**

| Stage | Content |
|---|---|
| Customer problem | "My course doesn't have enough modern PDS." |
| Input to us | **Passive:** course description, past evaluations, all current course material. **Active:** interview with course responsible. |
| Our work | Structured AI analysis; human in the loop. |
| Our output | Upgrade plan; AI-generated inspiration material. |
| Impact for customer | "My course has been supercharged with DS and AI, with good didactics." |
| Value for us | Portfolio of happy customers; learning about practical challenges. |
| Value for overall purpose | Pharma education is one step closer to the future. |

**Staff Upskilling**

| Stage | Content |
|---|---|
| Customer problem | "Our staff needs new skills." |
| Input to us | *[draft]* presumed similar to Course Upgrade (course materials + responsible interview). |
| Our work | *[draft]* likely the same structured AI + human-in-the-loop pattern. |
| Our output | PDS resource and Course Lead onboarded to structure and flow. |
| Impact for customer | Clarity on what and how I should learn. |
| Value for us | Portfolio of happy customers. |
| Value for overall purpose | Students come out with state-of-the-art skills from the course. |

**New Course Creation**

| Stage | Content |
|---|---|
| Customer problem | "We need a new course with lots of PDS." |
| Input to us | **Often CPDSE-initiated** (we have the idea ourselves) — an asymmetry vs the other journeys. |
| Our work | Structured AI analysis + commitment to an upgrade plan. |
| Our output | Assigned PDS resource. |
| Impact for customer | Pharmaschool as a cool offering. |
| Value for overall purpose | *[to define]* |

### Internal self-improvement
*Customer: CPDSE itself.* **Stub** — onboarding new consultants and building
shared infrastructure (this project is an example). Not among the five
customer journeys; see [`services/internal/`](services/internal/).

### Open questions (from the value-stream draft)
- **Staff Upskilling** intake/work were sparse on the board — does it collapse
  into Course Upgrade (same intake, different output), or is the intake genuinely
  different?
- **New Course Creation** "value for overall purpose" is undefined — inherit
  Course Upgrade's, or draw something specific to net-new courses?
- "Value for us" was treated as a shared cross-journey return, not attributed per
  row — confirm that abstraction.
- The three Educational journeys likely share more than drawn; a consolidation
  pass before a real Educational workflow design would help.

## Pipeline (Research & DS Strategy)

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

## Prompt versioning

All prompt documents are versioned independently. When updating a prompt,
increment the version number and log it in engagement-log.md.
The engagement log maps each engagement to the model + prompt versions used,
ensuring reproducibility.

## Status

All three reference models exist (`reference/`). The Research & DS Strategy
workflow is the only one fully designed; all its prompt documents are v0.1.0
AI-drafted, pending expert review before the first real engagement. ENG001-SIM is
a simulated test engagement only. See [`TODO.md`](TODO.md) for near-term work.
