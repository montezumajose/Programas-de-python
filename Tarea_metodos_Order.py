import random

randomNumber = []

for i in range (0,100):
    randomNumber.append(random.randint(1, 100))

def seleccion(lista):
    comparaciones = 0
    cambios = 0

    tamanio=len(lista)
    for i in range(0,tamanio):
        min=i
        for j in range(i+1,tamanio):
            if lista[min]>lista[j]:
                min=j
                comparaciones += 1
        aux=lista[i]
        lista[i]=lista[min]
        lista[min]=aux
        cambios += 1

    print(f"\nCambios: {cambios}\nComparaciones: {comparaciones}\n")
    return lista

def burbuja(lista):
    cambios = 0
    comparaciones = 0

    for numPasada in range(len(lista)-1,0,-1):
        for i in range(numPasada):
            if lista[i]>lista[i+1]:
                comparaciones += 1
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                cambios +=1 

    print(f"\nCambios: {cambios}\nComparaciones: {comparaciones}\n")
    return lista

def burbuja_mejorada(lista):
    comparaciones = 0
    cambios = 0

    n = len(lista)
    
    cambios = 0
    comparaciones = 0
    cambio = True
    while cambio:
        cambio = False
       
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                comparaciones += 1
                lista[i], lista[i+1] = lista[i+1], lista[i]
                cambio = True
                cambios += 1
        n -= 1
    print(f"\nCambios: {cambios}\nComparaciones: {comparaciones}\n")
    return lista

def mostrarLista(lista):
    for numero in lista:
        print(numero, end=" ,")    

print("Estructura de ordenamiento selección\n")
lista = seleccion(randomNumber)
mostrarLista(lista)

print("\nEstructura de ordenamiento Burbuja\n")
lista = burbuja(randomNumber)
mostrarLista(lista)

print("\nEstructura de ordenamiento Burbuja mejorada\n")
lista = burbuja_mejorada(randomNumber)
mostrarLista(lista)

            


