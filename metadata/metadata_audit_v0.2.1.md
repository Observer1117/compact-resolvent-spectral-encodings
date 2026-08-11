# Metadata audit v0.2.1

Audit date: 2026-08-11

## Scope

This audit resolves two repository-level metadata defects without modifying the
frozen v0.2.0 archival object:

1. the repository previously used `2026-07-27` as `date-released` even though
   the public GitHub Release for tag `v0.2.0` was published on 2026-08-01;
2. the frozen source embeds `Stassis Research Program` in the PDF `Author`
   metadata together with the human author, which may be parsed as a second
   author by indexers.

## Frozen archival object

The following objects are historical and remain unchanged:

- Git tag `v0.2.0` -> commit `91aeed526a126ede56397fe42e7393bfbc30d3f6`;
- GitHub Release asset `compact-resolvent-spectral-encodings-v0.2.0-publication-ready.zip`;
- asset SHA-256 `3e1a2fbf85199db46df781b3ed8f897ae974442584cb0eaa9a301d2c7f1e0bd0`;
- frozen manuscript PDF SHA-256 `2adc288fc3dc596e566bb786de8162411e69416669a90a7dfe35486aa8723c09`;
- frozen source SHA-256 `5babef3ab8c8ed04b243e4d818809751a7bfe4f20d000f29e88dfbc8db752d5f`;
- immutable OSF Registration DOI `10.17605/OSF.IO/RWPGA`.

No v0.2.0 tag, release asset, registered file, theorem statement, proof, or
mathematical expression is replaced by this audit.

## Date normalization

The repository now treats dates as typed events:

| Field | Value | Meaning |
|---|---|---|
| historical version date | 2026-07-27 | v0.2 mathematical-hardening/version provenance |
| manuscript revision date | 2026-08-01 | date printed on the frozen manuscript title page |
| GitHub Release published | 2026-08-01T05:55:04Z | actual public GitHub Release timestamp |
| archival metadata added | 2026-08-01 | DOI/OSF links propagated to repository metadata |
| metadata revision | 2026-08-11 | current repository-only v0.2.1 normalization |

The exact sub-day OSF registration timestamp is intentionally left unset. It
must not be inferred from GitHub commit times.

## Author authority normalization

Canonical human author:

- Stassis Stashkevichyus
- ORCID: 0009-0000-2294-705X
- role: Independent Researcher
- location: Vilnius, Lithuania

`Stassis Research Program` is project/program metadata, not an author entity.
The frozen v0.2.0 source remains unchanged for provenance. A new contract
builder, `scripts/build_metadata_revision.py`, verifies the frozen source hash
and produces a v0.2.1 build using exactly two reversible substitutions:

1. `pdfauthor={Stassis Stashkevichyus; Stassis Research Program}` ->
   `pdfauthor={Stassis Stashkevichyus}`;
2. the title-page revision label -> an explicit v0.2.1 metadata-correction label.

Undoing those substitutions must reproduce the frozen source exactly.

## Citation policy

The repository metadata package is revision `0.2.1`, but the DOI continues to
identify the frozen archival Version 0.2 object. Therefore:

- the top-level `CITATION.cff` describes repository metadata revision 0.2.1 and
  does not attach the OSF DOI to that revision;
- `preferred-citation` remains Version 0.2 and carries DOI
  `10.17605/OSF.IO/RWPGA`;
- the preferred citation uses August 2026 because the public GitHub Release was
  published on 1 August 2026.

## Claim boundary

This is a metadata and packaging correction only. It makes no novelty claim,
changes no theorem, and does not alter the scientific status: expository
framework preprint, not peer reviewed.
