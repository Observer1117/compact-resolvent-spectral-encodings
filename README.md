# A Layered Framework for Compact-Resolvent Spectral Encodings

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](#versioning)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-green)](LICENSE)
[![Status: expository preprint](https://img.shields.io/badge/status-expository%20preprint-orange)](#scientific-status)

This repository contains the manuscript, source, metadata, and referee-hardening audit for an expository operator-theoretic framework separating several notions that are often conflated in spectral discussions:

- compactness of a carrier;
- compact resolvent of an operator;
- trace-class heat evolution;
- abstract diagonal realizability;
- elliptic-geometric realizability;
- equivariant labels and physical interpretation.

Author: Stassis Stashkevichyus, Independent Researcher. ORCID: [0009-0000-2294-705X](https://orcid.org/0009-0000-2294-705X). Contact: [theobserver.of.multiverses@proton.me](mailto:theobserver.of.multiverses@proton.me).

Canonical repository: [Observer1117/compact-resolvent-spectral-encodings](https://github.com/Observer1117/compact-resolvent-spectral-encodings).

## Scientific status

This is an **expository framework preprint**. It systematizes standard results from operator theory, heat-kernel theory, harmonic analysis, and compact-group representation theory. It does **not** claim a new general theorem in spectral geometry, a physical compactification model, or an inverse spectral theorem. It has not been peer reviewed.

## Main contents

The manuscript:

1. distinguishes compact carrier, compact resolvent, and heat-admissibility;
2. defines the spectral counting measure and complex-time heat trace;
3. states elementary holomorphy, differentiation, domination, and periodicity criteria with explicit hypotheses;
4. separates formal, analytic, abstract diagonal, elliptic-geometric, equivariant, and physical realization levels;
5. gives circle and flat-torus theta examples;
6. records counterexamples to common invalid implications;
7. formulates an audit protocol for proposed spectral encodings.

## Files

- [`paper/compact_resolvent_spectral_encodings_v0_2.pdf`](paper/compact_resolvent_spectral_encodings_v0_2.pdf) — current manuscript.
- [`source/main.tex`](source/main.tex) — self-contained LaTeX source.
- [`audit/referee_audit_v0_2.md`](audit/referee_audit_v0_2.md) — proof and bibliography ledger.
- [`metadata/publication_metadata.yaml`](metadata/publication_metadata.yaml) — canonical structured metadata.
- [`metadata/citation.bib`](metadata/citation.bib) — BibTeX citation record.
- [`metadata/osf_registration_metadata.md`](metadata/osf_registration_metadata.md) — copy-ready OSF fields.
- [`metadata/release_notes_v0.2.0.md`](metadata/release_notes_v0.2.0.md) — GitHub Release text.
- [`metadata/metadata_audit.md`](metadata/metadata_audit.md) — consistency and unresolved-field audit.
- [`metadata/build_environment.txt`](metadata/build_environment.txt) — verified build environment and result.
- [`checksums/SHA256SUMS`](checksums/SHA256SUMS) — integrity manifest.

## Build

Requirements: PDFLaTeX with the standard packages listed in `source/main.tex`. The package was reproduced byte-for-byte with TeX Live 2023; the earlier arXiv-compatibility audit targeted TeX Live 2025.

```bash
cd source
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Without `latexmk`, run `pdflatex` twice:

```bash
cd source
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Citation

Until an OSF Registration DOI is assigned, cite the versioned manuscript:

> Stashkevichyus, Stassis. (2026). *A Layered Framework for Compact-Resolvent Spectral Encodings* (Version 0.2). Expository framework preprint.

Machine-readable citation metadata are available in [`CITATION.cff`](CITATION.cff) and [`metadata/citation.bib`](metadata/citation.bib). After DOI assignment, the DOI must be added to both files without changing the scientific content of v0.2.

## Reporting errors

Use the issue templates for either a mathematical error or a bibliographic/typographical correction. A GitHub issue is public error reporting, not peer review.

## Versioning

- `v0.2.x`: metadata, packaging, or typographical corrections that do not change mathematical content;
- `v0.3`: changed definitions, statements, proofs, or substantial exposition;
- `v1.0`: reserved for a version hardened after independent external mathematical review.

## License

The manuscript, LaTeX source, metadata, and documentation are licensed under [Creative Commons Attribution 4.0 International](LICENSE).
