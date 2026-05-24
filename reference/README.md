# CPDSE Reference Models — how they relate and build services

This folder holds CPDSE's three **reference models**. Each is **self-contained**:
a model describes only itself and does not cross-reference the others. The
relationships *between* models — and how they compose into service workflows —
live here, in this file. (Earlier drafts baked cross-references into the model
docs; that coupling was pulled out so each model can evolve independently.)

## The three models

Each model answers a different question about an engagement:

| Model | Answers | Folder |
|---|---|---|
| **Pharma Value Chain Model** | **Where** is the customer in the drug pipeline? (2-tier linear: Pre-clinical → Clinical development → On-market → 13 substeps) | [`pharma-value-chain-model/`](pharma-value-chain-model/) |
| **PDS Competence Model** | **What** data-science capabilities matter — assessed and targeted? (7 domains → 30 sub-areas → ~123 competencies, rated L1–L5) | [`competency-model/`](competency-model/) |
| **Pedagogic Practices** | **How** do we build those capabilities? (Bowman's 4Cs + Six Trumps) | [`pedagogic-practices/`](pedagogic-practices/) |

Supporting doc: [`competency-model-migration-crosswalk.md`](competency-model-migration-crosswalk.md)
maps the old placeholder competency model onto the current one.

## How they relate

The three models compress into one methodology line:

> *"To improve **capabilities** in **PharmaValueChain** we train and catalyse
> **Data Science Competencies** using **Training From the Back of the Room**
> practices."*

Read as: improve **competencies** (PDS Competence Model) at the customer's
**value-chain stage** (Pharma Value Chain Model) by **training** them (Pedagogic
Practices). *Where × What × How.*

## How a service workflow is constructed

Every CPDSE service, whatever the customer trigger, is built by composing the
three models in the same order:

1. **Anchor** — locate the customer on the Pharma Value Chain Model (which
   stage(s) they operate in). This sets which work is in scope.
2. **Assess & target** — use the PDS Competence Model to snapshot current
   capabilities and pick target levels. *The model intersection that matters here
   — which competencies are most relevant at which value-chain stage — is
   constructed per engagement (and will be formalised into a stage→competency map
   over time); it is deliberately **not** hard-coded into either model.*
3. **Deliver** — design the workshops/courses with Pedagogic Practices (4Cs for
   structure, Six Trumps as the within-block check) to move capabilities toward
   their targets.

A service workflow = a specific recipe over these three steps. Services differ in
emphasis, not in ingredients.

## The service portfolio

Customer-facing work is organised into **three workflow types** (see
[`../services/README.md`](../services/README.md)). All reuse the three models above
— that reuse is what keeps CPDSE consistent across consultants and customer types.

| Type | Customers | Workflows (status) | Model emphasis |
|---|---|---|---|
| **Research** | researchers, groups, departments | Research & DS Strategy (**built**); Specific Research Consulting (in design) | Anchor + Assess heavy; workshop delivery |
| **Educational** | teachers, course owners, curriculum leaders, staff | Course Upgrade; Staff Upskilling; New Course Creation (in design) | Competence targets + Pedagogic Practices heavy |
| **Internal self-improvement** | CPDSE itself | onboarding; infrastructure building (**stub**) | n/a — not customer-facing |

Only the Research **Research & DS Strategy** workflow is fully written up (see
[`../services/01-research-strategy/`](../services/01-research-strategy/)).
