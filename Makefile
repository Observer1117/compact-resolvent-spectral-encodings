.PHONY: all clean

all:
	cd source && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

clean:
	cd source && latexmk -C main.tex

