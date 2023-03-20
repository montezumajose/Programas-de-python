class Meses:
    #Variable a utlizar
    def __init__(self):
        self.lista = []
    #Agrega el mes y el valor a la lista
    def agregar(self, valor):
        self.lista.append(valor)
    #Elimina el mes y el valor de la lista
    def eliminar(self, valor):
        indice = self.lista.index(valor)
        self.lista.remove(valor)
        self.lista.pop(indice)
    #Imprime la lista           
    def verLista(Self):
        print(Self.lista)
#Intenta correr el programa y si hay un fallo, imprime que lo tiene
try:   
    c = Meses()
    answerStop = ''
    print("Inicio de Programa")
    #ciclo para pasar meses y sus valores definidos por el usuario
    while (answerStop != 's'):
        #agrega mes a la lista
        answerMes = input("Esciba el mes que desea agregar: ")
        c.agregar(answerMes)
        #agrega monto a la lista
        answerValor = float (input("Esciba el monto de venta del mes: "))
        c.agregar(answerValor)
        #Elimina un mes y su monto
        answerDelete = input("Quiere eliminar un mes? s/n: ")
        if (answerDelete == 's'):
            eliminarMes = input("Escribe el mes que quieres borrar, ej., Enero: ")
            c.eliminar(eliminarMes)
        #Imprime la lista
        answerVer = input("Quieres ver como va la lista s/n: ")
        if (answerVer == 's'):
            c.verLista()
        #Detiene el programa
        answerStop = input("Quieres terminar el programa s/n: ")
        if (answerStop == 's'):
            print("Valor de la lista:\n",c.lista)

except ValueError:
        print("Ingresaste un valor mal")    

    