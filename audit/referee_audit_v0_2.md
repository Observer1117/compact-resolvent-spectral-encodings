# Referee audit for Article A v0.2

## Scope and verdict

This audit treats the manuscript as an expository framework note, not as an
original research paper. Every theorem, proposition, corollary, example with a
mathematical conclusion, and proof was checked against its stated hypotheses.

Verdict: the revised manuscript is mathematically suitable for arXiv submission
as an expository note in `math.SP`, with `math.FA` as a reasonable cross-list.
This is not a substitute for independent human peer review, and the manuscript
still makes no claim of a new theorem in spectral geometry.

## Proof ledger

| Item | Classification | Audit result |
| --- | --- | --- |
| Theorem 2.2, compact-resolvent spectral theorem | Standard | Correct. The proof now states that the compact resolvent is injective, accounts for its kernel, transfers eigenvectors to the unbounded operator, separates the finite-dimensional case, and proves finite-rank bounded spectral windows. |
| Example 2.4, compact carrier with continuous spectrum | Counterexample | Correct. The spectrum is the essential range `[1,3]`. Noncompactness of the resolvent multiplier now follows explicitly because a compact boundedly invertible operator on an infinite-dimensional space would make the identity compact. |
| Example 2.8, compact resolvent without heat-admissibility | Counterexample | Correct. The real diagonal operator is self-adjoint on its maximal domain, its resolvent entries tend to zero, and its heat trace is a divergent p-series for `0 < t <= 1`. |
| Proposition 3.3, complex-time trace | Elementary analytic result | Correct. Trace-class membership, the trace-norm identity, local uniform convergence, differentiation under the sum, and domination all follow from heat-admissibility. |
| Proposition 3.4, imaginary periodicity | Elementary uniqueness result | Correct. The converse proof now contains an explicit summable majorant before dominated convergence is iterated over the ordered distinct levels. |
| Proposition 3.7, Mellin identity | Standard transform identity | Correct after repair. The kernel multiplicity is denoted by `h_L`, avoiding conflict with the first spectral multiplicity `m_0`; the exact Tonelli/Fubini absolute-integrability calculation is displayed. |
| Proposition 4.2, diagonal realization | Standard spectral construction | Correct. The maximal diagonal domain, compactness by finite-rank resolvent truncation, trace-class criterion, unitary classification, and finite-list variant are explicit. |
| Theorem 4.5, elliptic package | Quoted standard theorem | Correct under the declared hypotheses: closed manifold, finite-rank Hermitian bundle, nonnegative self-adjoint Laplace-type operator. It is explicitly marked as standard and sourced. |
| Example 4.7, non-geometric abstract heat trace | Obstruction example | Correct. Heat-admissibility is proved by a geometric tail bound, while one optimized summand yields `Z_L(t) >= exp(c/t)`, excluding every closed finite-dimensional Laplace-type realization by small-time heat asymptotics. |
| Proposition 5.1, circle spectrum | Standard Fourier/Poisson result | Correct with the now-declared Fourier-transform convention. |
| Proposition 5.2, flat-torus spectrum | Standard Fourier/Poisson result | Correct. Positive definiteness gives convergence and the Gaussian transform has the stated determinant and pi normalization. |
| Proposition 5.4, product heat trace | Standard tensor result | Correct after repair. The tensor sum is now defined through its closed quadratic form and joint functional calculus before the heat-trace factorization is asserted. |
| Proposition 6.2, fiber criterion | Elementary set-theoretic result | Correct. The induced map is canonically defined only on the actual image `Pi(X)`. |
| Corollary 6.3, continuous descent | Standard quotient result | Correct. Surjectivity and the quotient-map hypothesis are both present. |
| Proposition 6.6, static symmetry labels | Standard equivariant spectral result | Correct. Domain commutation is passed to the resolvent and bounded Borel functional calculus; finite-dimensional eigenspaces decompose unitarily. |
| Proposition 6.8, toric eigenspace | Elementary representation calculation | Correct. The full lattice degeneracy `r_A(lambda)` multiplies every internal representation multiplicity. |

## Blocking defects repaired from v0.1

1. The symbol `m_0` was used both for the first distinct eigenvalue
   multiplicity and for `dim ker L`. It is now `h_L` in the zeta section.
2. Pointwise convergence of a level series was described as an analytic
   expression. The definition now requires normal convergence on open sets and
   groups repeated levels before any heat-trace claim.
3. The tensor sum lacked a self-adjoint domain. It is now defined by a closed
   quadratic form.
4. The compact-resolvent proof suppressed the zero-kernel argument for the
   resolvent. The proof now states it.
5. The periodicity proof invoked dominated convergence without displaying a
   tail majorant. The majorant is now explicit.
6. An editorial checklist was labeled as a proposition. It is now an audit
   protocol, not a mathematical result.
7. `cleveref` was removed because arXiv documents a TeX Live 2025 compatibility
   issue for theorem names. Explicit typed references are used instead.

## Bibliographic audit

All sixteen entries were checked for author order, title, venue or series,
year, and page range where applicable. Publisher or DOI records were used for
the main analytic sources. DOI links were added or normalized for Berline-
Getzler-Vergne, Chamseddine-Connes, Davies, Folland, Fulton-Harris, Gilkey,
Kato, Minakshisundaram-Pleijel, and Simon. The Seeley proceedings entry is
identified by volume, pages, and MR number rather than by an unverified DOI.

The cited literature supports only standard inputs. No bibliography entry is
used to imply priority for the manuscript's organizational taxonomy.

## arXiv technical audit

- Source engine: PDFLaTeX.
- External figures: none.
- External bibliography files: none.
- Local or proprietary style files: none.
- File names: restricted to arXiv-safe characters.
- JavaScript or embedded media: none.
- The metadata abstract is below arXiv's 1920-character limit.
- Suggested primary category: `math.SP`.
- Suggested cross-list: `math.FA`.
- The source was compiled twice with resolved references and no LaTeX warnings,
  undefined citations, or overfull boxes.

Account endorsement and arXiv moderation are external submission conditions;
they are not established by this technical audit.
