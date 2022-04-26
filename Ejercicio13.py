#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
texto = ""
salir = "salir"
while texto != salir:
    texto = input("Escribe algo y para salir es (salir): ")
    print(texto)
print("EXIT, THANKS")

#while True:
#    frase = input("Introduce algo: ")
#    if frase == "salir":
#        break
#    print(frase)