# Título de primer nivel

## Título de segundo nivel

Lista numerada:

1. *cursiva* o _cursiva_
1. **negrita**
1. [enlace](url) o [enlace] o [enlace][ref]
1. Texto[^nota]

[^nota]: Texto de la nota al pie

[enlace]: url

[ref]: url

### Título de tercer nivel

Imagen

![Texto alternativo](ejemplo.jpg){width=50%}

Tabla

------------
  x      y
----- ------
 0.1   1.3 
------------

Table: Aquí va el caption

$a=1$

$$\int_a^b x^2 \mathrm{d}x$$

`Código inline`

Bloque de código

```haskell
-- Fibonacci!
  fib = 0 : 1 : zipWith (+) fib (tail fib)
```
