class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

class linked_list:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node_obj = node(data = nodes.pop(0))
            self.head = node_obj
            for i in nodes:
                node_obj.next = node(data = i) 
                node_obj = node_obj.next

    def __str__(self):
        node = self.head
        nodes = list()
        while node != None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
    def __iter__(self):
        node = self.head
        while node != None:
            yield node
            node = node.next

if __name__ == '__main__':
    #Lista / elemento iterable de nodos
    nodes = ['A', 'B', 'C', 'D']

    #crear lista enlazada
    lk_list = linked_list(nodes)

    #creación de nodo cabecera
    #node_01 = node('A')

    #establecer node_01 como header de la lista enlazada
    #lk_list.head = node_01

    #crear nodos adicionales
    #node_02 = node('B')
    #node_03 = node('C')
    #node_04 = node('D')

    #enlazar nodos
    #node_01.next = node_02
    #node_02.next = node_03
    #node_03.next = node_04

    #Iterar sobre la lista enlazada
    for node in lk_list:
        print(node)

    #imprimir la lista enlazada con el método __str__
    print(lk_list)