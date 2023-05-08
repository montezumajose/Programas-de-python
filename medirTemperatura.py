temperatures = []
answer = ''
person = 0
mayorGrado = 0
menorGrado = 0

print("Programa para registrar las temperaturas de las personas\n")

while (answer != 's'):

    try:
        person = person + 1
        temperatures.append(float(input(f"¿Cual es la temperatura de la persona #{person}?: ")))
    except:
        print("Solo se permiten numeros decimales")
        break
    
    answer = input("Desea terminar el programa s/n: ")

for i in range(0,len(temperatures)):
    if (temperatures[i] >= 37.0):
        mayorGrado += 1
    elif (temperatures[i] <= 33.0):
        menorGrado += 1
    
print("\nPersonas que ingresaron con una temperatura mayor a 37°C: ",mayorGrado)
print("Personas que ingresaron con una temperatura menor a 33°C: ",menorGrado)




