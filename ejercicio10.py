#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
numero = int(input("Digite un numero: "))

for i in range (2, numero):
   if numero%i == 0:
       break
if i+1 == numero:
    print(i)
    print (numero," Es un numero primo")
else:
    print(numero," No es un numero primo")
    print(i)
print(numero%i == 0)
print(i+1 == numero)