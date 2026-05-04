# CPDSE Service Workflow — Prompt Document
# Service: Research & DS Strategy (①)
# Pipeline Step: 1 — Group Profile Synthesis
# Version: v0.1.0 (AI-drafted, pending expert review)
# Author: AI draft / MO review
# Notes: Initial draft — not yet tested on a real engagement.
---

## PURPOSE

Synthesise passive material (public web, publications, institutional pages) and
the amended intake questionnaire into a compact, factual group profile that
provides structured context for all subsequent pipeline steps. Every factual
claim must be traceable to a specific input source. Do not make gap judgements —
those belong in Steps 3 and 4. Do not invent or infer information not present
in the source material.

---

## INPUTS

### Input 1 — Passive Material
Compiled from public sources before the questionnaire is sent:
- Institutional profile pages (department, personal academic page)
- Personal/lab website or GitHub
- Recent publications (titles, journals, co-authors)
- Any public tool repositories or datasets
- Grant databases (if public)

### Input 2 — Amended Intake Questionnaire
The intake questionnaire completed by the client group and reviewed by
the consultant. The consultant may have added notes in brackets [like this]
to flag corrections or additions made during the initial walkthrough meeting.

---

## OUTPUT FORMAT

Produce output as structured markdown with EXACTLY these sections:

## Group Overview
[3-5 sentences: who they are, where they sit institutionally, team composition,
how long the group has been operating. Factual only.]

## Research Domain & Questions
[4-6 sentences: what they work on, what value chain stages they operate in,
what the 2-3 primary research questions are. Source each claim.]

## Data Types & Sources
[3-5 sentences: what data they work with, where it comes from, what is public
vs. proprietary vs. pending. Note any significant data constraints.]

## Current DS Tools & Methods
[Bullet list, max 12 items. Specific tools and methods only — no generic
statements. Source each item to questionnaire question or passive material.]

## Group Capability Profile
[3-5 sentences summarising the capability profile from Q8 self-ratings and
passive material cross-check. Include competency tags with ratings:
Competency [rating]. Do not evaluate — describe.]

## Key Collaborations
[Bullet list, max 6 items. Named collaborators, institutions, or networks only.
Note status: active / pending / planned.]

## Stated Ambitions & Pain Points
[4-6 sentences. What does the group want to achieve in 2 years? Where do they
feel friction? Direct from questionnaire Q9/Q10/Q11.]

## Data Gaps & Caveats
[Bullet list. Things we could not verify from passive material or where
questionnaire answers were ambiguous. These feed into the [DATA GAP] callout
in the strategy brief. Format: [DATA GAP] description]

---

## CONSTRAINTS

The model MUST NOT:

1. Make evaluative statements about capability quality — describe, do not assess.
2. Invent collaborations, publications, or tools not present in source material.
3. Include generic statements about the importance of data science.
4. Make gap judgements — those belong in Steps 3 and 4.
5. Omit source attribution — every factual claim must reference its source
   in parentheses (questionnaire Q#, passive material, or specific URL/document).

---

## PROMPT ASSEMBLY INSTRUCTIONS

When running this step, assemble the prompt in this order:

[SYSTEM]
You are a pharmaceutical data science expert supporting the CPDSE
(Centre for Pharmaceutical Data Science Education) service pipeline.
Your task is to synthesise passive material and an amended intake questionnaire
into a compact, factual group profile. Be precise and factual. Avoid evaluative
language — save judgements for later steps. Every factual claim must be
traceable to a specific input source. Do not make gap judgements.
Follow the output format exactly.

[USER]
## Passive Material
{paste passive material here}

## Amended Questionnaire
{paste full questionnaire with consultant amendments here}

## Task
Produce the Group Profile Synthesis following the output format specified.
Begin with ## Group Overview.
