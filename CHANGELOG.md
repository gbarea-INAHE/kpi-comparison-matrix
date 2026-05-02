# Changelog

All notable changes to this dataset will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-05-02

Initial release. First publication of the KPI Comparison Matrix
deliverable of the 2026–2029 plan, prior to the parallel release of the
companion Python library `aridkpi`.

**DOI:** [10.5281/zenodo.19964373](https://doi.org/10.5281/zenodo.19964373)
**Concept DOI (always latest):** [10.5281/zenodo.19964372](https://doi.org/10.5281/zenodo.19964372)

### Added

- 17 KPIs documented across three tiers (CORE, EXTENSION, EXPLORATORY).
- Single source of truth: `kpi_definitions.py`.
- Generated artefacts: `data/kpi_comparison_matrix.csv`,
  `data/kpi_comparison_matrix.xlsx` (3 sheets: README, KPI matrix, Tier legend).
- Companion descriptive document: `README.md`.
- Build script: `build_matrix.py` (regenerates CSV and XLSX from the source of truth).
- Reproducibility: `Makefile` with `make all`.

### Released formats

- CSV (UTF-8, RFC 4180-compliant, semicolon-free): the citable dataset.
- XLSX with formatting and tier-based colour coding: human-readable companion.
- Markdown + PDF: descriptive document explaining structure, motivation, limitations and rationale for regional extensions.

### Coverage

- Annex 80 indicators (IOD, AWD, CCOR, UDH, BCVF, HE).
- Sensitivity, passive performance, resilience and hygrothermal stability extensions.
- Composite Arid Climate Resilience Score (ACRS) with entropy weighting.

### Notes

- Designed to be consumed by the `aridkpi` Python library
  (Sprint 2 deliverable, forthcoming).
- Indexed in OpenAIRE and archived in Software Heritage.
