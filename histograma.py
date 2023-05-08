pesosAlumnos = []
contarPesos = {}
answer = ''
alumno = 0

print("Histograma\n")
while (answer != 'n'):
    
    alumno += 1
    try:
        NumeroPeso = int(input(f"Escribe el peso del alumno #{alumno}: "))
    except:
        print("Solo numeros enteros")
        break

    if (NumeroPeso >= 10 and NumeroPeso <= 100):
        pesosAlumnos.append(NumeroPeso)
    else:
        print("\nEl peso debe ser entre 10 y 100 kg")
        break

    answer = input("Desea continuar con el programa s/n: ")

for peso in pesosAlumnos:
    if peso in contarPesos:
        contarPesos[peso] += "*"
    else:
        contarPesos[peso] = "*"

print("\n Peso      Numero de alumnos")
print("-------------------------------")
for peso, cantidad in contarPesos.items():
    print(f"  {peso}       {cantidad}")
