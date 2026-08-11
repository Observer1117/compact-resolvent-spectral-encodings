# Metadata correction v0.2.1

Date: 11 August 2026

This repository revision is a metadata and packaging successor to the frozen
v0.2.0 archival manuscript. It does not change mathematical content.

## Corrected

- `date-released` ambiguity: the public GitHub Release for `v0.2.0` was
  published on 1 August 2026 at 05:55:04 UTC. The earlier `2026-07-27` value is
  retained only as historical mathematical-hardening/version provenance.
- PDF author metadata for successor builds: `Stassis Research Program` is no
  longer placed in the PDF `Author` field. The human author is
  `Stassis Stashkevichyus`.
- Citation layering: repository metadata revision `0.2.1` is separated from the
  DOI-bearing preferred citation for frozen Version `0.2`.

## Preserved unchanged

- Git tag `v0.2.0` and commit `91aeed526a126ede56397fe42e7393bfbc30d3f6`;
- GitHub Release asset and SHA-256
  `3e1a2fbf85199db46df781b3ed8f897ae974442584cb0eaa9a301d2c7f1e0bd0`;
- frozen PDF SHA-256
  `2adc288fc3dc596e566bb786de8162411e69416669a90a7dfe35486aa8723c09`;
- frozen source SHA-256
  `5babef3ab8c8ed04b243e4d818809751a7bfe4f20d000f29e88dfbc8db752d5f`;
- OSF Registration DOI `10.17605/OSF.IO/RWPGA`;
- every definition, theorem, proof, example, counterexample, equation, and
  scientific-status statement.

## Build contract

Run:

```bash
make metadata-check
make
```

The builder refuses to transform `source/main.tex` unless its SHA-256 matches
the frozen v0.2.0 source. It then applies exactly two reversible metadata and
presentation substitutions. The generated successor PDF is intentionally not
part of the frozen v0.2.0 checksum manifest.
