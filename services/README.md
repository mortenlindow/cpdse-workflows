# CPDSE Services — customer-facing workflow types

CPDSE's customer-facing work is organised into **three workflow types**. Each type
serves a distinct customer, but all reuse the same three reference models
(*Where × What × How* — see [`../reference/README.md`](../reference/README.md)).

| Type | Customers | Workflows | Status |
|---|---|---|---|
| **Research** | researchers, research groups, departments | Research & DS Strategy · Specific Research Consulting | 1 built, 1 in design |
| **Educational** | teachers, course owners, curriculum leaders, and their staff | Course Upgrade · Staff Upskilling · New Course Creation | in design |
| **Internal self-improvement** | CPDSE itself | onboarding · infrastructure building | stub |

## Research
Customers who *do research* and want to use pharmaceutical data science better.

- **Research & DS Strategy** — fixed-scope diagnostic engagement (AI pipeline +
  2 workshops → strategy brief). **Built.** Lives at
  [`01-research-strategy/`](01-research-strategy/).
- **Specific Research Consulting** — time-based engagement on a concrete research
  question. *In design.*

## Educational
Customers who *teach* and want more (and better) PDS in their teaching — plus
upskilling for the staff who deliver it.

- **Course Upgrade** — add modern PDS to an existing course. *In design.*
- **Staff Upskilling** — build new PDS skills in teaching staff. *In design.*
- **New Course Creation** — design a new PDS-rich course (often CPDSE-initiated).
  *In design.*

See [`educational/`](educational/).

## Internal self-improvement
Not customer-facing. How CPDSE improves *itself* — consultant onboarding and the
building of shared infrastructure (this very project is an example). Deliberately
a **stub** for now. See [`internal/`](internal/).

---

> **Note (transitional):** under the current "light-touch" layout, the built
> Research workflow stays at top level (`01-research-strategy/`) rather than under
> a `research/` folder. If the portfolio grows, fold it into `research/` alongside
> the others. The five customer journeys behind these types are detailed in
> [`../reference/cpdse-value-stream-v0.1.0.md`](../reference/cpdse-value-stream-v0.1.0.md).
