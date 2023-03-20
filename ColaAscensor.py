class Ascensor:
    #Variables principales
    def __init__(self):
        self.ascensor = []
        self.limite = 0
    #Agrega una cadena a la lista
    def encolar(self, item):
        self.ascensor.append(item)
    #Elimina la primera cadena de la lista
    def desencolar(self):
        return self.ascensor.pop(0)
    #Determina cuantas personas van a entrar
    def personas (self):
        try:
            self.limite = int (input("Cuantas personas van a entrar: "))
        except ValueError:
            print("Solo numeros enteros, por favor.")
            
c = Ascensor()
#Ciclo para hacer la lista dinamica de la clase Ascensor
while  True:
    print("Limite del ascensor\n")
    c.personas()
    #Recibe los nombres de las personas
    for i in range(0, c.limite):
        person = input("Personas que van a entrar: ")
        c.encolar(person)
        #Cuando el limite puesto es igual a los elementos de la lista, estara lleno
        if (i == c.limite -1):
            print("Ya no caben, ascensor lleno")
    #Elimina la primera persona e imprime la lista
    answer = input("Desea eliminar a una persona s/n: ")
    if (answer == 's' and 'S'):
        print("Sacamos a ",c.desencolar())
        print("Personas adentro del ascensor\n",c.ascensor)
        c.ascensor.clear()
    else:
        print("Personas adentro del ascensor\n",c.ascensor)
        break