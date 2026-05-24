# CPDSE Service Workflows
Version: v0.1.0 | Last updated: 2026-04-25

## Structure

```
cpdse-service-workflows/
  README.md                            ← this file
  engagement-log.md                    ← all engagements, prompt versions
  services/
    01-research-strategy/
      intake-questionnaire-blank-v0.1.0.txt
      prompts/
        01-group-profile-synthesis.md  ← Step 1 prompt
        02-ds-landscape-analysis.md    ← Step 2 prompt
        03-gap-assessment.md           ← Step 3 prompt
        04-recommendation-synthesis.md ← Step 4 prompt
      output-templates/
        workshop1-miro-frames.pdf      ← 4-frame PDF for Miro import
        workshop1-facilitation-guide.docx ← consultant session script
  reference/
    competency-model/                  ← PDS Competence Model (git submodule)
    pharma-value-chain-model/          ← Pharma Value Chain Model (git submodule)
  engagements/
    ENG001-MortenLindow/
      intake-questionnaire-ENG001-SIM.txt
      step3-gap-assessment-ENG001-SIM.md
      step4-recommendation-synthesis-ENG001-SIM.md
      strategy-brief-ENG001-SIM.docx  ← client-facing brief
```

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

## Prompt versioning

All prompt documents are versioned independently. When updating a prompt,
increment the version number and log it in engagement-log.md.
The engagement log maps each engagement to the prompt versions used,
ensuring reproducibility.

## Status

All prompt documents are v0.1.0 AI-drafted, pending expert review before
first real engagement. ENG001-SIM is a simulated test engagement only.
