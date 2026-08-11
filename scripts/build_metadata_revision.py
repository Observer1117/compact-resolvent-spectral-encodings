#!/usr/bin/env python3
"""Build the v0.2.1 metadata-only successor from the frozen v0.2.0 source.

The mathematical source in source/main.tex is an immutable input. This script
permits exactly two presentation/metadata substitutions and refuses to run if
the frozen source hash changes.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FROZEN_SOURCE = ROOT / "source" / "main.tex"
BUILD_DIR = ROOT / "build" / "v0.2.1"
GENERATED_SOURCE = BUILD_DIR / "main.tex"
OUTPUT_PDF = ROOT / "paper" / "compact_resolvent_spectral_encodings_v0_2_1.pdf"

FROZEN_SOURCE_SHA256 = "5babef3ab8c8ed04b243e4d818809751a7bfe4f20d000f29e88dfbc8db752d5f"
OLD_PDF_AUTHOR = "pdfauthor={Stassis Stashkevichyus; Stassis Research Program}"
NEW_PDF_AUTHOR = "pdfauthor={Stassis Stashkevichyus}"
OLD_REVISION_LINE = "{\\normalsize Expository framework preprint -- revised 1 August 2026\\par}"
NEW_REVISION_LINE = "{\\normalsize Expository framework preprint -- v0.2.1 metadata correction, 11 August 2026\\par}"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def transformed_source() -> str:
    actual = sha256(FROZEN_SOURCE)
    if actual != FROZEN_SOURCE_SHA256:
        raise RuntimeError(
            "Frozen source hash mismatch: expected "
            f"{FROZEN_SOURCE_SHA256}, found {actual}. Refusing metadata patch."
        )

    text = FROZEN_SOURCE.read_text(encoding="utf-8")
    if text.count(OLD_PDF_AUTHOR) != 1:
        raise RuntimeError("Expected exactly one frozen pdfauthor field.")
    if text.count(OLD_REVISION_LINE) != 1:
        raise RuntimeError("Expected exactly one frozen title-page revision line.")

    transformed = text.replace(OLD_PDF_AUTHOR, NEW_PDF_AUTHOR, 1)
    transformed = transformed.replace(OLD_REVISION_LINE, NEW_REVISION_LINE, 1)

    # Reversibility is the mathematical-content guard: undoing the two allowed
    # substitutions must recover the frozen source byte-for-byte as text.
    reversed_text = transformed.replace(NEW_PDF_AUTHOR, OLD_PDF_AUTHOR, 1)
    reversed_text = reversed_text.replace(NEW_REVISION_LINE, OLD_REVISION_LINE, 1)
    if reversed_text != text:
        raise RuntimeError("Metadata transformation is not exactly reversible.")

    if "pdfauthor={Stassis Stashkevichyus;" in transformed:
        raise RuntimeError("Program identity remains embedded in PDF author metadata.")
    return transformed


def check() -> None:
    transformed_source()
    print("v0.2.1 metadata transformation contract verified.")
    print(f"Frozen source SHA-256: {FROZEN_SOURCE_SHA256}")
    print("Allowed changes: pdfauthor field; title-page metadata-revision line.")


def prepare() -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    GENERATED_SOURCE.write_text(transformed_source(), encoding="utf-8")
    print(f"Prepared {GENERATED_SOURCE.relative_to(ROOT)}")


def build() -> None:
    prepare()
    subprocess.run(
        [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "main.tex",
        ],
        cwd=BUILD_DIR,
        check=True,
    )
    built = BUILD_DIR / "main.pdf"
    if not built.is_file():
        raise RuntimeError("latexmk completed without producing main.pdf")
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(built, OUTPUT_PDF)
    print(f"Built {OUTPUT_PDF.relative_to(ROOT)}")
    print(f"PDF SHA-256: {sha256(OUTPUT_PDF)}")


def clean() -> None:
    shutil.rmtree(BUILD_DIR, ignore_errors=True)
    if OUTPUT_PDF.exists():
        OUTPUT_PDF.unlink()


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--prepare", action="store_true")
    group.add_argument("--build", action="store_true")
    group.add_argument("--clean", action="store_true")
    args = parser.parse_args()

    if args.check:
        check()
    elif args.prepare:
        prepare()
    elif args.build:
        build()
    else:
        clean()


if __name__ == "__main__":
    main()
