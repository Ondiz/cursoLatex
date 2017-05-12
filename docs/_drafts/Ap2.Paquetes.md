# Hablemos de paquetes

Hay dos maneras de instalar TeXLive en GNU/Linux:

* **Desde el gestor de paquetes**, cuando queramos instalar paquetes
  usaremos también el gestor

* **Descargándolo por ahí**, lo que suelen llamar *TeXLive nativo*. En
  este caso habrá que usar el gestor de paquetes de TeXLive con el
  comando `tlmgr`

Yo instalé TexLive con `apt-get` así que os hablaré de la primera
opción. Lo que a mí me lió fue que los paquetes de TeXLive viven en
paquetes de los repositorios (de Debian, en mi caso) pero *no
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
de español. Bien, vamos a buscarlo. Hacemos:
 
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
idioma (`texlive-lang-spanish`). Yo instalé el segundo.

Resumiendo: *cada vez que necesitemos un paquete de TeXLive debemos
buscar el paquete de los repositorios que lo contiene*.


# Referencias

[*Best way to install packages for TeXLive in Ubuntu?* en StackExchange](http://tex.stackexchange.com/questions/28528/best-way-to-install-packages-for-texlive-in-ubuntu)

[*TeX Live - Quick install*](https://www.tug.org/texlive/quickinstall.html)

[*How to install a language package in Texmaker on Ubuntu 12.04?* en StackExchange](http://tex.stackexchange.com/questions/73526/how-to-install-a-language-package-in-texmaker-on-ubuntu-12-04#73528)

[*TeX Live package installation*](https://www.tug.org/texlive/pkginstall.html)
