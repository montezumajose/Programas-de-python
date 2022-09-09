resultados = []
residuos = []
resultados.append(int(input("Inserte numero: ")))
contador = 0
while True:
    resul = resultados[contador]/16
    resultados.append(resul)
    contador += 1
    if float(resul) < 1:
        break
for i in range(0, len(resultados)-1):
    residuos.append(int(resultados[i] % 16))
print("Convertir Decimal >>> Hexadecimal\n")
for a in range(len(residuos)-1, -1, -1):
    if residuos[a] == 10:
        print("A", end="")
    elif residuos[a] == 11:
        print("B", end="")
    elif residuos[a] == 12:
        print("C", end="")
    elif residuos[a] == 13:
        print("D", end="")
    elif residuos[a] == 14:
        print("E", end="")
    elif residuos[a] == 15:
        print("F", end="")
    elif residuos[a] == 16:
        print("G", end="")
    elif residuos[a] == 17:
        print("H", end="")
    elif residuos[a] == 18:
        print("I", end="")
    elif residuos[a] == 19:
        print("J", end="")
    elif residuos[a] == 20:
        print("K", end="")
    elif residuos[a] == 21:
        print("L", end="")
    elif residuos[a] == 22:
        print("M", end="")
    elif residuos[a] == 23:
        print("N", end="")
    elif residuos[a] == 24:
        print("Ñ", end="")
    elif residuos[a] == 25:
        print("O", end="")
    elif residuos[a] == 26:
        print("P", end="")
    elif residuos[a] == 27:
        print("Q", end="")
    elif residuos[a] == 28:
        print("R", end="")
    elif residuos[a] == 29:
        print("S", end="")
    elif residuos[a] == 30:
        print("T", end="")
    elif residuos[a] == 31:
        print("U", end="")
    elif residuos[a] == 32:
        print("V", end="")
    elif residuos[a] == 33:
        print("W", end="")
    elif residuos[a] == 34:
        print("X", end="")
    elif residuos[a] == 35:
        print("Y", end="")
    elif residuos[a] == 36:
        print("Z", end="")
    else:
        print(residuos[a], end="")
print("\n\n")