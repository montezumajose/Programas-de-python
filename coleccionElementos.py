import random

arreglo = []
numero = 0
contador = 0

for i in range(0,20):

    arreglo.append(random.randint(1,20))

numero = int(input("Escriba el numero que desea consultar: "))

for i in range(0,len(arreglo)):
    if (numero == arreglo[i]):
        contador += 1

print(f"\nEl numero {numero} se repite: {contador} veces.")
