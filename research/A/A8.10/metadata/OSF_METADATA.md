# OSF metadata — A.8.10 + R2

## Title
A Certified Seventh Min–Max Index Below the Essential Threshold

## Subtitle
Refined Composite Quadrature, Sub-Unit Entry Validation, and Exact Rational Threshold Separation

## Resource type
Preprint + computational certificate + replication package

## Version
A.8.10 theorem v0.8.10; R2 implementation-replication v0.2

## Creator
Stassis Stashkevichyus  
Independent Researcher  
ORCID: https://orcid.org/0009-0000-2294-705X  
Email: theobserver.of.multiverses@proton.me

## Description
We certify a seventh min–max index below the exact essential threshold of the phase-extended A2 modular-defect Laplacian. Seven frozen integer trial vectors in a 192-dimensional coefficient window define a seven-dimensional trial space. A refined 40 x 5 composite 20-point Gauss–Legendre direct-compression calculation, together with exact rational enclosures for the Gauss nodes and weights, an analytic quadrature remainder, normalization control, MPFR roundoff auditing, and integer-center rounding, yields the uniform entry enclosure |(A_dir-A0)_ij|<2. The exact Gram matrix satisfies G>99999999980000000000 I, implying a normalized operator error below 1.40000000028e-19. Exact rational LDL^T proves positivity of b_7^- G-A0-14I for b_7^-=0.697224362268005353, while exact arithmetic proves b_7^-<(5-sqrt(13))/2. Hence mu_7(Delta)<0.697224362268005353<(5-sqrt(13))/2 and the sub-threshold spectral projection has rank at least seven, counted with multiplicity. A separate R2 implementation-level replication independently reconstructs the exact threshold gate and error budget and reproduces the frozen direct-compression center using a different __float128/libquadmath implementation, independently generated 24-point Gauss nodes, and a 48 x 6 composite grid. This is not actor-separated external replication and the work has not been peer reviewed.

## Scientific status
Computer-assisted mathematical result with implementation-level independent replication. The replication is a second implementation performed within the same research workflow and is not actor-separated external replication. The work has not been peer reviewed.

## Keywords
modular defect Laplacian; essential spectrum; min-max principle; computer-assisted proof; validated quadrature; exact rational arithmetic; interval certification; reproducibility; Weil representation; A2 lattice

## Suggested subjects
Mathematics; Spectral theory; Numerical analysis; Computational mathematics

## Suggested MSC 2020
Primary: 47A10  
Secondary: 65G20, 65D30

## Language
English

## License
Creative Commons Attribution 4.0 International (CC BY 4.0)

## Related resources
- GitHub repository: https://github.com/Observer1117/compact-resolvent-spectral-encodings
- Existing editable OSF project: https://osf.io/a9fws/
- Earlier immutable OSF registration (different work/version; do not overwrite): https://osf.io/rwpga/
- Earlier registration DOI: https://doi.org/10.17605/OSF.IO/RWPGA

## New A.8.10 OSF component
Component URL: PENDING

## New A.8.10 registration
Registration URL: PENDING  
Registration DOI: PENDING

## Registration contents
Register the exact frozen payload represented by `checksums/SHA256SUMS`. The registration should include the theorem PDF, R2 replication PDF, computational proof objects, independent R2 checkers, claim wall, metadata, and checksum manifest.
