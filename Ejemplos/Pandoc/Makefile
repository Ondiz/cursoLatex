# Archivos markdown

FILES = input.md

all: 
	pandoc \
	--filter pandoc-crossref \
	--filter pandoc-citeproc \
	--template=./plantilla.latex \
	-N \
	-V documentclass=book \
	$(FILES) metadatos.yaml \
	-f markdown -o output.pdf
	xdg-open output.pdf

# Eliminar output

clean:
	rm output.pdf

# Por si hay algún archivo que se llame clean

.PHONY: clean 
