#buscador del numero mayor con 3 numeros enteros
n1 = 0
n2 = 0
n3 = 0
n1 = int (input("Ingrese el primer numero entero: "))
n2 = int (input("Ingrese el segundo numero entero: "))
n3 = int (input("Ingrese el tercer numero entero: "))

if (n2 < n1 > n3):
    print ("El numero mayor es: ",n1)
elif (n1 < n2 > n3):
    print ("El numero mayor es: ",n2)
elif  (n1 < n3 > n2):
    print ("El numero mayor es: ",n3)
else:
    print("Error, por favor intente de nuevo")