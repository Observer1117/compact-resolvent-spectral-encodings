# GitHub / OSF release notes — A.8.10 + R2

This release publishes the theorem-level A.8.10 seventh-index certificate together with the A.8.10-R2 implementation-level replication.

## Theorem
`mu_7(Delta) < 0.697224362268005353 < (5-sqrt(13))/2`, hence the spectral projection below the exact essential threshold has rank at least seven, counted with multiplicity.

## Replication
R2 reproduces the central proof object through:
- an independently written exact rational checker;
- an independently reconstructed error budget;
- an independent GCC `__float128`/libquadmath direct-compression evaluator;
- independently generated 24-point Gauss nodes and a different 48 x 6 composite grid.

## Boundaries
This release does not claim seven distinct eigenvalues, actor-separated external replication, peer review, or physical interpretation.

## Archival policy
The OSF registration should be created from a dedicated A.8.10 component and must freeze the exact bytes listed in `checksums/SHA256SUMS`. The earlier OSF registration for v0.2 remains a separate immutable record.
