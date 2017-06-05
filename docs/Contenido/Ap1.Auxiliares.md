---
layout: default
title: LaTeX - Auxiliares
---

# Una nota sobre los archivos auxiliares

Os habréis fijado como yo en que cuando compilamos LaTeX desde un IDE
se generan miles y miles de archivos auxiliares al darle a que genere
el documento. Vamos a ver si conseguimos clarificar un poco que para
qué sirven algunos de ellos.

Aquí tenemos un lista de los archivos auxiliares más típicos, lo mejor
de todo es que todos ellos son texto plano así que podemos abrirlos y
mirar qué contienen:

- `aux`: sirve para gestionar las referencias cruzadas (`\ref`) y las
  citas bibliográficas (`\cite`), entre otras cosas. En general,
  guarda la información que ha de pasarse de un proceso de
  compilación a otro.

- `log`: aquí se guarda la información sobre el proceso de
  compilación, las advertencias, los errores, los paquetes utilizados
  con su respectiva versión y tal. Es especialmente útil si nos falla
  al crear el documento y no sabemos por qué.

- `synctex`: sincroniza nuestro código fuente con el documento de
  salida en el IDE, es decir, al movernos por el código fuente vemos
  al lado la parte correspondiente del *pdf*. Podemos borrarlo
  alegremente, simplemente se creará otro.

- `toc`, `lof`, `lot` … : sirven para crear el índice, la lista de
  figuras, la lista de tablas …

- `out`: lo genera `hyperref` y vale para crear los enlaces que nos
  llevan de un lado a otro en el *pdf*.

- `bbl`: es el archivo de bibliografía creado por BibTeX. 

- *Otros*: otros paquetes crean archivos auxiliares para gestionar sus
  cosas, por ejemplo, el paquete [`listofsymbols`] crea un `sub` y un
  `sym` para gestionar la lista de subíndices y de símbolos
  respectivamente. Otro ejemplo son los archivos `idx` que sirven para
  hacer el índice por palabras con [`makeindex`].

[`listofsymbols`]: http://ctan.org/pkg/listofsymbols
[`makeindex`]: https://en.wikibooks.org/wiki/LaTeX/Indexing

Para el caso de Beamer se crean además estos otros:

- `snm`: ayuda en el proceso de insertar imágenes en el tipo `article`
- `nav`: sirve para crear la barra de navegación en la presentación

Todos estos archivos aparecen porque cuando nosotros le damos al
botoncillo para que nos cree el documento por dentro en realidad se
invocan un montón de procesos. Tomando como ejemplo un caso en el que
usemos `pdflatex` y tengamos referencias se haría algo así:

```bash
pdflatex fuente.tex  # primera compilación
bibtex fuente.aux    # la bibliografía
pdflatex fuente.tex  # para referencias 
pdflatex fuente.tex  # para referencias 
```

Como veis, necesitamos compilar tres veces para tener las referencias
correctamente. A este proceso se le pueden añadir otros pasos como
`makeindex`, para el índice por palabras, o `makeglossaries`, para
crear el glosario. Es por esta ristra de procesos que nosotros no
vemos que se escriben todos los archivos auxiliares.

Os preguntaréis: *¿estas mierdas para qué las va dejando por ahí? ¿no
las puede crear y luego borrarlas?* Podría hacerlo, sí, Pandoc lo hace
de hecho, crea una carpeta temporal con las basuras y luego la
borra. Esto es como todo en la vida, tiene sus ventajas y sus
inconvenientes. Tener esos archivos auxiliares nos permite hurgar y
trucar cosas y es útil para ver dónde falla al compilar. Pero si no os
gusta que os deje cosas por ahí tenéis varias opciones:

- Si usáis un IDE tipo Kile, tendréis un botón para eliminar los
  archivos auxiliares.

- Si el documento no tiene referencias cruzadas, ni citas
  bibliográficas, ni ninguna cosa que necesite archivos auxiliares
  podemos usar `\nofiles` en el preámbulo y solo nos creará el `pdf`y
  el `log`. También se creará el `synctex` si compilamos desde un
  IDE. Tampoco nos ahorramos mucha cosas como veis.

- Añadir `--aux-directory=CARPETA` a la orden de compilar. Así meterá
  todos los archivos auxiliares en la carpeta que le hemos dicho y
  buscará también ahí cuando los necesite. Lo podemos cambiar
  fácilmente en el IDE donde aparecen las órdenes. Esta es la opción
  que yo suelo usar (ahora que la he descubierto).

- Compilar con la opción `--jobname=CARPETA/OUTPUT INPUT.tex`, así
  guardará el *pdf* y los archivos auxiliares en la carpeta que
  nosotros queramos<label for="shevek" class="margin-toggle
  sidenote-number"></label><input type="checkbox" id="shevek"
  class="margin-toggle"/><span class="sidenote">¡Gracias Shevek por
  hablarme de esta opción!</span>.

- Usar *Pandoc*. Esto nos hace cambiar nuestra forma de trabajar
  radicalmente, pero no nos quedan sobras por ahí.


# Referencias

[*Auxiliary Files* en Dickimaw Books](http://www.dickimaw-books.com/latex/novices/html/auxiliary.html)

[*Prevent pdflatex from writing a bunch of files* en TeXExchange]( http://tex.stackexchange.com/questions/11123/prevent-pdflatex-from-writing-a-bunch-of-files)

[*I don’t want the .aux, .log and .synctex.gz files when using pdflatex* en StackOverflow](http://stackoverflow.com/questions/3745908/i-dont-want-the-aux-log-and-synctex-gz-files-when-using-pdflatex)

[`latex-mk`](http://latex-mk.sourceforge.net/)

***

<div>
<p> Anterior: <a href="{{ site.github.url
}}/Contenido/Ap2.X.html">AP2</a>,
[<a href="{{ site.github.url }}/">Contenido</a>]</p>
</div>
