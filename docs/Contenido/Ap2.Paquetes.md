---
layout: default
title: LaTeX - Paquetes
---

# Hablemos de paquetes

En todo el curso no he hablado de instalación pero me parecía
necesaria una pequeña nota sobre los paquetes, especialmente para el
caso de GNU/Linux, ya que la distribución de LaTeX para Windows,
MikTeX, instala los paquetes necesarios de manera automática.

El caso de TeXLive es diferente porque hay dos maneras<label
for="manual" class="margin-toggle sidenote-number"></label><input
type="checkbox" id="manual" class="margin-toggle"/><span
class="sidenote">También se pueden descargar los paquetes de CTAN y
descomprimirlos en la carpeta correcta de nuestro LaTeX tal y como
cuentan <a
href="https://en.wikibooks.org/wiki/LaTeX/Installing_Extra_Packages">aquí</a>.
Nunca lo he hecho y me parece un poco lioso.</span> de instalarlo en
GNU/Linux:

* **Desde los repositorios de nuestra distro**, cuando queramos
  instalar paquetes usaremos también los repositorios.

* **Descargándolo [por ahí][texlive]**, lo que suelen llamar *TeXLive
  nativo*. En este caso habrá que usar el gestor de paquetes de
  TeXLive.

[texlive]: https://www.tug.org/texlive/doc/texlive-en/texlive-en.html#installation

## Descargar paquetes desde los repositorios

Los paquetes de TeXLive viven en paquetes de los repositorios (de
Debian, en mi caso<label for="distro" class="margin-toggle
sidenote-number"></label><input type="checkbox" id="distro"
class="margin-toggle"/><span class="sidenote">Creo que funciona de la
misma manera en todas las distros, tenéis información específica <a
href="http://tug.org/texlive/distro.html">aquí</a>.</span>) pero *no
directamente con su nombre*. Me explico con un ejemplo: el soporte de
idioma.

Sabemos que para que LaTeX nos haga bien la silabación y que use las
palabras claves (*Capítulo*, *Sección*, …) en el idioma
correspondiente necesitamos el paquete `babel` con el idioma como
opción:

```latex
\usepackage[spanish]{babel}
```

Si hemos instalado la versión sencilla de TeXLive y añadimos esa línea
a nuestro *tex* nos dará error al compilar porque nos falta el paquete
de español. Para buscarlo hacemos<label for="buscar"
class="margin-toggle sidenote-number"></label><input type="checkbox"
id="buscar" class="margin-toggle"/><span class="sidenote">Para ver
cuál es el comando para buscar paquetes equivalente a <code>apt-cache
search</code> en otras distros podéis usar <a
href="https://colaboratorio.net/gestor-paquetes.html">esta tabla</a>
de los <em>compis</em> de <a
href="https://colaboratorio.net/">Colaboratorio</a>.</span>:

```bash
apt-cache search texlive spanish
```

Veremos lo siguiente:

```bash
texlive-latex-extra - TeX Live: LaTeX additional packages
texlive-doc-es - TeX Live: transitional dummy package
texlive-lang-spanish - TeX Live: Spanish
```

Esto nos da una pista de donde vive el paquete: en el grupo de
paquetes adicionales (`texlive-latex-extra`) o en uno específico de
idioma (`texlive-lang-spanish`). Ahora podemos instalar el que
prefiramos.

Resumiendo: *cada vez que necesitemos un paquete de TeXLive debemos
buscar el paquete de los repositorios que lo contiene*. Este sistema
es cómodo pero tiene el problema de que los paquetes suelen ser
ancianos, de ahí la utilidad del segundo método.

## El gestor de paquetes de TeXLive

También se pueden instalar los paquetes con `tlmgr`, el gestor de
paquetes de TeXLive. Para usar esta opción hay que instalar TeXLive
[descargándolo de la red][internet]<label for="kile"
class="margin-toggle sidenote-number"></label><input type="checkbox"
id="kile" class="margin-toggle"/><span class="sidenote">Kile por
ejemplo depende de TeXLive así que solo con una <em>instalación
nativa</em> no funcionará. En algunas distros está disponible el
paquete <code>texlive-dummy</code> para solucionar este problema. En
Debian y derivados hay que instalar un <a
href="http://tug.org/texlive/debian.html#vanilla"><em>vanilla
TeXLive</em></a>.</span>. Luego instalamos los paquetes escribiendo en
la terminal<label for="gui" class="margin-toggle
sidenote-number"></label>:

```bash
tlmgr install PAQUETE
```

[internet]: http://tug.org/texlive/acquire-netinstall.html

Incluso podemos actualizar todos los paquetes instalados con:

<input type="checkbox" id="gui"
class="margin-toggle"/><span class="sidenote">¡También tiene una <a
href="https://darrengoossens.wordpress.com/tag/gui/">GUI</a>!</span>

```bash
tlmgr update --all
```

Como siempre, tenemos toda la información sobre este comando en su
[manual] y en este caso también haciendo:

```bash
tlmgr --help
```

Este sistema tiene la ventaja de que los paquetes que descarguemos
estarán actualizados, aparte de que tendremos acceso a paquetes que
todavía no son parte de los repositorios de nuestra distribución de
GNU/Linux.

# Referencias

[*Best way to install packages for TeXLive in Ubuntu?* en TeXExchange](http://tex.stackexchange.com/questions/28528/best-way-to-install-packages-for-texlive-in-ubuntu)

[*LaTeX/Installing Extra Packages* en Wikibooks](https://en.wikibooks.org/wiki/LaTeX/Installing_Extra_Packages)

[*TeX Live - Quick install*](https://www.tug.org/texlive/quickinstall.html)

[*How to install a language package in Texmaker on Ubuntu 12.04?* en TeXExchange](http://tex.stackexchange.com/questions/73526/how-to-install-a-language-package-in-texmaker-on-ubuntu-12-04#73528)

[*TeX Live package installation*](https://www.tug.org/texlive/pkginstall.html)

[*TeX Live and distros*](http://tug.org/texlive/distro.html)

[*LaTeX Installation* en texblog](http://texblog.org/2011/05/12/updating-latex-tex-live/)

[*Installing TeXlive on Ubuntu, revisited* en TeXExchange](https://tex.stackexchange.com/questions/114623/installing-texlive-on-ubuntu-revisited)

[*TeX Live* en la wiki de Arch](https://wiki.archlinux.org/index.php/TeX_Live)

[Manual de `tlmgr`][manual]

[manual]: https://www.tug.org/texlive/doc/tlmgr.html

***

<div> <p> Anterior: <a href="{{ site.github.url
}}/Contenido/Ap1.Auxiliares.html">Una nota sobre los archivos
auxiliares</a>,
Siguiente: <a href="{{ site.github.url
}}/Contenido/Ap3.Enlaces.html">Enlaces de interés</a>,
[<a href="{{ site.github.url }}/">Contenido</a>]</p> </div>
