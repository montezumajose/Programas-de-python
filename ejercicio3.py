#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas
numero = 0
resultado = 0
evaluacion = 0
numero = int (input("Ingrese un numero entero positivo, por favor: "))
for i in range(numero):
    resultado = i + 1
    evaluacion = resultado%2
    if evaluacion == 1:
        print (resultado)