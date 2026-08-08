# Branch E external-reproduction stage

This directory starts the evidence layer that follows the internal E.11 hardening release.

## Immutable identifiers

- E.11 canonical bundle SHA-256: `2f827df6d8ff0b395db1eefea2258adb0a8d5ad262c761f4bc6c2dcdc388fcb9`
- E.11 external reproduction kit SHA-256: `93eb92abcd1056b0e9e15acce4b33da09a37743f307394a45ee823e4c1fa2bcf`
- Expected CPON digest: `6ea0e7aa7a96208649d8474ca28a7243dc0da6ae895d51476bf826ef49d02e3b`
- Pinned ampyL upstream commit: `4e292b319fd3721ea99f9347490641591862baaf`

## Evidence taxonomy

- `E_int`: internally generated mathematical/numerical evidence.
- `E_runner`: evidence from separately controlled hosted runners/toolchains.
- `E_human`: actor-separated reproduction by an independent person or team.
- `E_phys`: physics-grade admission of an external dataset/release.

`E_runner` must not be relabeled as `E_human`.

## Current open gates

1. native macOS CPON reproduction;
2. pinned ampyL benchmark execution;
3. actual container image, content digest, SPDX SBOM and signature;
4. signed actor-separated reproduction;
5. actual blind external challenge;
6. publication-equivalent real-QCD admission.

Negative results and discrepancies are valid evidence and should be preserved.

See `E11_EXTERNAL_REPRODUCTION_REQUEST.md` and `THIRD_PARTY_ATTESTATION_TEMPLATE.json`.
