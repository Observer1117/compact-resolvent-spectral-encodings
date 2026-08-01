# Pre-publication blocking checklist

Release-blocking checks are separated from post-release archival tasks below.

## Author identity

- [x] Canonical surname spelling confirmed as `Stashkevichyus`.
- [x] ORCID identifier confirmed by the author as `0009-0000-2294-705X`.
- [x] Public research email confirmed as `theobserver.of.multiverses@proton.me`.

## Version and license

- [x] Public manuscript title fixed.
- [x] Scientific status fixed as `Expository framework preprint; not peer reviewed`.
- [x] Version fixed as `v0.2.0` for the first public repository release candidate.
- [x] CC BY 4.0 confirmed as the author's final license choice.

## Repository QA

- [x] Rebuild `source/main.tex` twice in a clean TeX environment.
- [x] Compare the rebuilt PDF with the release PDF byte-for-byte.
- [x] Regenerate `checksums/SHA256SUMS` after every metadata or file change.
- [x] Confirm that temporary LaTeX files are excluded by `.gitignore`.
- [x] Parse `CITATION.cff` and all repository YAML files successfully.

## Publication sequence

- [x] Dedicated public GitHub repository identified as `Observer1117/compact-resolvent-spectral-encodings`.
- [x] Push the reviewed package to the dedicated public repository.
- [ ] Create tag and release `v0.2.0`.
- [ ] Create the public OSF Project and upload an independent copy.
- [ ] Create an immutable public OSF Registration.
- [ ] Add the assigned DOI to `CITATION.cff`, BibTeX, README, release notes, website, and ORCID.
