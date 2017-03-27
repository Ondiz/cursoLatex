# La opción Pandoc

Allá por los inicios del cursete de LaTeX hablé de Pandoc, una herramienta que nos permite pasar documentos de un formato a otro fácilmente y, sobre todo, *bien*. Comenté que Pandoc nos permitía escribir en Markdown y obtener un pdf de calidad porque por el medio usaba LaTeX. 

Ventajas:

* No nos deja archivos auxiliares por ahí, los borra una vez hecha la transformación.
* Tecleamos menos, ya que Markdown es un lenguaje mucho más escueto que LaTeX
* Markdown especial de Pandoc que nos permite...
* El documento es legible incluso antes de compilar
* Podemos usar cualquier editor de texto
* Podemos mezclar LaTeX alegremente por ahí, alguna vez me ha dado problemas, pero pocos

Desventajas:

* Más archivos, si es un documento complejo necesitaremos un Makefile
* Instalarlo puede ser un poco lío
* Tenemos que saber LaTeX (pero ya sabemos ¿no?), Markdown y usar Pandoc

# Instalación y uso

Versión antigua en los repositorios
Paquete Debian
Cabal, el gestor de paquetes de Haskell

Citeproc + crossref

Se usa desde la consola

* Compilador
* Variables

# ¿Qué necesitamos?

En esencia necesitamos

* Archivos escritos en Mardown con extensión *md*
* Pandoc y una distribución de LaTeX
* Una consola
* Un bib y un estilo de bibliografía csl si vamos a tener referencias bibliográficas
* Una plantilla si la que usa por defecto no nos gusta

Para hacernos la vida más fácil nos conviene:

* Un archivo YAML para las variables
* Un Makefile y `make`

## Plantilla personalizada

## YAML

```
fontsize: 12pt
```

* Márgenes

```
geometry:
```

* Idioma

```
lang: es
```

* Fuente: 

https://ondahostil.wordpress.com/2017/03/11/lo-que-he-aprendido-margenes-y-fuentes-en-pandoc/

## Makefile
