resul = 0
num = []
print("Transformar BINARIO >>> DECIMAL")
numero = input("Ingrese numero binario: ")
for i in range (len(numero)-1,-1,-1):
    num.append(int(i))
for j in range(0, len(numero)):
    datos = int(numero[j])*2**num[j]
    resul =  resul + datos
print(resul," Decimal")