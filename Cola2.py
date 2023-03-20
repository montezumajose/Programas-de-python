import os as sis

class Cola:
    def __init__(self):
        self.array = []
    
    def encolar (self, element):
        self.array.append(element)
    
    def desencolar (self):
        self.array.pop(0)
    
    def frente (self):
        return self.array[0]
    
    def estado (self):
        if (len(self.array) == 0):
            print("Estado del array: Vacio")
        else:
            print("Estado del array: lleno")

c = Cola()

sis.system(command= 'cls')
c.encolar("Jose")
c.encolar("Hola")
c.encolar("pc")


print(c.frente())

c.desencolar()

print(c.frente())
c.estado()
print(c.array,"\n\n")