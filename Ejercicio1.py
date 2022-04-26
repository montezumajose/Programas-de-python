#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = ""
contador = 0
palabra = input("Ingrese una palabra: ")
for i in range (10):
    contador += 1
    print (palabra,"=",contador)
    