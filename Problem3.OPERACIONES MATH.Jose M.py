#Calculadora para operaciones simples y segun el tipo de dato numerico, en decimales o enteros (beta)
n1 = 0
n2 = 0
letra = ""
letra1 = ""
resultado = 0
letra = input ("Ingrese la letra para el tipo de calculo que desea relaizar, E (Numeros Enteros) / D (Numeros Decimales): ")
letra = letra.upper()
if letra == "E":
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    letra1 = input("Ingrese una letra; S (Suma), R (Resta), M (Multiplicacion), D (Division), RE (Residuo): ")
    letra1 = letra1.upper ()
    if letra1 == "S":
        resultado = n1 + n2
        print ("La suma de ",n1," y ",n2,"es igual a ",resultado)
    elif letra1 == "R":
        resultado = n1 - n2
        print ("La resta de ",n1," y ",n2,"es igual a ",resultado)
    elif letra1 == "M":
        resultado = n1 * n2
        print ("La multiplicacion de ",n1," y ",n2,"es igual a ",resultado)
    elif letra1 == "D":
        resultado = n1/n2
        print ("La división de ",n1," y ",n2,"es igual a ",resultado)
    elif letra1 == "RE":
        resultado = n1%n2
        print ("El residuo de ",n1," y ",n2,"es igual a ",resultado)
    else:
        print("Por favor, ingrese una letra correspondiente a la operación") 
elif letra == "D":
    n1 = float(input("Ingrese el primer numero: "))
    n2 = float(input("Ingrese el segundo numero: "))
    letra1 = input("Ingrese una letra; S (Suma), R (Resta), M (Multiplicacion), D (Division), RE (Residuo): ")
    letra1 = letra1.upper ()
    if letra1 == "S":
        resultado = n1 + n2
        resultado = round(resultado,2)
        print ("La suma de ",n1," y ",n2,"es igual a ",resultado)
    elif letra1 == "R":
        resultado = n1 - n2
        resultado = round(resultado,2)
        print ("La resta de ",n1," y ",n2,"es igual a ",resultado)
    elif letra1 == "M":
        resultado = n1 * n2
        resultado = round(resultado,2)
        print ("La multiplicacion de ",n1," y ",n2,"es igual a ",resultado)
    elif letra1 == "D":
        resultado = n1/n2
        resultado = round(resultado,2)
        print ("La división de ",n1," y ",n2,"es igual a ",resultado)
    elif letra1 == "RE":
        resultado = n1%n2
        resultado = round(resultado,2)
        print ("El residuo de ",n1," y ",n2,"es igual a ",resultado)
    else:
        print("Por favor, ingrese una letra correspondiente a la operación") 
else:
    print ("Por favor, seleccione una letra para realizar el tipo de calculo") 