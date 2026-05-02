# Changelog

All notable changes to this dataset will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## \[1.0.0] — YYYY-MM-DD

Initial release. First publication of the KPI Comparison Matrix
deliverable of the 2026–2029 plan, prior to the parallel release of the
companion Python library `arid-resilience-kpis`.

### Added

* 17 KPIs documented across three tiers (CORE, EXTENSION, EXPLORATORY).
* Single source of truth: `kpi\\\\\\\\\\\\\\\_definitions.py`.
* Generated artefacts: `data/kpi\\\\\\\\\\\\\\\_comparison\\\\\\\\\\\\\\\_matrix.csv`,
`data/kpi\\\\\\\\\\\\\\\_comparison\\\\\\\\\\\\\\\_matrix.xlsx` (3 sheets: README, KPI matrix, Tier legend).
* Companion descriptive document: `README.md`.
* Build script: `build\\\\\\\\\\\\\\\_matrix.py` (regenerates CSV and XLSX from the source of truth).
* Reproducibility: `Makefile` with `make all`.

### Released formats

* CSV (UTF-8, RFC 4180-compliant, semicolon-free): the citable dataset.
* XLSX with formatting and tier-based colour coding: human-readable companion.
* Markdown + PDF: descriptive document explaining structure, motivation, limitations and rationale for regional extensions.

### Coverage

* Annex 80 indicators (IOD, AWD, CCOR, UDH, BCVF, HE).
* Sensitivity, passive performance, resilience and hygrothermal stability extensions.
* Composite Arid Climate Resilience Score (ACRS) with entropy weighting.

### Notes

* DOI placeholder pending Zenodo release.
* Repository URL: `https://github.com/gbarea-INAHE/kpi-comparison-matrix`
* Designed to be consumed by the `arid-resilience-kpis` Python library
(Sprint 2 deliverable).

