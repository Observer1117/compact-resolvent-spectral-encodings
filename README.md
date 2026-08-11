# A Layered Framework for Compact-Resolvent Spectral Encodings

[![Metadata revision](https://img.shields.io/badge/metadata-v0.2.1-blue)](#metadata-status)
[![Frozen release](https://img.shields.io/badge/archive-v0.2.0-lightgrey)](#metadata-status)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-green)](LICENSE)
[![Status: expository preprint](https://img.shields.io/badge/status-expository%20preprint-orange)](#scientific-status)
[![DOI](https://img.shields.io/badge/DOI-10.17605%2FOSF.IO%2FRWPGA-blue)](https://doi.org/10.17605/OSF.IO/RWPGA)

This repository contains the manuscript, source, metadata, and referee-hardening audit for an expository operator-theoretic framework separating several notions that are often conflated in spectral discussions:

- compactness of a carrier;
- compact resolvent of an operator;
- trace-class heat evolution;
- abstract diagonal realizability;
- elliptic-geometric realizability;
- equivariant labels and physical interpretation.

Author: Stassis Stashkevichyus, Independent Researcher. ORCID: [0009-0000-2294-705X](https://orcid.org/0009-0000-2294-705X). Contact: [theobserver.of.multiverses@proton.me](mailto:theobserver.of.multiverses@proton.me).

Canonical repository: [Observer1117/compact-resolvent-spectral-encodings](https://github.com/Observer1117/compact-resolvent-spectral-encodings).

Immutable archival record: [OSF Registration](https://osf.io/rwpga/) ([DOI 10.17605/OSF.IO/RWPGA](https://doi.org/10.17605/OSF.IO/RWPGA)). The associated editable project is available at [OSF Project a9fws](https://osf.io/a9fws/).

## Metadata status

The mathematical archival object is **v0.2.0** and remains frozen. Git tag `v0.2.0` points to commit `91aeed526a126ede56397fe42e7393bfbc30d3f6`; its GitHub Release was published on **1 August 2026 at 05:55:04 UTC**. The OSF DOI identifies that frozen Version 0.2 object.

The current repository metadata revision is **v0.2.1 (11 August 2026)**. It resolves two packaging issues without changing mathematical content:

1. `2026-07-27` is retained only as the historical v0.2 mathematical-hardening/version date; it is no longer represented as the public release date.
2. the frozen source's PDF author field contains both `Stassis Stashkevichyus` and `Stassis Research Program`; the v0.2.1 builder emits PDF author metadata containing the human author only.

See [`metadata/date_ledger_v0.2.1.yaml`](metadata/date_ledger_v0.2.1.yaml) and [`metadata/metadata_audit_v0.2.1.md`](metadata/metadata_audit_v0.2.1.md). The v0.2.0 tag, release asset, PDF, source, checksums, and OSF Registration are not rewritten.

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

- [`paper/compact_resolvent_spectral_encodings_v0_2.pdf`](paper/compact_resolvent_spectral_encodings_v0_2.pdf) — frozen archival v0.2.0 manuscript.
- [`source/main.tex`](source/main.tex) — frozen self-contained v0.2.0 LaTeX source.
- [`scripts/build_metadata_revision.py`](scripts/build_metadata_revision.py) — SHA-guarded v0.2.1 metadata-only builder.
- [`audit/referee_audit_v0_2.md`](audit/referee_audit_v0_2.md) — proof and bibliography ledger.
- [`metadata/publication_metadata.yaml`](metadata/publication_metadata.yaml) — canonical structured metadata with typed dates.
- [`metadata/date_ledger_v0.2.1.yaml`](metadata/date_ledger_v0.2.1.yaml) — publication-event date ledger.
- [`metadata/metadata_audit_v0.2.1.md`](metadata/metadata_audit_v0.2.1.md) — current metadata consistency audit.
- [`metadata/citation.bib`](metadata/citation.bib) — BibTeX citation record for the frozen Version 0.2 object.
- [`metadata/osf_registration_metadata.md`](metadata/osf_registration_metadata.md) — historical OSF registration fields.
- [`checksums/SHA256SUMS`](checksums/SHA256SUMS) — frozen v0.2.0 package integrity manifest.

## Build

Requirements: Python 3 and PDFLaTeX/`latexmk` with the standard packages listed in the frozen source.

The default build produces the **v0.2.1 metadata-only successor**. Before any transformation it verifies that `source/main.tex` still has the frozen SHA-256 `5babef3ab8c8ed04b243e4d818809751a7bfe4f20d000f29e88dfbc8db752d5f`.

```bash
make
```

The generated successor is written to:

```text
paper/compact_resolvent_spectral_encodings_v0_2_1.pdf
```

To verify the metadata transformation without compiling:

```bash
make metadata-check
```

To compile the historical frozen source directly:

```bash
make frozen-v0.2.0
```

The v0.2.1 build permits exactly two reversible presentation/metadata substitutions: the PDF `Author` field and the title-page metadata-revision label. Reversing those substitutions must recover the frozen source exactly.

## Citation

Use the immutable OSF Registration as the primary citation record for the frozen Version 0.2 manuscript:

> Stashkevichyus, Stassis. (2026). *A Layered Framework for Compact-Resolvent Spectral Encodings* (Version 0.2). OSF. [https://doi.org/10.17605/OSF.IO/RWPGA](https://doi.org/10.17605/OSF.IO/RWPGA)

The public GitHub Release was published on 1 August 2026. Machine-readable citation metadata are available in [`CITATION.cff`](CITATION.cff) and [`metadata/citation.bib`](metadata/citation.bib). `CITATION.cff` separates the current repository metadata revision from the frozen DOI-bearing preferred citation.

## Reporting errors

Use the issue templates for either a mathematical error or a bibliographic/typographical correction. A GitHub issue is public error reporting, not peer review.

## Versioning

- `v0.2.0`: frozen archival mathematical manuscript registered on OSF;
- `v0.2.x`: metadata, packaging, or typographical corrections that do not change mathematical content;
- `v0.3`: changed definitions, statements, proofs, or substantial exposition;
- `v1.0`: reserved for a version hardened after independent external mathematical review.

## License

The manuscript, LaTeX source, metadata, and documentation are licensed under [Creative Commons Attribution 4.0 International](LICENSE).