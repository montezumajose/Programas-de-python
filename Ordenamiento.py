datosCero = []


numero = int (input("¿Cuantos numeros vas a ingresar?: "))
for n in range(numero):
   datosCero.append (int (input(f"Ingrese el numero {n+1}: ")))
datosUno = datosCero.copy()
datosDos = datosCero.copy()
datosTres = datosCero.copy()
datosCuatro = datosCero.copy()

def seleccion(lista):
    comparaciones = 0

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
        

    print(f"\nComparaciones: {comparaciones}")
    return lista



def insercionDirecta(lista):
    comparaciones = 0

    for i in range(1,len(lista)):
        v=lista[i]
        j=i-1
        while j >= 0 and lista[j] > v:
            lista[j+1] = lista[j]
            j=j-1
            comparaciones += 1
        lista[j+1]=v

    print(f"\nComparaciones: {comparaciones}")
    return lista

def burbuja(lista):
    comparaciones = 0

    for pasada in range(len(lista)-1,0,-1):
        for i in range(pasada):
            if lista[i]>lista[i+1]:
                
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
                comparaciones +=1 

    print(f"\nComparaciones: {comparaciones}")
    return lista

def insercionDirecta(lista, tam):
    comparaciones = 0
    for i in range(1,tam):
        v=lista[i]
        j=i-1
        while j >= 0 and lista[j] > v:
            lista[j+1] = lista[j]
            j=j-1
            comparaciones += 1
        lista[j+1]=v 
    print(f"\nComparaciones: {comparaciones}")   

def imprimeLista(lista,tam):
    for i in range(0,tam):
        print (lista[i])

#Ordenamiento por seleccion
print("ordenamiento seleccion: ",datosUno)
seleccionList = datosCero
seleccion (seleccionList)
print(seleccionList)

print("\n\n")

#ordenamiento por Burbuja
print("Ordenamiento Burbuja: ",datosDos)
seleccionListDos = datosDos
burbuja (seleccionListDos)
print(seleccionListDos)

print("\n\n")

#ordenamiento por insercion directa
print("\nInsercion directa",datosTres)
seleccionListTres = datosTres
burbuja (seleccionListTres)
print(seleccionListTres)

print("\n\n")

"""#Ordenamiento por rapido
print("\nOrdenamiento rapido: ",datosCuatro)
seleccionListaCuatro=datosCuatro
insercionDirecta(seleccionListaCuatro,len(seleccionListaCuatro))
imprimeLista(seleccionListaCuatro,len(seleccionListaCuatro))"""





