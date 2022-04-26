n1 = 0.0
n2 = 0.0
resultado = 0

n1 = int(input("Ingrese el dividendo: "))
n2 = int(input("Ingrese el divisor: "))

if n2 == 0:
    print ("Error, por favor ingrese otro numero que no sea 0")
elif n1 or n2 != 0:
    resultado = n1/n2
    resultado = round (resultado,2)
    print (n1," / ",n2," = ",resultado)
else:
    print("Error intente de nuevo")