# Case study: CSP systematic review and meta-analysis

The platform was first developed for a conduction-system pacing (CSP) systematic review and meta-analysis. It began as a CSP-specific evidence database and workflow, then became the foundation for the reusable multi-project platform.

## Verified project scale

The current research database contains **709 active article/source-report records**.

Structured scientific data have been extracted from retained source text, including abstracts or full text where available, for **417 studies**. The current CSP evidence includes 1,499 outcome records, 1,351 baseline-characteristic records, 2,192 lead/device measurements, 1,790 clinical-event records and 482 effect-size records. These counts exclude universal observation rows that are migration copies of existing CSP evidence.

A PubMed deduplication check detected 4 duplicate records, leaving 521 unique PubMed records in that import set.

## How the CSP workflow was used

A researcher defines the systematic-review/meta-analysis question and the information that needs to be collected. The AI client can then help translate the approved search requirements into database-specific literature searches, while the backend stores the returned records and retained source material.

After screening, the retained papers are processed study by study and report by report. The extraction workflow reads the available article text, tables and supplements and proposes structured scientific data with source quotations and locations. Those records are stored in the evidence database for review rather than written directly into the final Excel output.

The CSP project therefore exercised the full workflow:

`literature search/import → deduplication and screening → retained sources → structured extraction → human review → curated evidence → analysis → Excel/CSV and forest-plot outputs`

## What the platform handles

### Screening and study/report management

The platform keeps the literature records associated with the project, supports screening workflows, and distinguishes a scientific study from the individual papers or reports that may come from that study. This matters because one trial can have a primary publication, follow-up papers or supplementary reports without representing separate independent studies.

### Study quality and risk-of-bias assessment

After studies are selected, the platform also supports the part of a systematic review where researchers assess how trustworthy each study is. It can record the study design, link the study to the appropriate appraisal or risk-of-bias framework, keep the source evidence used for each assessment, preserve reviewer judgements and disagreements, and export the final approved assessment.

The software organizes and audits this process. The AI can help find or structure the supporting evidence, but the final appraisal and risk-of-bias judgement remains a human scientific decision.

### Statistical analysis and forest plots

The software contains deterministic statistical-analysis code rather than asking the language model to calculate the meta-analysis. It supports calculations such as confidence intervals and effect estimates, including paired pre/post handling when the required uncertainty information is available. Compatible study effects can be pooled by the analysis layer, and the system can generate forest plots together with the included/excluded evidence log and CSV/Excel analysis files.

The current database does not yet contain a validated completed meta-analysis artifact. Historical forest-plot render files exist, but they are development outputs rather than a completed scientific result, so this public case study does not present them as validated meta-analysis findings.

The exact statistical choices and analysis protocol used for the private CSP review are not disclosed in this public release.

## What was generalized

The existing CSP dataset was kept in place while the reusable parts of the system were separated from CSP-specific scientific fields.

In practical terms:

- each research project can define its own scientific variables, groups, outcomes and extraction requirements;
- studies, reports, retained sources and evidence provenance can be managed in the same way across projects;
- review and audit history can be preserved consistently across projects;
- statistical analysis can use a project- and analysis-specific set of eligible evidence rather than automatically using every stored value.

This meant the CSP review did not have to be rebuilt when the same core platform was later reused for zebrafish CRISPR evidence.

## Private protocol boundary

This public release describes the software workflow only. It does not disclose the CSP search strategy, eligibility criteria, outcome definitions, subgroup rules, appraisal configuration, statistical-analysis decisions, extracted evidence, results or research deliverables.

The CSP project is included here as the origin of the platform, not as a public release of its scientific protocol.
