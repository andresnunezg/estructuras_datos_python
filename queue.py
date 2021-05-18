class queue:
    def __init__(self):
        #constructor
        self.val = list()
    
    def enqueue(self, data):
        #encolar
        self.val.append(data)

    def dequeue(self):
        #desencolar
        self.val.pop(0)
    
    def front(self):
        #frente o peek
        return self.val[0]

    def back(self):
        #cola o tail
        return self.val[-1]
    
    def empty(self):
        if len(self.val) == 0:
            return True
        else:
            return False
    
    def print_queue(self):
        print(str(self.val))
    
    def __str__(self):
        return str(self.val)

if __name__ == '__main__':
    #crear una instancia de la clase queue
    queue_instance = queue()

    #encolar diferentes tipos de datos a la cola
    print('enqueue...')
    queue_instance.enqueue(10)
    queue_instance.enqueue('Hola')
    queue_instance.enqueue(True)
    queue_instance.enqueue(3.0)
    queue_instance.enqueue(False)

    #mostrar el estado de la cola con el método print_queue()
    print('Queue creado: ')
    queue_instance.print_queue()

    #desencola un elemento
    print('dequeue: ')
    queue_instance.dequeue()

    #imprimir la cola con el método built-in print()
    print(queue_instance)

    #Prueba de vaciado de una queue. Uso del método empty()
    print('Cola vacía: ', queue_instance.empty())
    print('Vaciado de la cola...')
    while not queue_instance.empty():
        queue_instance.dequeue()
    
    print('Cola vacía: ', queue_instance.empty())