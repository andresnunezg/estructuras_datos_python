#  Estructuras de datos con Python 🐍  🟡🔵

## Autor: Andrés Camilo Núñez Garzón 👨🏽‍💻

## 📔 References / Fuentes:

[Stack - Wikipedia](https://es.wikipedia.org/wiki/Pila_(inform%C3%A1tica))
[Queue - Wikipiedia](https://es.wikipedia.org/wiki/Cola_(inform%C3%A1tica))
[Real Python!](https://realpython.com/linked-lists-python/)


## Stack / Pila
**Archivo**: <code>stack.py</code>
- Estructura de datos con método de acceso tipo LIFO por las siglas en inglés Last Input First Output.
- En cada momento se tiene acceso sólo al TOS (Top Of Stack - parte superior de la pila)
- Cuenta con dos operaciones básicas: **Push (apilar)**: coloca un objeto en la pila, y **Pop**: retira el TOS

### Operaciones
Adicional a las operaciones tradicionales **push** y **pop** las pilas cuentan con:
- Crear (constructor): Crea una pila vacía
- Tamaño (size): Regresa el tamaño de la pila
- Apilar (push): Agrega un elemento al TOS
- Desapilar (pop): Retira el TOS
- Leer el TOS (peek / top): Lee el último elemento apilado
- Vacía (empty): True si la pila está vacía y False de lo contrario