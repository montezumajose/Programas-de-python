#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = ""
palabra = input("Ingrese una palabra: ")
lista = ""
contador = 0
#while contador < len(palabra):
#    lista = palabra [contador]
#    print (lista)
#    contador += 1

for i in range(len(palabra)-1,-1,-1):
    print (palabra[i])