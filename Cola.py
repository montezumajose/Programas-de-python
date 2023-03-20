class Cola:
    def __init__(self):
        self.cola = []
    
    def encolar (self, item):
        self.cola.append(item)
    
    def desencolar (self):
        if len(self.cola) < 1:
            return None
        return self.cola.pop(0)
    
    def size (self):
        return len(self.cola)
    
    def is_empty (self):
        return self.size() == 0

# Crear una nueva cola
c = Cola()

# Agregar elementos a la cola
c.encolar ('Carro')
c.encolar ('Bicicleta')
c.encolar ('Patineta')
# Eliminar elementos de la cola
print(c.desencolar())

# Ver si la cola esta vacia
print(c.is_empty())

print(c.size())
