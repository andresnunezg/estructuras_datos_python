class linked_list:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        node = self.head
        nodes = list()
        while node != None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data
    
if __name__ == '__main__':
    #crear lista enlazada
    lk_list = linked_list()

    #creaación de nodo cabecera
    node_01 = node('A')

    #establecer node_01 como header de la lista enlazada
    lk_list.head = node_01

    #crear nodos adicionales
    node_02 = node('B')
    node_03 = node('C')
    node_04 = node('D')

    #enlazar nodos
    node_01.next = node_02
    node_02.next = node_03
    node_03.next = node_04

    print(lk_list)