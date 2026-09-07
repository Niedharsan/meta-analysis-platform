# Case study: CSP systematic review and meta-analysis

The platform was first developed for a conduction-system pacing (CSP) systematic review and meta-analysis. It began as a CSP-specific evidence database and workflow, then became the foundation for the reusable multi-project platform.

## How the CSP workflow was used

A researcher defines the systematic-review/meta-analysis question and the information that needs to be collected. The AI client can then help translate the approved search requirements into database-specific literature searches, while the backend stores the returned records and retained source material.

After screening, the retained papers are processed study by study and report by report. The extraction workflow reads the available article text, tables and supplements and proposes structured scientific data with source quotations and locations. Those records are stored in the evidence database for review rather than written directly into the final Excel output.

The CSP project therefore exercised the full workflow:

`literature search/import → deduplication and screening → retained sources → structured extraction → human review → curated evidence → analysis → Excel/CSV and forest-plot outputs`

## What the platform handles

### Screening and study/report management

The platform keeps the literature records associated with the project, supports screening workflows, and distinguishes a scientific study from the individual papers or reports that may come from that study. This matters because one trial can have a primary publication, follow-up papers or supplementary reports without representing separate independent studies.

### Evidence review and provenance

AI-extracted values enter as proposed evidence. The system keeps each value linked to its study/report and source evidence, and records the review history when a researcher accepts, rejects or corrects it.

### Study appraisal and risk of bias

The platform also contains workflow support for study-design classification, appraisal/risk-of-bias tools, source-backed reviewer assessments, review history and consensus/export checks. These are controlled review workflows: the AI can help prepare or inspect evidence, but the scientific judgement and approval remain attributable to human reviewers.

### Statistical analysis and forest plots

Yes — the software contains deterministic statistical-analysis code rather than asking the language model to calculate the meta-analysis. It supports calculations such as confidence intervals and effect estimates, including paired pre/post handling when the required uncertainty information is available. Compatible study effects can be pooled by the analysis layer, and the system can generate forest plots together with the included/excluded evidence log and CSV/Excel analysis files.

The exact statistical choices and analysis protocol used for the private CSP review are not disclosed in this public release.

## What was generalized

The original CSP records were retained rather than being discarded and rebuilt. Shared concepts were then added around them so that other projects could reuse the same infrastructure.

In practical terms:

- each research project can have its own scientific configuration and extraction requirements;
- common concepts such as studies, reports, variables, groups, measurements/effect estimates and source evidence can be reused across projects;
- provenance records where scientific values came from;
- review history records what was accepted, rejected or corrected;
- an approved scientific value can still be included or excluded differently for a particular analysis, rather than being automatically used in every meta-analysis.

This allowed the CSP review to remain intact while the same core platform was later reused for zebrafish CRISPR evidence.

## Private protocol boundary

This public release describes the software workflow only. It does not disclose the CSP search strategy, eligibility criteria, outcome definitions, subgroup rules, appraisal configuration, statistical-analysis decisions, extracted evidence, results or research deliverables.

The CSP project is included here as the origin of the platform, not as a public release of its scientific protocol.
