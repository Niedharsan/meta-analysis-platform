# Case study: zebrafish CRISPR meta-analysis

The zebrafish CRISPR meta-analysis was the second real scientific use of the platform. It was used to test whether a system originally built around a clinical systematic review could support a very different molecular-biology evidence problem without creating a separate application from scratch.

## Verified project scale

The current research database contains **8,952 active article/source-report records**.

Structured CRISPR data have been extracted from retained article text and structured sources such as tables or supplements, including abstract-level sources where full text was unavailable. The current evidence includes **18,528 normalized guides, 22,928 guide-to-report records, 4,812 experiments and 3,998 measurements**.

A complete repeat ZFIN import detected all 3,230 existing study records as duplicates and created no additional studies, confirming that the import path was deduplicating rather than duplicating the corpus.

The project also retains **6,149 physical source files** (about 14.9 GB), linked through the source-asset layer.

## What changed for the CRISPR project

The shared platform already handled projects, literature records, retained source material, provenance, review state and exports. The CRISPR project added domain-specific scientific records for:

- CRISPR guides and reported guide sequences;
- experiments;
- guide-to-experiment relationships;
- measurements and reported outcomes.

The extraction workflow can process both narrative text and structured material such as article tables and supplements. Extracted guide, experiment and measurement records remain linked to the paper/report and source evidence from which they came.

## CRISPR-specific evidence handling

The CRISPR layer distinguishes different types of reported evidence rather than treating every percentage as the same result. For example, editing or indel measurements, phenotype outcomes, germline transmission and knock-in outcomes remain separate scientific measurements.

Safeguards include:

- missing measurements are not converted to zero;
- a genuine reported zero is kept distinct from missing, not tested, not reported or failed-assay states;
- multiplex outcomes are not automatically copied to individual component guides;
- reported guide sequences are preserved rather than silently inferred or rewritten;
- evidence remains linked to its source;
- automated specialist and verifier roles can check extraction quality but cannot approve their own output as accepted scientific evidence.

## What this use case demonstrated

The important result was architectural reuse. A clinical systematic review and a zebrafish CRISPR evidence project require very different scientific fields, but they can still share the same underlying workflow for:

`literature and sources → structured extraction → provenance → review → curated evidence → project exports`

The CRISPR-specific records were added on top of that shared infrastructure rather than building another independent literature/extraction system.

## Public boundary

This public case study describes the implemented workflow, verified project scale and safeguards only. It does not publish the CRISPR extraction registry, production prompts, source corpus, validation datasets, live scientific values or research results.
