.PHONY: all metadata-check metadata-source metadata-v0.2.1 frozen-v0.2.0 clean

all: metadata-v0.2.1

metadata-check:
	python3 scripts/build_metadata_revision.py --check

metadata-source:
	python3 scripts/build_metadata_revision.py --prepare

metadata-v0.2.1:
	python3 scripts/build_metadata_revision.py --build

frozen-v0.2.0:
	cd source && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	python3 scripts/build_metadata_revision.py --clean
	cd source && latexmk -C main.tex
