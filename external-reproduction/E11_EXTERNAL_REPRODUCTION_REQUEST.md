# E.11 External Reproduction Request

## Objective
Reproduce the released E.11 semantic outputs without author assistance and return a signed attestation. This is an actor-separated scientific reproducibility test, not a request for agreement with the physical interpretation.

## Minimal procedure
1. Obtain the canonical E.11 external-reproduction kit and verify its SHA-256.
2. Use a fresh environment not prepared by the author.
3. Run the documented one-command/CI harness without altering numerical tolerances.
4. Record OS, architecture, compiler, Python version, dependency lock, CPON digest, raw maximum difference, and any failures.
5. Do not request organizer truth for the blind component before finalizing your output.
6. Fill `THIRD_PARTY_ATTESTATION_TEMPLATE.json`.
7. Sign the canonical attestation bytes with a key controlled by the reproducer and provide the public verification key.

## Independence condition
A GitHub-hosted runner triggered by the author is useful runner-separated evidence but is **not** sufficient for this gate. The reproducer must be a separate human actor or team exercising independent control of the execution environment.
