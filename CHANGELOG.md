# Changelog

All notable changes to the public manuscript package are recorded here.

## [0.2.1] - 2026-08-11

### Metadata and provenance hardening

- Separated the historical v0.2 version date, manuscript revision date, public GitHub Release timestamp, archival-metadata date, and repository metadata-revision date.
- Corrected the current repository citation metadata so `2026-07-27` is no longer represented as the public release date.
- Recorded the actual GitHub Release publication timestamp `2026-08-01T05:55:04Z` for tag `v0.2.0`.
- Kept the OSF DOI attached only to the preferred citation for the frozen Version 0.2 object, not to the repository-only v0.2.1 metadata revision.
- Added a SHA-guarded builder that corrects PDF `Author` metadata to the human author only while preserving the frozen v0.2.0 source as an immutable input.
- Added a typed date ledger and a dedicated v0.2.1 metadata audit.
- Left the v0.2.0 tag, release asset, frozen PDF, frozen source, checksum manifest, mathematical content, and OSF Registration unchanged.

## [Unreleased]

### Archival metadata - 2026-08-01

- Added the immutable OSF Registration DOI `10.17605/OSF.IO/RWPGA`.
- Added links to the public OSF Project and Registration.
- Updated CFF, BibTeX, README, release notes, and structured publication metadata.
- Left the frozen v0.2.0 manuscript PDF and mathematical content unchanged.

### Metadata confirmation - 2026-08-01

- Confirmed the canonical author name as `Stassis Stashkevichyus`.
- Added the public research email `theobserver.of.multiverses@proton.me`.
- Confirmed Creative Commons Attribution 4.0 International as the publication license.
- Assigned the dedicated canonical repository `Observer1117/compact-resolvent-spectral-encodings`.
- Updated the manuscript title page revision date without changing mathematical content.

## [0.2.0] - 2026-07-27

`2026-07-27` is retained as the historical mathematical-hardening/version date. The public GitHub Release for tag `v0.2.0` was published on 2026-08-01.

### Mathematical hardening

- Repaired the compact-resolvent proof and made the finite-dimensional case explicit.
- Replaced the conflicting kernel notation by `h_L` in the zeta section.
- Required normal convergence for analytic level encodings.
- Defined tensor sums through closed quadratic forms and joint functional calculus.
- Added the missing dominated-convergence majorant in the periodicity argument.
- Removed an editorial checklist from the theorem/proposition layer.

### Technical hardening

- Removed the `cleveref` dependency for stable arXiv-compatible compilation.
- Verified references, citations, text extraction, embedded fonts, and page rendering.
- Recorded the proof and bibliography audit in `audit/referee_audit_v0_2.md`.
