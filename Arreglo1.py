#Dudo que fuera así profe, hice este por si acaso.
#arreglo0 = [23,56,34,12,78,26,567,67,98,100]
'''
Hice un algoritmo donde el usuario pueda agregar 10 números enteros (10  espacios) de forma aleatoria 
(que el mismo escogiera) en el arreglo y también que pueda ver lo que hay especificamente en el índice del array
y la otra opción para que pueda ver el arreglo completo.
'''
arreglo = []
posicion = 0
verArreglo = ""
respuesta = ""

for i in range(10):
    numero= int(input(f"Esbribe un número entero en el espacio {i+1}: "))
    arreglo.append (numero)

respuesta = input("¿Desea ver lo que tiene el arreglo según la posición? Sí (S) o No (Presione cualquier tecla): ")
respuesta = respuesta.capitalize()

if respuesta == "S":
    posicion =int(input("Ingrese el número de la posición que desea ver del arreglo (0-9):"))
    print("En la posición",posicion,"del arreglo está el número: ", arreglo[posicion])

verArreglo = input("¿Desea ver el arreglo? Sí (S) o No (Presione cualquier tecla): ")
verArreglo = verArreglo.capitalize()

if verArreglo == "S":
    print("Arreglo: ", arreglo)
else:
    print("Que tenga un buen día :)")

