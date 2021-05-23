#  Estructuras de datos con Python 🐍  🟡🔵

## Autor: Andrés Camilo Núñez Garzón 👨🏽‍💻

## 📖 References / Fuentes:

[Stack - Wikipedia 🇪🇸](https://es.wikipedia.org/wiki/Pila_(inform%C3%A1tica))       
[Queue - Wikipiedia 🇪🇸](https://es.wikipedia.org/wiki/Cola_(inform%C3%A1tica))      
[Linked List - Real Python 🇬🇧](https://realpython.com/linked-lists-python/)
[Graphs - Tutorials Point 🇬🇧](https://www.tutorialspoint.com/python_data_structure/python_graphs.htm)

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

## Queue / Cola
**Archivo**: <code>queue.py</code>
Las colas son una estructura de datos tipo FIFO (First Input First Output, primera entrada primera salida)también cuentan con operaciones para acceder o manipular los datos:
- Crear: constructor de la cola
- Encolar: agregar elemento al final de la cola
- Desencolar: retirar elemento del principio (o front) de la cola
- Frente: Leer el frente de la cola sin retirarlo

## Linked List / Lista Enlazada
**Archivo**: <code>linked_list.py</code>
Las listas enlazadas son una colección ordenada de datos diferentes a las listas en la manera que estas se almacenan en memoria, ya que las listas se almacenan de manera contigua, mientras que las listas enlazadas almacenan dentro de sus elementos referencias.
### Node / node
Las listas enlazadas están compuestas por nodos y cada nodo está compuesto por dos elementos principales:
- Data / Datos: contiene los valores a ser almacenados en el nodo
- Next / siguiente: contiene una referencia al siguiente nodo de la lista
El primer nodo en la lista es llamado **head** o **cabecera** y es el punto de partida para cualquier iteración sobre la lista enlazada.
En cuanto al último nodo su referencia al siguiente nodo debe ser None.

## Graph / Grafo
**Archivo**: <code>graph.py</code>
Los grafos son utilizados para representar la relación entre objetos o para representar diferentes tipos de redes. Típicamente un grafo se representa como un conjunto de puntos (vértices) unidos por líneas (aristas).
Hay diferentes maneras de realizar la implementación de los grafos, uno de los más comunes es la **lista de adyacencia**, donde la primera columna corresponde a los vértices y la segunda columa los vértices conectados mediante aristas al nodo de la primera columna.
Los métodos u operaciones implementadas para esta esta estructura de datos son:
- get_vertices: obtener los vertices del grafo (llaves del diccionario)
- get_edges: obtener las aristas asociadas a cada vértice, devuelve una lista de tuplas
- set_vertice: establecer un nuevo vértice
- set_edge:  establecer una nueva arista, también acepta nuevos vértices