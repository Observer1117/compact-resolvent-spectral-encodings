# Publication claim wall — A.8.10 + R2

## Proved in A.8.10

- The seven frozen integer trial vectors are linearly independent.
- The exact Gram matrix obeys `G > 99999999980000000000 I`.
- The declared direct-compression validation budget is below the entry radius `2`.
- Therefore the normalized operator error is below `1.40000000028e-19`.
- Exact rational `LDL^T` proves
  `0.697224362268005353 G - A0 - 14 I > 0`.
- Exact arithmetic proves
  `0.697224362268005353 < (5-sqrt(13))/2`.
- Hence
  `mu_7(Delta) < 0.697224362268005353 < (5-sqrt(13))/2`.
- Consequently the sub-threshold spectral projection has rank at least seven, counted with multiplicity.

## Reproduced in A.8.10-R2

- The original exact certificate replays.
- A second exact checker independently reconstructs the Gram matrix and threshold `LDL^T` gate.
- A second checker independently reconstructs the analytic error budget.
- An independent `__float128`/libquadmath implementation on a different Gauss order/grid reproduces the frozen direct-compression center; all 49 entries round to the same integer `A0`.

## Not proved / not claimed

- seven distinct sub-threshold eigenvalues;
- simplicity of the seventh level;
- exact sub-threshold rank;
- any statement about the eighth index;
- actor-separated external replication;
- peer review;
- historical priority;
- physical interpretation of the defect-Laplacian spectrum.
