# CPDSE Service Workflow — Prompt Document
# Service: Research & DS Strategy (①)
# Pipeline Step: 3 — Gap Assessment
# Version: v0.2.0 (synced to PDS Competence Model; pending expert review)
# Author: AI draft / MO review
# Notes: Initial draft — not yet tested on a real engagement.
#        v0.2.0 tags gaps by PDS domain › sub-area (reference/competency-model/).
---

## PURPOSE

Cross-reference the group's current DS capabilities (from Step 1 Group
Profile) against the DS landscape for their relevant value chain stages
(from Step 2 Landscape Analysis) to identify meaningful gaps. Produce a
structured gap assessment that is specific, traceable, and prioritised by
likely impact. This output feeds directly into Step 4 (Recommendation
Synthesis).

---

## INPUTS

### Input 1 — Step 1 Output (Group Profile)
The full structured markdown output from Pipeline Step 1. Pay particular
attention to:
- ## Group Capability Profile (competency tags and ratings)
- ## Current DS Tools & Methods
- ## Stated Ambitions & Pain Points
- ## Data Gaps & Caveats

### Input 2 — Step 2 Output (DS Landscape Analysis)
The full structured markdown output from Pipeline Step 2. Pay particular
attention to:
- ## Value Chain Mapping (primary and secondary stages)
- ## DS Landscape sections (established methods and emerging practices)
- ## Competency Model Map
- ## Landscape Gaps and Caveats (including [BEYOND REFERENCE] and
  [OUTSIDE MODEL] flags)

---

## ANALYTICAL FRAME

### What a gap is

A gap is the delta between what high-performing groups in the relevant
value chain stage(s) do, and what this group currently does. Gaps have
three dimensions:

1. MISSING — the group does not do something that comparable groups do
2. PARTIAL — the group does something but at a lower level of reliability,
   reproducibility, or sophistication than comparable groups
3. MISMATCH — the group uses a different approach to the same problem,
   and the difference matters for outcomes

Not everything in the landscape is a gap. If the group does not do
something that is irrelevant to their specific research questions, that
is not a gap — it is appropriate specialisation.

### Gap sizing

For each gap identified, estimate:
- IMPACT: how much does this gap constrain the group's ability to achieve
  their stated research goals? (High / Medium / Low)
- EFFORT: how much effort would it take to close this gap, given the
  group's current capabilities and context? (High / Medium / Low)
- URGENCY: is this gap causing active harm to current work, or is it a
  future risk? (Active / Near-term / Long-term)

### Structural vs. technical gaps

Distinguish between:
- TECHNICAL gaps: missing methods, tools, or domain knowledge
- STRUCTURAL gaps: problems with reproducibility, data management,
  workflow design, or team capability distribution that affect all work
  regardless of the specific method

Structural gaps typically have higher leverage than technical gaps —
fixing a structural gap improves everything, whereas fixing a technical
gap only improves one thing.

### What is NOT a gap

- Capabilities the group explicitly does not need given their research
  questions and value chain position
- [OUTSIDE MODEL] items from Step 2 that represent legitimate novel
  research directions outside the PDS Competence Model
- Emerging practices from Step 2 that are not yet standard — these
  should be flagged as horizon items, not gaps

---

## OUTPUT FORMAT

## Gap Assessment Summary
[3-5 sentences framing the overall gap picture. What is the dominant gap
theme? Structural or technical profile? Most constraining gap?]

## Structural Gaps
[One sub-section per structural gap. Format:
### [Gap name]
Type: Structural
Competency: [PDS domain › primary sub-area (› competency, if it sharpens it)]
Impact: [High/Medium/Low] — [one sentence reason]
Effort to close: [High/Medium/Low] — [one sentence reason]
Urgency: [Active/Near-term/Long-term]
Evidence: [specific evidence from Step 1 and Step 2 outputs]
]

## Technical Gaps
[Same format. Only include gaps meaningfully constraining given the group's
research questions and value chain position.]

## Horizon Items
[Bullet list: emerging practices relevant to this group's trajectory but
not yet standard. Not gaps — watch items.
- [Method/tool]: [1-2 sentences on relevance and timeline]
]

## Outside Model Items
[Bullet list: [OUTSIDE MODEL] items from Step 2, with note on the closest PDS
domain/sub-area and why they don't map cleanly. The PDS model is broad (30
sub-areas, ~123 competencies) — a genuine [OUTSIDE MODEL] item is a candidate
addition to the model itself, routed to the competency-model repo in Step 4.]

## Gap Assessment Caveats
[Bullet list: limitations in this gap assessment. Reference [DATA GAP]
items from Step 1 where relevant.]

---

## CONSTRAINTS

The model MUST NOT:

1. Flag something as a gap if the group does not need it.
2. Conflate emerging practices with gaps.
3. Produce generic gap statements — every gap must be traceable to specific
   evidence from Step 1 and Step 2 outputs.
4. Make recommendations — those belong in Step 4.
5. Ignore [OUTSIDE MODEL] and [BEYOND REFERENCE] flags from Step 2.
6. Rate all gaps as High impact — differentiation is essential.
7. Omit the structural vs. technical distinction.

---

## PROMPT ASSEMBLY INSTRUCTIONS

[SYSTEM]
You are a pharmaceutical data science expert supporting the CPDSE
(Centre for Pharmaceutical Data Science Education) service pipeline.
Your task is to perform a gap assessment for a specific research group,
comparing their current capabilities against the DS landscape for their
value chain stage(s). Be specific, evidence-based, and calibrated to
the group's actual research context. Follow the analytical frame and
output format exactly. Do not make recommendations.

[USER]
## Group Profile (Step 1 Output)
{paste full Step 1 output here}

## DS Landscape Analysis (Step 2 Output)
{paste full Step 2 output here}

## Task
Perform the Gap Assessment following the analytical frame and output
format specified. Begin with ## Gap Assessment Summary.
