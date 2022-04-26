#Funcion <def compra()>, es la funcion que se encarga de realizar la lista de compra y todo el proceso de calculo.
def compra():
    #Variables para guardar informacion
    arreglo_Nombre = []
    arreglo_Precio = []
    NumArt = []
    total = 0.0
    Choice = ""
    tx = ""
    #El ciclo while recoje la informacion de los productos, mediante el metodo append (captura la informacion de la variable temporal)
    #Se ejecuta las veces que sean necesarias hasta que su condicion sea falsa este rompera el ciclo.
    while tx != "0":
        arreglo1 = str (input ("\nIngrese el nombre del producto: "))
        arreglo1 = arreglo1.capitalize()
        arreglo_Nombre.append(arreglo1)
        
        arreglo2 = float (input("\nIngrese el precio del producto: "))
        
        Numero_art = int(input("\n¿Cuántos va a comprar?: "))
        NumArt.append(Numero_art)
        #Este if se encarga de validar la informacion y multiplica el precio del producto ingresado por las veces que se va a comprar, 
        #despues lo almacena en el arreglo mediante el metodo append. 
        if Numero_art >= 1:
            multi = round (arreglo2 * Numero_art,2)
            arreglo_Precio.append(multi)
        else:
            print("Error, por favor ingrese un número que no sea 0")
        #Este input <tx> hace que el ciclo while siga o termine.
        tx = input("\nIngrese (0) para terminar o (1) para seguir agregando: ")
    #Este for hace un recorrido mediante el rango de 0 al espacio de la lista, su funcion es la sumatoria mediante el indice de la lista.
    for i in range (0,len (arreglo_Precio)):
        total = total + arreglo_Precio[i]
    #Aqui ocurre la impresion de los productos, precios y cuantas veces fue comprada. Mediante el ciclo for vamos imprimiendola
    #y para tener toda la informacion en una fila del mismo indice, se usa un rango de 0 al espacio del arreglo.
    print("\nProducto (s):\n")
    for j in range(0,len(arreglo_Nombre)):
        print("X",NumArt[j], arreglo_Nombre[j]," $",arreglo_Precio[j])
    print ("\nTotal: ","$",round(total,2))
    #<Choise> captura la informacion de formato string para usarla en el if y el metodo capitalize convierte la primera letra en Mayuscula.
    Choice = str(input("\n¿Desea realizar otra compra? Sí (S) o No (N): "))
    Choice = Choice.capitalize()
    #Este if valida la informacion de la variable. Para ver si se ejecuta el programa de nuevo o no. Todo de depende de la variable <Choise>
    #Si se ejecuta de nuevo, entonces con el metodo clear borra los datos almacenados en los arreglos.
    if Choice == "S":
        arreglo_Nombre.clear()
        arreglo_Precio.clear()
        NumArt.clear()
        compra()
    else:
        print ("\nHasta luego :)")
#Este if hace que la funcion se ejecute.
if __name__ == "__main__":
    compra()    