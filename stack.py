
class stack:
    def __init__(self):
        self.val = []
    
    def push(self, data):
        self.val.append(data)
    
    def pop(self):
        self.val.pop(-1)
    
    def print_stack(self):
        return self.val
    
    def peek(self):
        return self.val[-1]

    def __str__(self):
        return str(self.val)
    
if __name__ == '__main__':
    #Crear una instancia de la clase stack()
    stack_instance = stack()

    #Importar la librería random
    import random

    #Crar una pila o stack con 10 números aleatorios enteros aleatorios entre 1 y 10
    for i in range(10):
        stack_instance.push(random.randint(0, 10))

    #Mostrar la pila creada con el método print_stack()
    print('Pila creada: ', end='')
    print(stack_instance.print_stack())

    #Eliminar el último elemento apilado
    print('Retirar el último elemento apilado: ' + str(stack_instance.peek()))
    stack_instance.pop()

    #Mostrar la pila creada con el método print()
    print('Pila: ', end='')
    print(stack_instance)

    #Mostrar el último elemento apilado con print y el método built-in print()
    print('Peek de la pila: ' + str(stack_instance.peek()))