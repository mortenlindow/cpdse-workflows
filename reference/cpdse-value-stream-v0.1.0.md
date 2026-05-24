# CPDSE Value Stream — v0.1.0

> Source: `reference/value streams - DRAFT.pdf` (Miro board export, 2026-04-26).
> This document is the markdown promotion of that draft. Where the board was
> sparse or ambiguous, cells are marked `[—]` (intentionally empty on the
> board) or `[?]` (unclear from the export — to be confirmed in next session).

---

## One-line positioning

> "Pharma is full of data. But not of data science. We are here to change that."

## Methodology

To improve capabilities in **PharmaValueChain** we train and catalyse
**Data Science Competencies** using **Training From the Back of the Room**
practices.

---

## The seven stages

Every CPDSE engagement, regardless of which customer journey it serves, moves
through the same seven stages. The columns of the value stream:

| # | Stage | What it captures |
|---|---|---|
| 1 | **Customer problem** | The trigger that brings the customer to us |
| 2 | **The input to us** | What we gather (passive) and ask for (active) before we start work |
| 3 | **Our work** | The structured AI-assisted analysis + human-in-the-loop activities |
| 4 | **Our output** | The artefact handed to the customer |
| 5 | **Impact for customer** | What changes for the customer once they have the output |
| 6 | **Value for us** | What CPDSE earns from running the engagement (beyond fees) |
| 7 | **Value for overall purpose** | How this engagement nudges pharma toward more data science |

Stages 1–5 are the customer's experience. Stage 6 is the business case for
CPDSE. Stage 7 is the mission.

---

## The five customer journeys

Three serve **course / education** customers (Service ③). Two serve
**research** customers (Service ① and ②). The same seven stages, populated
differently per row.

### Journey 1 — "Course doesn't have enough modern PDS" *(Service ③)*

| Stage | Content |
|---|---|
| Customer problem | "My course doesn't have enough modern PDS." |
| Input to us | **Passive:** course description, past evaluations, all current course material. **Active:** interview with course responsible. |
| Our work | Structured AI analysis; human in the loop. |
| Our output | Upgrade plan; AI-generated inspiration material. |
| Impact for customer | "My course has been supercharged with DS and AI, with good didactics." |
| Value for us | Portfolio of happy customers; learning about practical challenges. *[shared across journeys; not row-specific on board]* |
| Value for overall purpose | The pharma education is one step closer to the future. |

### Journey 2 — "Staff needs new skills" *(Service ③)*

| Stage | Content |
|---|---|
| Customer problem | "Our staff needs new skills." |
| Input to us | [?] — board sparse for this row; presumed similar to Journey 1 (course materials + responsible interview). |
| Our work | [?] — likely the same structured AI + HIL pattern. |
| Our output | PDS resource and Course Lead onboarded to structure and flow. |
| Impact for customer | Clarity on what and how I should learn. |
| Value for us | Portfolio of happy customers. |
| Value for overall purpose | Students come out with state-of-the-art skills from the course. |

### Journey 3 — "We need a new course with lots of PDS" *(Service ③)*

| Stage | Content |
|---|---|
| Customer problem | "We need a new course with lots of PDS." |
| Input to us | **Often CPDSE has the idea ourselves** — i.e. CPDSE-initiated, not customer-initiated. *(Important asymmetry vs other journeys.)* |
| Our work | Structured AI analysis + commitment to an upgrade plan. |
| Our output | Assigned PDS resource. |
| Impact for customer | Pharmaschool as a cool offering. |
| Value for us | Portfolio of happy customers; learning about practical challenges. |
| Value for overall purpose | [—] |

### Journey 4 — "Research group wants to make better use of PDS" *(Service ①)*

This is the journey fully designed and written up on the website.

| Stage | Content |
|---|---|
| Customer problem | "My research group wants to make better use of PDS." |
| Input to us | **Passive:** lab website, current grants, publications. **Active:** PI fills questionnaire + Meeting 1 walkthrough interview. |
| Our work | Run research DS strategy workflow (Steps 1–4 of the AI pipeline); conduct 2 workshops. |
| Our output | Recommendation document with commitments (the strategy brief .docx). |
| Impact for customer | Concrete commitments to improve. |
| Value for us | **Portfolio of happy customers** (referrals between PIs in adjacent groups) + **learning about practical challenges** (every `[BEYOND REFERENCE]` / `[OUTSIDE MODEL]` flag improves our reference docs). |
| Value for overall purpose | More PDS in research helps on the longer term. |

### Journey 5 — "Specific research question, need help" *(Service ②)*

| Stage | Content |
|---|---|
| Customer problem | "I have a specific research question and need help." |
| Input to us | Structured interview with AI to assess needs and current competencies; live interview with human; workplan and agreement. |
| Our work | According to workplan and agreed time allocation. *(Time-based engagement, not fixed-scope.)* |
| Our output | As agreed in workplan. |
| Impact for customer | DS research problem solved; learned something. |
| Value for us | Portfolio of happy customers. |
| Value for overall purpose | A *little* bit more pharma data research. |

---

## The three reference models (the CPDSE advantage and consistency)

The streams differ row by row. What stays constant across all five — and
what gives CPDSE its consistency advantage — is that every engagement is
grounded in three reference models.

| Domain | Model | Where it shows up |
|---|---|---|
| **Pharma** | Pharma Value Chain Model | Every engagement maps customers to stage(s). Lives at `reference/pharma-value-chain-reference.md`. |
| **Data Science** | PDS Competence Model | Seven domains / 30 sub-areas / ~123 competencies, rated L1–L5 (Awareness→Expertise; L3 = target). Vendored at `reference/competency-model/` (git submodule). Clients self-rate at the domain level; analysis drills into sub-areas. |
| **Education** | Training from the Back of the Room (Bowman) | Pedagogical reference for workshop design. The 4Cs framework: Connections, Concepts, Concrete Practice, Conclusions. |

The methodology line at the top of this document is the verbal compression
of these three.

---

## Notes for the next revision

Items the board left ambiguous or sparse — to confirm in the next pass:

- **Journey 2** input and work columns were sparse on the board. Either the
  journey collapses into Journey 1 (same input/work, different output and
  impact), or there's a meaningfully different intake we haven't drawn yet.
- **Journey 3** "value for overall purpose" cell was empty. Either inherit
  from Journey 1 ("pharma education is one step closer to the future") or
  draw something specific to net-new course creation.
- The board did **not** show a `value for us` post-it on every row — it's
  treated above as a shared cross-journey return. Confirm this is the right
  abstraction, or attribute specifically per row.
- The three orange (course) rows likely share more than the board currently
  shows. A consolidation pass before a real Service ③ design would be useful.

## Versioning

- **v0.1.0** (2026-04-26) — Initial markdown promotion from
  `value streams - DRAFT.pdf`. Five journeys captured, three reference models
  named, seven stages defined. Several `[?]` cells remain.
