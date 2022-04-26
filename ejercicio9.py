#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contra = "hola"
hola = ""
#identifica = input("Escribe la contrasena: ")
#if contra == identifica:
#    print ('Correcto')
#else:
#    print ("Incorrecto")

while hola != contra:
    hola = input ("Escribe la contrasena: ")
print ('Contrasena correcta')