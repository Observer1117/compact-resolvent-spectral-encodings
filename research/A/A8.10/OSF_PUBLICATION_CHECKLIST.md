# OSF publication checklist — A.8.10 + R2

This checklist is deployment guidance and is **not** part of the immutable scientific payload.

## 1. Preserve the earlier record

Do not modify or repurpose the existing immutable registration `https://osf.io/rwpga/` / DOI `10.17605/OSF.IO/RWPGA`. It belongs to the earlier expository v0.2 manuscript.

## 2. Create a dedicated component

In editable OSF project `https://osf.io/a9fws/`, create a component named:

`A.8.10 — Certified Seventh Min–Max Index`

Use the metadata in `metadata/OSF_METADATA.md` and license CC BY 4.0.

## 3. Upload the frozen archive

Upload exactly:

`A8_10_OSF_GitHub_frozen_payload_v0.8.10-r2.zip`

Expected SHA-256:

`723e90f76ca81c236be434945fd8c7e118017f43d4d2697189a088cc0310430c`

For convenient browsing, also upload the two PDFs and `checksums/SHA256SUMS` as separate files, without modifying their bytes.

## 4. Verify before registration

Verify the ZIP SHA-256 and the individual file hashes in `checksums/SHA256SUMS`.

Do not register if any byte differs from the frozen manifest.

## 5. Register the component

Start a new OSF registration **from the A.8.10 component**, not from the root project. Use a general/open-ended registration suitable for archiving a completed research snapshot.

Make it public when ready. Treat the registration as immutable scientific evidence.

## 6. Use one primary DOI

Use the new public **registration DOI** as the primary citation identifier for A.8.10. A separate component DOI is optional; avoiding an unnecessary second DOI reduces citation ambiguity.

## 7. Backfill GitHub metadata only after DOI minting

Replace `PENDING` in:

- `metadata/OSF_METADATA.md`
- `metadata/publication_metadata.yaml`
- `metadata/CITATION_A8_10.cff`
- `README.md`

Do not modify theorem PDFs, proof objects, R2 checkers, or the frozen OSF payload when backfilling metadata.

## 8. GitHub release state

After DOI backfill:

1. review and merge the publication PR;
2. create a version tag/release such as `a8.10-r2` in the GitHub UI;
3. use `metadata/RELEASE_NOTES.md` as the release description;
4. link the OSF registration DOI prominently;
5. keep the root v0.2 citation metadata unchanged because it refers to a different publication object.

## Claim boundary

Permitted wording:

`Computer-assisted theorem with implementation-level independent replication.`

Not permitted until further evidence exists:

`Externally independently reproduced.`

`Peer reviewed.`
