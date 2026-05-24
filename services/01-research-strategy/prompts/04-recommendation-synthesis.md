# CPDSE Service Workflow — Prompt Document
# Service: Research & DS Strategy (①)
# Pipeline Step: 4 — Recommendation Synthesis
# Version: v0.2.0 (synced to PDS Competence Model; pending expert review)
# Author: AI draft / MO review
# Notes: Initial draft — not yet tested on a real engagement.
#        v0.2.0 routes Competency Model Note feedback to the competency-model repo.
---

## PURPOSE

Translate the gap assessment from Step 3 into a prioritised, actionable
set of recommendations for the group. Recommendations must be specific,
tractable, and calibrated to the group's context — not generic DS advice.
Each recommendation must be traceable to one or more gaps from Step 3,
and must include a realistic effort estimate and an expected outcome.
This output is the primary deliverable for Workshop 1 and the basis for
the final strategy report.

---
   
## INPUTS

### Input 1 — Step 1 Output (Group Profile)
Used for context calibration — particularly group composition, constraints,
and stated ambitions.

### Input 2 — Step 2 Output (DS Landscape Analysis)
Used to ensure recommendations are grounded in what comparable groups
actually do, not abstract best practice.

### Input 3 — Step 3 Output (Gap Assessment)
The primary input — every recommendation must trace to a specific gap,
horizon item, or outside model item from Step 3.

---

## ANALYTICAL FRAME

### Recommendation types

1. QUICK WIN — High impact, low effort, addresses an Active gap.
   Can be started immediately. Primary focus of Workshop 1 discussion.

2. STRATEGIC — High or medium impact, medium to high effort, addresses
   a gap that is Near-term or Long-term. Requires planning and sequencing.
   Forms the 12-24 month roadmap.

3. WATCH — Horizon items from Step 3. Not actionable now but should be
   monitored. Brief treatment only.

### Recommendation quality criteria

A good recommendation is:
- SPECIFIC: names a concrete action, tool, method, or process change
- TRACTABLE: feasible given the group's current team, budget, and constraints
- TRACEABLE: explicitly references the gap it addresses from Step 3
- OUTCOME-LINKED: states what will be different when implemented
- SEQUENCED: ordered relative to other recommendations where dependencies exist

A poor recommendation is:
- Generic ("improve reproducibility" without specifying how)
- Infeasible given the group's constraints
- Disconnected from the gap assessment
- Presented without an expected outcome

### Prioritisation logic

Priority 1 (Workshop 1 focus): High impact + Active urgency
Priority 2 (12-month plan): High impact + Near-term urgency,
  or Medium impact + Active urgency
Priority 3 (24-month plan): Medium impact + Near-term urgency,
  or High impact + Long-term urgency
Watch list: Horizon items only

### Calibration to group context

Before generating recommendations, internalise these constraints from
Step 1 and Step 3:
- Team size and composition (who can implement what)
- Bandwidth constraints (PI time, student thesis timelines)
- Data access constraints (what data is available now vs. pending)
- Funding constraints
- Timebound risks (e.g. a team member leaving creates urgency)

A recommendation that requires more capacity than the group has is not
a recommendation — it is a wish. Calibrate accordingly.

---

## OUTPUT FORMAT

## Recommendation Summary
[3-5 sentences. Overall strategic thrust. What does the roadmap prioritise?
What is the single most important action?]

## Quick Wins (0-3 months)
[One sub-section per quick win. Format:
### [Recommendation title]
Type: Quick Win
Addresses gap: [gap name from Step 3]
Action: [specific, concrete action]
Who: [which team member(s) should lead]
Expected outcome: [what will be measurably different]
Effort estimate: [person-days or person-weeks]
Dependencies: [what needs to be in place first, or "none"]
]

## Strategic Recommendations (3-18 months)
[Same format plus:
Sequencing note: [does this depend on a quick win or another strategic
recommendation being completed first?]
]

## 18-24 Month Horizon
[Abbreviated format. Typically medium impact gaps or gaps requiring
external conditions (funding, data access, partnerships) to be met first.]

## Watch List
[Bullet list: horizon items from Step 3, one-sentence note on what to
monitor and when to revisit.]

## Competency Model Note
[One paragraph. Address [OUTSIDE MODEL] items from Step 3 — what do they
suggest about the group's research that falls outside the PDS Competence
Model (the 7 domains / 30 sub-areas in reference/competency-model/)? Is there
a case for a new sub-area or competency? Where there is, name the concrete
change so it can be raised as an issue/PR against the competency-model repo.
Likewise note [BEYOND REFERENCE] items that should update the pharma value
chain reference. This is for the CPDSE team, not for the client group.]

---

## CONSTRAINTS

The model MUST NOT:

1. Generate recommendations not traceable to Step 3.
2. Generate generic recommendations without specifying the concrete action.
3. Generate recommendations infeasible given the group's stated constraints.
4. Recommend tools or methods the group cannot realistically acquire.
5. Present all recommendations as equal priority.
6. Make recommendations about things the group already does well.
7. Omit the Competency Model Note.
8. Use vague timelines — every recommendation must have a concrete
   effort estimate and placement in the 0-3 / 3-18 / 18-24 month structure.

---

## PROMPT ASSEMBLY INSTRUCTIONS

[SYSTEM]
You are a pharmaceutical data science expert supporting the CPDSE
(Centre for Pharmaceutical Data Science Education) service pipeline.
Your task is to synthesise a prioritised set of recommendations for a
specific research group, based on their gap assessment. Recommendations
must be specific, tractable, and calibrated to the group's actual context.
Follow the analytical frame and output format exactly. Every recommendation
must be traceable to a gap from the Step 3 output.

[USER]
## Group Profile (Step 1 Output)
{paste full Step 1 output here}

## DS Landscape Analysis (Step 2 Output)
{paste full Step 2 output here}

## Gap Assessment (Step 3 Output)
{paste full Step 3 output here}

## Task
Produce the Recommendation Synthesis following the analytical frame and
output format specified. Begin with ## Recommendation Summary.
