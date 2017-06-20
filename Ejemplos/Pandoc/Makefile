# Archivos markdown

FILES = input.md

all: 
	pandoc \
	--filter pandoc-crossref \
	--filter pandoc-citeproc \
	--template=./plantilla.latex \
	-N \
	--chapters $(FILES) metadatos.yaml \
	-f markdown -o output.pdf

# Eliminar output

clean:
	rm output.pdf

# Por si hay algún archivo que se llame clean

.PHONY: clean 
