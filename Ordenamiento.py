
lista_personas = []


n = int(input("Ingrese la cantidad de personas que desea registrar: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre de la persona {i}: ")
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    persona = {"nombre": nombre, "edad": edad}  
    lista_personas.append(persona)  

for i in range(len(lista_personas)):
    min_idx = i
    for j in range(i + 1, len(lista_personas)):
        if lista_personas[j]["edad"] < lista_personas[min_idx]["edad"]:
            min_idx = j
    if min_idx != i:
        lista_personas[i], lista_personas[min_idx] = lista_personas[min_idx], lista_personas[i]

print("Lista de personas ordenada por edad (de menor a mayor):\n",lista_personas)
