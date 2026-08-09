# A Certified Seventh Min–Max Index Below the Essential Threshold

## Refined Composite Quadrature, Sub-Unit Entry Validation, and Exact Rational Threshold Separation

**Branch:** A.8.10  
**Theorem version:** v0.8.10  
**Replication companion:** A.8.10-R2 v0.2  
**Author:** Stassis Stashkevichyus  
**ORCID:** 0009-0000-2294-705X  
**License:** CC BY 4.0  
**Scientific status:** computer-assisted theorem; implementation-level independent replication passed; not actor-separated external replication; not peer reviewed.

## Main theorem

Let
\[
b_* = \frac{5-\sqrt{13}}2.
\]

The certified seven-dimensional trial space satisfies
\[
\mu_7(\Delta)
<
0.697224362268005353
<
b_*.
\]

Therefore
\[
\operatorname{rank}\mathbf 1_{(-\infty,b_*)}(\Delta)\ge 7.
\]

The statement counts min–max indices with multiplicity. It does **not** assert seven distinct eigenvalues.

## Verification layers

1. Original exact-rational certificate replay.
2. Exact Gram and threshold `LDL^T` certification.
3. Analytic direct-quadrature and normalization error budget.
4. MPFR 192-bit archived direct-compression center.
5. R2 second exact checker written independently of the original proof script.
6. R2 independent reconstruction of the full error budget.
7. R2 cross-stack direct compression with GCC `__float128`/libquadmath, independently generated 24-point Gauss nodes, and a different 48 x 6 composite grid.

The remaining reproducibility gate is actor-separated execution by an external researcher or group.

## Immutable publication rule

The OSF registration for this result should contain the exact files represented by `checksums/SHA256SUMS`. Once registered, that archive is not to be silently replaced. Corrections should receive a new version/registration with an explicit changelog.

## Repository placement

Canonical GitHub repository:

`Observer1117/compact-resolvent-spectral-encodings`

Path:

`research/A/A8.10/`

## OSF

Existing OSF Registration `10.17605/OSF.IO/RWPGA` belongs to the earlier expository v0.2 manuscript and must remain unchanged.

For A.8.10 create a separate OSF component under editable project `a9fws`, then register that component as a new immutable snapshot.

**A.8.10 OSF DOI:** PENDING
