class graph:
    def __init__(self, graph_dict = None):
        if graph_dict is None:
            graph_dict = dict()
        self.graph_dict = graph_dict
    
    def get_vertices(self):
        return list(self.graph_dict.keys())

    def get_edges(self):
        edges = []
        for vertice in self.graph_dict:
            for vertices in self.graph_dict[vertice]:
                if (vertices, vertices) not in edges:
                    edges.append((vertice, vertices))
        return edges
    
    def set_vertice(self, vertice):
        if vertice not in self.graph_dict:
            self.graph_dict[vertice] = []
        else:
            print('vertice already exists!')

    def set_edge(self, edge):
        if edge[0] in self.graph_dict.keys():
            if edge[1] not in self.graph_dict[edge[0]]:
                self.graph_dict[edge[0]].append(edge[1])
            else:
                print('edge already exists!')
        else:
            self.graph_dict[edge[0]] = [edge[1]]

if __name__ == '__main__':
    #grafo a través de diccionarios
    #lista de adyacencia
    graph_dict = {
        'a': ['b', 'c'],
        'b': ['a', 'd'],
        'c': ['a', 'd'],
        'd': ['e'],
        'e': ['d'],
    }

    #mostrar grafo (diccionario)
    print('Diccionario / Lista de adyacencia del grafo')
    print(graph_dict)

    #creación de la instancia para el gráfico
    graph_instance = graph(graph_dict)

    #obtener e imprimir vertices
    print('Aristas: ')
    print(graph_instance.get_edges())

    #agregar vértice f
    graph_instance.set_vertice('f')

    #mostrar nuevamente los vertices
    print('Vertices: ')
    print(graph_instance.get_vertices())

    #agregar una arista (edge) a un vertice existente
    graph_instance.set_edge(('a', 'd'))

    #mostrar el vertice donde se agregó la alista ('a', 'd')
    print('Aristas: ')
    print(graph_instance.get_edges())

    #agregar una arista (edge) a un vertice nuevo
    graph_instance.set_edge(('g', 'a'))

    #mostrar vertices y aristas al agregar arista con vertice nuevo
    print('Vertices: ')
    print(graph_instance.get_vertices())
    print('Aristas: ')
    print(graph_instance.get_edges())

    #agregar arista existente
    graph_instance.set_edge(('g', 'a'))
    #output: edge already exists!