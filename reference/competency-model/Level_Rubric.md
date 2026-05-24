# PDS Competence Model — Level Rubric (L1–L5)

A single behavioral rubric that applies to **every** competency. Per-competency entries should write *one indicator sentence per level* using the verbs and artifacts below — not freshly invented adjectives. If you can't write a concrete indicator at a given level, that's a signal the level either doesn't apply to that competency (mark `—`) or that the competency needs sharpening.

The rubric is built around four dimensions that move together as level rises:

| Dimension              | L1            | L2              | L3              | L4              | L5                |
|------------------------|---------------|-----------------|-----------------|-----------------|-------------------|
| **Autonomy**           | needs guidance every step | works from a template with a mentor available | works independently on standard problems | works independently on non-standard problems | sets the team's standards |
| **Context**            | toy / textbook examples | small slice of real pharma data | end-to-end on a real pharma project | messy, unfamiliar, multi-source pharma data | shapes which problems get tackled at all |
| **Judgment**           | recognizes the concept | follows a recipe | chooses among known methods | weighs trade-offs, knows when to break the recipe | defines what "good" looks like for the field |
| **Effect on others**   | learning from others | asks good questions | delivers usable work | reviews and unblocks peers | teaches, mentors, publishes, or open-sources |

---

## L1 — Awareness

> *Recognizes the concept when it shows up. Cannot yet do it.*

A person at L1 can:

- **Recognize** the concept in someone else's work or in a paper, slide, or repo.
- **Define** it in plain language and **give an example** from a pharma context.
- **Identify** when a colleague's task touches this competency ("that's a survival analysis question").
- **Read** code or output that uses it and follow what is happening at a high level.

Cannot yet: produce work in this area without close guidance.

**Promotion signal to L2:** has completed a guided exercise (course, tutorial, paired session) end-to-end.

---

## L2 — Familiarity

> *Can do the task with a template, a tutorial, or someone to ask.*

A person at L2 can:

- **Apply** a worked example or template to a small slice of real data.
- **Modify** a known recipe (change a parameter, swap a column, adjust a filter) and predict the result.
- **Spot** when their attempt is going wrong, even if they can't always fix it alone.
- **Ask** specific, well-formed questions when stuck (not "it doesn't work" but "the model returns NaN when the dose column has zeros").

Cannot yet: choose between methods on their own, or handle data that doesn't match the template.

**Promotion signal to L3:** has independently delivered usable output on a real pharma problem they hadn't seen a template for.

---

## L3 — Proficiency

> *Independently delivers usable work on standard pharma problems.*

L3 is the **target working level** and the reference line on the radar. It is not an expectation that every person reaches L3 in every competency — most people will be at L3 in a *subset* of competencies that matches their role and lower in the rest, and that is fine. L3 describes what proficiency looks like *when present*, not where everyone must be.

A person at L3 can:

- **Plan and execute** the work on a standard problem without supervision: scoping, choosing a method, implementing, validating, documenting.
- **Choose** between common methods and justify the choice in writing or to a colleague.
- **Diagnose** the usual failure modes (missing data, miscoded variables, leakage, overfitting, biased samples) and fix them.
- **Produce** an artifact a peer can pick up and run: a reproducible notebook, a tested script, a written analysis with assumptions stated.
- **Review** a peer's L1/L2 work and give actionable feedback.

Cannot yet (reliably): handle problems where the standard recipes don't apply, or notice when a non-standard situation is hiding behind a standard-looking one.

**Promotion signal to L4:** has handled at least one problem where the obvious approach didn't work, recognized that, and chosen a different one with a defensible reason.

---

## L4 — Mastery

> *Handles non-standard cases and is the person others escalate to.*

A person at L4 can:

- **Recognize** when a problem is *not* standard — when the assumptions of the usual method are violated, when the data has structure the recipe doesn't account for — and adjust before producing wrong answers.
- **Adapt or combine** methods across competencies (e.g. blending causal inference with survival analysis, or feature engineering driven by domain knowledge of PK/PD).
- **Trade off** competing constraints (statistical rigor vs. regulatory deadlines, interpretability vs. accuracy, sample size vs. measurement quality) and explain the trade-off to a non-technical stakeholder.
- **Lead** a small piece of work end-to-end: scope it, break it down, review the team's output, sign off on quality.
- **Detect bullshit** — recognize when a tool, paper, or vendor claim doesn't hold up against the data.

Cannot yet (necessarily): change what the broader team or field considers good practice.

**Promotion signal to L5:** has changed how others work — through teaching, a published method, an internal standard, or an open-source contribution that others adopted.

---

## L5 — Expertise

> *Sets the standard. Others learn this competency from them.*

A person at L5 can:

- **Define** what "good" looks like for this competency in a pharma context, in writing, and have peers adopt it.
- **Teach** the competency: train colleagues, design curriculum, write guides that get reused.
- **Innovate**: publish, contribute to open-source tools, propose new methods, or run a research programme.
- **Spot the next problem** before it becomes urgent — know which methods are aging out and which are emerging.
- **Represent** the organization externally on this topic (conference, regulator, cross-pharma working group).

L5 is rare and is not required at the role level for most competencies. A senior data scientist will have L5 in a handful of competencies, L4 in several, L3 in most, and lower in some — that's normal.

---

## How to write a competency entry against this rubric

For each numbered competency, write five short lines like this (in a real entry this block sits inside its sub-area's header — see *How tools and pharma examples fit in* below):

```
Algorithmic Thinking
  L1 — recognize loops, conditionals, and recursion in someone else's code
  L2 — translate a worked algorithm (e.g. cohort matching) into Python or R from a tutorial
  L3 — design a clear algorithm for a new pharma task (e.g. dedup adverse event records) and implement it
  L4 — analyze the complexity of an algorithm on a real dataset and choose a better one when the obvious choice is too slow
  L5 — design algorithms that the team adopts as a standard pattern, or contribute one to an open-source pharma toolkit
```

Rules:

- **One sentence per level.** No bullet lists, no Tools/Pharma Examples sub-blocks.
- **Start with a verb.** If the verb is "understand", "be aware of", "appreciate", rewrite it. Use: recognize, apply, choose, design, implement, diagnose, adapt, lead, teach, define.
- **Name an artifact or observable.** "Can do regression" is too vague; "fits and validates a regression on a real trial dataset and reports assumption checks" is testable.
- **Use `—` if a level genuinely doesn't apply.** Better than filler. If you find yourself writing `—` at L4 and L5 for many competencies in a sub-area, the sub-area itself is probably L1–L3 in nature, and that's useful information.

---

## How tools and pharma examples fit in

Don't repeat them per level, and don't repeat them per competency either. Pool them at the **sub-area** level, with one header block per sub-area that covers all its competencies:

```
Computational Thinking          ← sub-area
  Typical stack: base R, Python stdlib, dplyr, purrr; SciPy, NumPy at higher levels.
  Pharma examples:
    - Cohort matching in pharmacovigilance       (Algorithmic Thinking @ L3)
    - Real-time PK processing from wearables     (Algorithmic Thinking @ L4)
    - ETL pipelines for clinical trial data      (Functional Thinking @ L3)
    - Quantum-inspired molecular simulation      (Complexity Theory @ L5)

  Algorithmic Thinking
    L1 — recognize loops, conditionals, and recursion in someone else's code
    L2 — translate a worked algorithm into Python or R from a tutorial
    L3 — design a clear algorithm for a new pharma task and implement it
    L4 — analyze complexity on a real dataset and choose a better algorithm when needed
    L5 — design algorithms the team adopts as standard, or contribute to an open-source pharma toolkit

  Functional Thinking
    L1 — …
    …

  Complexity Theory
    L1 — …
    …
```

Why sub-area pooling: tools and pharma scenarios almost always span several sibling competencies in the same sub-area, and per-competency repetition is exactly what produced the placeholder filler in the first draft. Pooling forces examples to be specific enough to anchor more than one competency, and tagging each example with `competency @ level` keeps the link traceable.
