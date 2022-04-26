arreglo = [[]]
m = ""
while m != "S" :
    text = input("Ingrese nombre\n>>> ")
    arreglo.append(text)

    edad = int (input("ingrese edad\n>>> "))
    arreglo.append(text)

    m = input("Terminar\n>>> ")
print (arreglo)