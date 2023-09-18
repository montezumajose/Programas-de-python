n = int(input("Cuantos clientes son: "))
telefonos = [[]]*n

def eliminar():
    answerName = input("Nombre del cliente que desea elimiar: ")
    for name in telefonos:
        if (name [0] == answerName):
            telefonos.remove(name)
    print("Eliminado correctamente")
            
for i in range(0,n):
    tel = input("Escribe el nombre y el numero de telefono: \n").split()
    telefonos [i]= tel
 
answer = input("Desea eliminar un cliente s/n: ")
if (answer == "s"):
    eliminar()

nombreDelFichero = "Clientes y numeros de telefonos"+".txt"
fichero = open(nombreDelFichero, "w")

for clientes in telefonos:
    for elemento in clientes:
        fichero.write(str(elemento+" "+"\n"))
fichero.close()