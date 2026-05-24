# CLAUDE.md — CPDSE DS Consulting Service
# Project: cpdse-service-workflows
# Last session: 2026-04-25 (claude.ai)
# Handoff to: Claude Code
---

## Positioning

> "Pharma is full of data. But not of data science. We are here to change that."

**Methodology, in one line:** to improve capabilities in *PharmaValueChain* we
train and catalyse *Data Science Competencies* using *Training From the Back of
the Room* practices.

---

## What this project is

A structured data science consulting service for pharmaceutical research groups,
built by Morten Lindow (Professor, ILF/UCPH, Center Leader of CPDSE). The service
helps individual research groups identify and close DS capability gaps relative to
what comparable groups do at their pharma value chain stage.

This is Service ① — "Research & DS Strategy" — a fixed-scope engagement with an
AI-assisted analysis pipeline. It is Phase 1 of a broader CPDSE consulting service
portfolio that will eventually include time-based DS Research Consulting (②) and
Course Upgrade engagements (③).

### Customer journeys (from the value-stream board)

CPDSE serves five distinct customer triggers across the same 7-stage value
stream (customer problem → input → our work → output → impact → value for us →
overall purpose). Today only Service ① is fully designed and written up on the
website.

| # | Trigger | Service |
|---|---|---|
| 1 | "My research group wants to make better use of PDS." | ① — fully designed |
| 2 | "I have a specific research question and need help." | ② — in design |
| 3 | "My course doesn't have enough modern PDS." | ③ — in design |
| 4 | "Our staff needs new skills." | ③ — in design |
| 5 | "We need a new course with lots of PDS." | ③ — in design |

Source artefact: `reference/value streams - DRAFT.pdf` (still draft; promote to
versioned reference doc once stable).

---

## Repository structure

```
cpdse-service-workflows/
  README.md
  engagement-log.md                        ← maps engagement ID → prompt versions
  services/
    01-research-strategy/
      intake-questionnaire-blank-v0.1.0.txt
      prompts/                             ← THE CORE PIPELINE (see below)
        01-group-profile-synthesis.md
        02-ds-landscape-analysis.md
        03-gap-assessment.md
        04-recommendation-synthesis.md
      output-templates/
        workshop1-miro-frames.pdf          ← 4-frame PDF for Miro board import
        workshop1-facilitation-guide.docx  ← consultant session script
  reference/
    competency-model/                      ← PDS Competence Model (git submodule)
    pharma-value-chain-model/              ← Pharma Value Chain Model (git submodule)
    competency-model-migration-crosswalk.md ← old→new competency model mapping
  engagements/
    ENG001-MortenLindow/                   ← test engagement (simulated, 2028)
      intake-questionnaire-ENG001-SIM.txt
      step3-gap-assessment-ENG001-SIM.md
      step4-recommendation-synthesis-ENG001-SIM.md
      strategy-brief-ENG001-SIM.docx       ← client-facing Word brief
```

The full zip is at: `/home/claude/cpdse-service-workflows.zip` (from last session).
It also exists locally in `/home/claude/cpdse-service-workflows/`.

---

## The AI pipeline — how it works

The pipeline runs Steps 1–4 sequentially. Each step is a prompt document in
`services/01-research-strategy/prompts/`. In Phase 1, a consultant manually
pastes outputs between steps. Phase 2 will automate this via API.

```
Passive collection (lab site, grants, pubs, READMEs) (~1h)
→ Active intake: questionnaire (client async, ~30min)
              + Meeting 1 walkthrough + amendment (~1h)
→ Step 1: Group Profile Synthesis       [factual only, human checkpoint]
→ Step 2: DS Landscape Analysis         [value chain map + open landscape + competency model]
→ Step 3: Gap Assessment                [structural vs technical, impact/effort/urgency]
→ Step 4: Recommendation Synthesis      [quick wins / strategic / horizon]
→ Consultant QA (~1h)
→ Workshop 1 (~2h)                      [Miro board + facilitation guide]
→ Workshop 2 (~1.5h)                    [final brief + roadmap]
Total consultant time: ~7-8h per engagement
```

---

## Core design decisions — the WHY

### Why structured prompts as .md files, not a Claude agent

Phase 1 is a human-in-the-loop workflow: consultant reads Step 1 output, validates
it with the client in Meeting 1, then runs Step 2. This is intentional. The risk
of a fully agentic pipeline is that errors compound across steps with no human
correction point. Step 1 is explicitly factual-only so the consultant can verify
it before analysis begins. Phase 2 (API-backed agent) is deferred until the manual
workflow has been tested on 2-3 real engagements.

### Why structural vs. technical gap distinction (Step 3)

This is the analytical frame that differentiates the service from generic DS advice.
Structural gaps (reproducibility, data management, workflow design, team knowledge
distribution) affect all research threads simultaneously — fixing one improves
everything. Technical gaps affect one method or capability. Most academic groups
come in expecting a list of tools to learn. The structural/technical frame shifts
the conversation to higher-leverage interventions. The distinction must be preserved
in all outputs, workshop materials, and the strategy brief.

### Why Step 1 is factual-only

Step 1 (Group Profile Synthesis) must contain zero evaluative language. It is shared
with the client at Workshop 1 as a "mirror" — a proof that CPDSE understood them
correctly. If it contains gap judgements, the client becomes defensive rather than
corrective. Gap judgements live exclusively in Step 3.

### Why the [OUTSIDE MODEL] and [BEYOND REFERENCE] flags

These flags are first-class outputs, not error conditions.
- [BEYOND REFERENCE]: the Pharma Value Chain Model (`reference/pharma-value-chain-model/`)
  is incomplete — when Step 2 encounters methods not in it, flagging them feeds
  reference model improvement.
- [OUTSIDE MODEL]: when work doesn't map to any sub-area of the PDS Competence
  Model, it signals a potential gap in the model itself. The discovery cascade
  stochastic process modelling work in ENG001-SIM was flagged [OUTSIDE MODEL] —
  it exposed a missing "Quantitative Process Modelling" sub-area (still uncovered
  by the 30-sub-area PDS model, so the finding stands). Step 4 routes such items
  to the `competency-model` repo as candidate additions.
Both flags flow through to Step 4's Competency Model Note, which is a meta-output
for the CPDSE team, not for the client.

### Why the engagement has a "value for us" column at all

The value-stream board names two non-revenue returns CPDSE earns from every
engagement, and we should design for them deliberately:
- **Portfolio of happy customers** — the basis for word-of-mouth referrals
  between PIs in adjacent groups. Workshop 2 specifically asks for permission
  to anonymise + cite.
- **Learning about practical challenges** — every engagement teaches us where
  our reference models break. The `[BEYOND REFERENCE]` and `[OUTSIDE MODEL]`
  flags above are the operational mechanism: every flagged item is a structured
  improvement to either the Pharma Value Chain Model
  (`reference/pharma-value-chain-model/`) or the competency model itself. Without
  these flags, "value for us" stays implicit and the reference docs stay stale.

### Why "a recommendation that requires more capacity than the group has is not a
recommendation — it is a wish"

This is the constraint that prevents Step 4 from producing generic DS advice.
Every recommendation must be calibrated to the actual team (who can implement it),
bandwidth (PI is CPDSE Center Leader with constrained time), and timeline (Emma
thesis transition in ~12 months in ENG001-SIM). The constraint is written into the
Step 4 prompt document explicitly.

### Why the brief is handed over at the END of Workshop 1, not before

If the client receives the brief before the workshop, Workshop 1 becomes them
reacting to the document rather than producing shared ownership of the diagnosis.
The brief is a record of what was decided, not a script for what to think.

### Why the filter question in Workshop 1 Block 4

"Which of these would you actually do in the next 4 weeks if we weren't in the
room?" is the most important move in the roadmap exercise. It distinguishes genuine
quick wins from aspirational items that need something else to be true first. If
the answer is "none of them," something went wrong earlier in the session.

### Why dot voting divergence matters in the gap exercise

The most useful data from the dot vote (Block 3) is not totals — it's divergence
between the PI and the rest of the group. If Morten votes for technical gaps and
master students vote for structural gaps, that tension is data worth surfacing
explicitly. The facilitation guide scripts this.

---

## The CPDSE PDS Competence Model

All gap assessments, capability snapshots, and competency model maps use the
**Pharmaceutical Data Science (PDS) Competence Model**, vendored in this repo as a
git submodule at `reference/competency-model/` (canonical spec:
`PDS_Competence_Model_Full_Rethought.md`; the L1–L5 rubric:
`Level_Rubric.md`). The pinned submodule commit is the model version.

Structure: **7 domains → 30 sub-areas → ~123 competencies.** The seven domains:
1. Computing & Programming
2. Data Acquisition & Management
3. Ethics, Legislation & Privacy
4. Exploration, Mining & Analysis
5. ML & AI
6. Mathematics & Statistics
7. Visualization & Presentation

Rating scale (L1–L5 Dreyfus, plus N/A): N/A=not relevant | L1=Awareness |
L2=Familiarity | L3=Proficiency *(target working level)* | L4=Mastery |
L5=Expertise.

**Two-tier use:** clients self-rate at the **domain** level in intake Q8 (clean
successor to the old 7 sub-areas); consultant-facing analysis (Step 2 landscape,
Step 3 gaps) drills into the **30 sub-areas and named competencies**. Don't
hard-code the 30 sub-areas in prompt docs — point to the submodule as the single
source of truth and inline only the 7 domains where a self-contained list helps.

This replaced the old v0.1.0 placeholder (7 flat sub-areas, 0–4 scale) on
2026-05-24. See `reference/competency-model-migration-crosswalk.md` for the
old→new mapping; engagements run under the old model (ENG001-SIM) stay frozen and
are read through that crosswalk.

---

## Three reference models (the CPDSE advantage and consistency)

Every engagement, regardless of customer type, is grounded in three reference
models. Together they are how we stay consistent across consultants, services,
and customer triggers.

1. **Pharma Value Chain Model** — a 2-tier linear model: 3 top-tier steps
   (Pre-clinical → Clinical development → On-market) → 13 substeps from target
   identification to pharmacoepidemiology. Used to anchor every engagement to the
   customer's actual pipeline stage(s). Vendored as a git submodule at
   `reference/pharma-value-chain-model/` (canonical doc:
   `Pharma_Value_Chain_Model.md`); the pinned commit is the version. v0.2.0,
   6 of 13 substeps written up, 7 stubs.

   **Sync points** (everywhere the value chain model is referenced — keep in step
   when the submodule is bumped to a new model version):
   - `CLAUDE.md` — this entry + "Pharma value chain model" section below
   - `README.md` — repository structure block
   - `reference/cpdse-value-stream-v0.1.0.md` — three-models table
   - `services/01-research-strategy/prompts/02-ds-landscape-analysis.md` — reference model input + [BEYOND REFERENCE] definition + paste block
   - `site/index.html` — reference-model card / tab copy
   - Any populated engagement (`engagements/ENG###-*/`) — new engagements use the current model version; finished engagements stay frozen (note version in their engagement-log entry).

2. **PDS Competence Model** — 7 domains / 30 sub-areas / ~123 competencies,
   rated L1–L5 (see "The CPDSE PDS Competence Model" section above). Vendored as
   a git submodule at `reference/competency-model/`; the pinned commit is the
   version. Used in capability snapshots, gap assessments, and the competency
   model map output.

   **Sync points** (everywhere the model is referenced — keep in step when the
   submodule is bumped to a new model version):
   - `CLAUDE.md` — "The CPDSE PDS Competence Model" section above
   - `reference/cpdse-value-stream-v0.1.0.md` — three-models table
   - `reference/pharma-value-chain-model/` — per-substep competency mappings (separate submodule)
   - `reference/competency-model-migration-crosswalk.md` — old→new crosswalk + scale
   - `services/01-research-strategy/prompts/02-ds-landscape-analysis.md` — competency snapshot construction
   - `services/01-research-strategy/prompts/03-gap-assessment.md` — gap-to-competency mapping
   - `services/01-research-strategy/prompts/04-recommendation-synthesis.md` — Competency Model Note
   - `services/01-research-strategy/intake-questionnaire-blank-v0.2.0.txt` — self-rating section (Q8, domain level)
   - `site/index.html` — "How we work" reference-model card + "For research groups" / "For consultants" tab copy
   - Any populated engagement (`engagements/ENG###-*/`) — new engagements use the current model; finished engagements stay frozen at the version they were run under (note version in their engagement-log entry).

3. **Training from the Back of the Room** — Sharon L. Bowman's pedagogical
   framework. The reference behind our workshop design. The core construct is
   the **4Cs** of training: **Connections** (anchor learners to prior
   knowledge and to each other), **Concepts** (deliver new content in short
   bursts), **Concrete Practice** (learners apply, not the trainer), and
   **Conclusions** (learners summarise and commit to action). Workshop 1's
   six-block timing should map cleanly onto these — currently implicit, not
   yet explicit in the facilitation guide.
   - **TODO:** flesh out the 4Cs → Workshop 1 block mapping in the
     facilitation guide. Note that "Mirror" maps to Connections, "Landscape"
     and "Gaps" carry Concepts + Concrete Practice (gap card exercise is the
     Concrete Practice anchor), "Roadmap" + "Close" handle Conclusions.

The unifying methodology line — *"To improve capabilities in PharmaValueChain
we train and catalyse Data Science Competencies using Training From the Back
of the Room practices"* — is the verbal compression of these three models.

---

## Pharma value chain model

The Pharma Value Chain Model is vendored as a git submodule at
`reference/pharma-value-chain-model/` (repo: `cpdse-pharma-value-chain-model`;
canonical doc: `Pharma_Value_Chain_Model.md`). It is **2-tier and linear**:

- **Tier 1 — three top-tier steps:** Pre-clinical → Clinical development → On-market
- **Tier 2 — 13 substeps** within those steps.

v0.2.0 covers 6 of 13 substeps in full; 7 are stubs:
- Pre-clinical: Target Identification ✓, Hit Identification ⬚, Lead Identification ✓,
  Lead Optimisation ✓ (oligo notes), Candidate Selection ⬚, Preclinical (DMPK/tox) ⬚
- Clinical development: Biomarker Development ✓, Clinical Pharmacology ✓ (NABM notes,
  [BEYOND REFERENCE]), Phase I/II/III ⬚, Regulatory ⬚
- On-market: Manufacturing ⬚, Market Access (HEOR) ⬚, Pharmacoepidemiology ✓

The model versions independently of the prompt docs; the pinned submodule commit
is the version. This replaced the flat `pharma-value-chain-reference.md` (v0.1.1)
on 2026-05-24 when the model was promoted to its own submodule and restructured
into the 2-tier form.

---

## ENG001-SIM — the test engagement

This is a fully simulated 2028 engagement for Morten Simulated Lindow's group.
It was designed to be a realistic test of the pipeline, not a trivial case.

**Team:** Emma Sørensen (PhD yr2), Jonas Andersen (postdoc yr1), 3 master students
(Anna, Bjorn, Priya). Morten is PI but technically rusty and bandwidth-constrained
by CPDSE leadership.

**Research questions:**
1. ASO safety/toxicity ML prediction (OpenOligoFeat) — generalised model from
   sequence + chemistry features; existing hepatotox predictor doesn't generalise
   to newer chemistries
2. Mechanistic PKPD for GalNAc-siRNA (OpenNABMPKPD) — compartment model for
   tissue uptake, intracellular trafficking, RISC loading, mRNA knockdown
3. Discovery cascade design as optimisation problem (OpenDiscoveryCascadeModel) —
   minimum assay set to distinguish productive/unproductive lead series in 3 months

**Value chain:** Lead Optimisation (primary), Lead Identification + Clinical
Pharmacology (secondary)

**Capability ratings:** Bioinformatics [4], ML [3], Scientific Programming [3],
Data Management [3], Statistical Analysis [2], Reproducible Research [2],
Data Visualisation [2]

**Key constraints:**
- Dataset sparsity for oligo safety — hard external constraint
- Two Roche data-sharing agreements unsigned (NDAs pending)
- Emma enters thesis phase ~12 months — OpenOligoLake continuity risk
- No external research grant — needs one within 18 months for postdoc

**Pipeline results:**

Step 3 dominant finding: ~60% structural / ~40% technical gaps. The most
constraining internally-solvable gap is PKPD pipeline non-reproducibility
(High impact, Low effort, Active — Docker + random seed fix).

Step 4 strategic thrust: fix infrastructure → strengthen ML credibility →
build toward industry data access.

Quick wins (all no-dependency, weeks not months):
1. Containerise PKPD workflow (Jonas, 2-3 person-weeks)
2. Structured extraction template for OpenOligoLake (Emma, 3 person-weeks)
3. Retroactive model cards on existing models (Jonas, 2-3 person-days) — BEFORE
   any Roche agreement is signed
4. Shared matplotlib style sheet (Jonas, 2 person-days)

Most time-sensitive strategic item: Emma succession plan must START by month 3.

[OUTSIDE MODEL] flag: OpenDiscoveryCascadeModel (research Q3) maps to operations
research / stochastic process modelling — no CPDSE sub-area captures it.
Suggested new sub-area: "Quantitative Process Modelling."

---

## Workshop 1 — the facilitation design

### Know / Feel / Do framework

**KNOW:**
1. We understood you correctly — or here's where we were wrong
2. The dominant problem is structural, not technical
3. Three things you can do next week, not twelve things eventually

**FEEL:**
1. Seen (not assessed) — the [DATA GAP] callouts build trust
2. Appropriately provoked, not overwhelmed — 2-3 moments of genuine surprise
3. Owners of the diagnosis (gap card exercise produces this)
4. Permission to not do everything (watch list and horizon sections)

**DO:**
1. In the room: fill in the commitments table (3 commitments, 3 owners, 3 dates)
2. In 4 weeks: at least one quick win started
3. In 3-6 months: Emma succession plan started (has a hard deadline)

### Session timing

```
00:00–00:10  OPEN — contract setting, opening round
00:10–00:35  BLOCK 1: Mirror — validate profile, surface corrections
00:35–01:00  BLOCK 2: Landscape — 3 curated provocations
01:00–01:30  BLOCK 3: Gap exercise — dot vote, challenge zone, missing zone
01:30–01:50  BLOCK 4: Roadmap — filter question, ownership assignment
01:50–02:00  CLOSE — commitments read back, brief handover
```

### The Miro board

`output-templates/workshop1-miro-frames.pdf` is a 4-page landscape A3 PDF (one
page per block). Import each page as a background image into Miro, then layer
interactive elements on top (sticky notes for correction/challenge zones, Miro
voting for dot votes). Built with ReportLab in Python.

The four frames:
- Frame 01 (NAVY): value chain card, capability snapshot table, correction zone
- Frame 02 (TEAL): structural/technical framing box, 3 finding cards, field notes
- Frame 03 (RED): 8 gap cards (4 structural NAVY, 4 technical TEAL), challenge
  zone, missing zone, dot vote circles on each card
- Frame 04 (AMBER): filter question, 4 quick win cards with owner/date fields,
  strategic summary strip, sequencing rail, commitments table

### The facilitation guide

`output-templates/workshop1-facilitation-guide.docx` is the consultant-facing
script. Structure per block: Script (what to say, in quotes), Move (what to do),
If (what to watch for and how to handle it). Key moments scripted:

- "Which rating is most wrong, and in which direction?" (not "do you agree?")
- "Emma, this card is specifically about you. Is the 12-month timeline accurate?"
- "Who will ACTUALLY DO this, not who is responsible for it?"
- "What would have to happen for this NOT to be a priority in the next 3 months?"
  (resolves Morten hedging on Emma succession)
- Morten should not own more than one quick win
- Brief is handed over at minute 110, not before

---

## The strategy brief

`engagements/ENG001-MortenLindow/strategy-brief-ENG001-SIM.docx` is the
client-facing Word document. Built with docx.js (Node). Five sections:

01. How we read your group (value chain card, capability snapshot, DATA GAP callout)
02. The landscape you're operating in (3 curated findings as left-border callouts)
03. Gap assessment (full table: type, gap, competency, impact, effort, urgency)
04. What we recommend (quick win cards, strategic summary, 18-24mo horizon, watch list)
05. Commitments from today (fillable table, blank — filled in at end of Workshop 1)

The brief template is the general form; a populated example is in ENG001-SIM.
The blank `output-templates/` directory is where the generic template should live.

---

## Gotchas and lessons learned

### docx.js syntax
The `})]}]},` closing bracket pattern causes `SyntaxError: missing ) after argument
list` in Node. When creating compact inline Table → TableRow → TableCell structures,
always expand them into separate `new TableRow({ children: [ new TableCell({...}) ] })`
blocks. The compact form looks fine but Node's parser chokes on it.

`PageNumber` is not a valid import from docx@9.6.1. Use `PageNumberElement` instead.

### ReportLab label() function
The custom `label()` helper in the workshop board script does not accept an `italics`
keyword argument. Remove it or add support explicitly. The helper is a thin wrapper
around `c.drawString()`.

### Google Drive API via MCP
The Drive MCP `create_file` tool requires base64-encoded content even for plain text.
Binary files (docx, pdf) work but are slow because the base64 encoding is large.
For large files in Claude Code, it's faster to write locally and sync manually than
to upload via MCP API calls. Drive uploads in the claude.ai session were unreliable
and slow — this is why we saved everything locally.

### Python base64 heredoc encoding
When using `python3 << 'PYEOF' ... PYEOF` heredocs to encode content for Drive
upload, special characters in the content (especially single quotes in Python
string literals like `r.readAsDataURL`) can break the heredoc. Use a Python file
instead of inline heredoc for anything complex.

### Pharma value chain reference doc
The NABM/oligo-specific content in Clinical Pharmacology goes significantly beyond
what's in the reference doc. Three specific items need adding before the next real
engagement:
- GalNAc delivery system and liver-tropism specifics
- RNA secondary structure tools (RNAfold, IntaRNA) in Lead Identification
- NABM multi-scale mechanistic modelling approaches in Clinical Pharmacology
These are flagged [BEYOND REFERENCE] in the ENG001-SIM Step 2 output.

### The Emma succession card in Workshop 1
This gap card will produce awkward silence in any real engagement where a PhD
student is in the room. The facilitation guide scripts the direct question
("Emma, this card is specifically about you") — but test this approach carefully
before the first real engagement. The consultant must name it rather than let
the awkwardness accumulate.

### LLM extraction hallucination on safety data
ENG001-SIM includes a real lesson: GPT-4 API was attempted for OpenOligoLake
automated extraction but reverted due to hallucination on safety-critical numerical
values. The current approach is human curation with LLM pre-screening. The
18-24 month horizon revisits this with structured output APIs (JSON schema
enforcement). Don't recommend LLM extraction for safety-critical numerical data
without a human verification layer.

---

## What is done

- [x] Service portfolio design (Services ①②③④)
- [x] AI pipeline design (Steps 1–4)
- [x] All 4 prompt documents (v0.1.0, AI-drafted, pending MO review;
  prompts 02–04 bumped to v0.2.0 for the PDS model swap)
- [x] Intake questionnaire blank template (v0.1.0; v0.2.0 for PDS model swap)
- [x] Pharma value chain reference doc (v0.1.1, 6 stages)
- [x] **Swap in the PDS Competence Model** (2026-05-24) — vendored as a git
  submodule at `reference/competency-model/`; all sync points re-synced;
  `reference/competency-model-migration-crosswalk.md` records the old→new map
- [x] ENG001-SIM — simulated test engagement, full pipeline run
- [x] Step 3 output for ENG001-SIM
- [x] Step 4 output for ENG001-SIM
- [x] Strategy brief Word doc (ENG001-SIM populated example)
- [x] Workshop 1 Miro board PDF (4 frames, landscape A3)
- [x] Workshop 1 facilitation guide Word doc (full consultant script)
- [x] Full directory structure zipped locally
- [x] Know/Feel/Do framework for Workshop 1
- [x] Session timing design (6 blocks, 2 hours)

## What is NOT done yet

- [ ] Flesh out the Training from the Back of the Room reference: explicit
  4Cs → Workshop 1 block mapping, written into the facilitation guide
- [ ] Promote `reference/value streams - DRAFT.pdf` to a versioned reference
  document — **DONE** as `reference/cpdse-value-stream-v0.1.0.md`. Remaining
  work: resolve `[?]` cells and bump to v0.2.0.
- [ ] Step 1 output for ENG001-SIM (group profile synthesis — only passive
  material versions exist; needs full combined version with questionnaire)
- [ ] Step 2 output for ENG001-SIM (DS landscape — was synthesised in conversation
  but not saved as a file in the engagement folder)
- [ ] Blank strategy brief template (the ENG001-SIM one is populated; need a
  generic version with {placeholder} fields in output-templates/)
- [ ] Workshop 1 Miro board — actual build in Miro (PDF frames need to be imported
  and sticky notes / voting set up manually)
- [ ] Workshop 2 design (facilitation guide + artefacts — not started)
- [ ] Workshop 1 summary doc template (the 48hr post-session artefact)
- [ ] Phase 2 planning: API-backed agent pipeline (deferred until 2-3 real engagements)
- [ ] Expert review of all v0.1.0 prompt documents (MO review pending)
- [ ] Remaining 7 substep stubs in `reference/pharma-value-chain-model/`
- [ ] First real engagement (not ENG001-SIM)
- [ ] Updating reference doc with ENG001-SIM [BEYOND REFERENCE] items
- [ ] CPDSElogic integration (separate project — the web app for the CPDSE
  competency model and people directory)

---

## File locations (local, end of session)

```
/home/claude/cpdse-service-workflows/           ← full directory tree
/home/claude/cpdse-service-workflows.zip        ← zipped for download
/home/claude/brief.js                           ← Node script that generates strategy brief
/home/claude/cpdse-strategy-brief-ENG001-SIM.docx
/home/claude/workshop1_board.py                 ← Python script for Miro PDF frames
/home/claude/workshop1_miro_frames.pdf
/home/claude/facilguide.js                      ← Node script for facilitation guide
/home/claude/workshop1_facilitation_guide.docx
```

Google Drive root folder: CPDSE Service Workflows
Drive folder ID: 1yP89_U5sFe0okd_y4MYrQ0D6wJM4Z86S
(Note: Drive sync was unreliable in session — local files are the source of truth)

---

## Morten's context

- Professor, ILF/UCPH, Department of Drug Design and Pharmacology
- Center Leader, CPDSE (Centre for Pharmaceutical Data Science Education)
- Cross-institutional network: UCPH + SDU
- Connected to HeaDS, EKA, ILF-LT
- Background: Santaris Pharma → Roche Innovation Center Copenhagen (2008-2024)
- Expertise: oligonucleotide/RNA therapeutics, bioinformatics, pharma strategy
- Codes in Ruby, R — currently learning React/FastAPI for CPDSElogic
- Votes Alternativet, interested in Holacracy/Teal/sociocracy
- Active in Grundejerforeningen Vildrose (homeowners' association, chairs meetings)
- Preference: concise output over comprehensive elaboration

---

## How to pick up in Claude Code

1. `cd` into the project directory (or clone from wherever Morten puts it)
2. The most pressing missing files are the Step 1 and Step 2 outputs for ENG001-SIM
   — synthesise them from the conversation context in the transcript
3. The blank strategy brief template needs to be created from the ENG001-SIM .docx
   by replacing populated content with {placeholder} fields
4. The Pharma Value Chain Model (`reference/pharma-value-chain-model/`) needs 3
   oligo-specific additions before the service is ready for a real engagement (see
   Gotchas above); edit in the standalone clone, push, then bump the submodule pin
5. All prompt documents are v0.1.0 AI-drafted — Morten needs to review them before
   using on a real group; flag anything that needs domain expert adjustment

The full conversation transcript is available at:
/mnt/transcripts/2026-04-25-15-51-13-cpdse-service-architecture.txt
