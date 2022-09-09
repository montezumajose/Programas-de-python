datos = []
contador = 0
datos2 = []
datos.append(int(input("Ingrese numero: ")))
while True:
    if int(datos[contador]) != 0: 
        datos.append(datos[contador]/2)
        contador +=1
    else:
        break
for j in range(0,len(datos)):
    datos2.append(datos[j]%2)
for obj in range(len(datos2)-2,-1,-1):
    print (int(datos2[obj]),end ="")   
print("\n\nPrograma finalizado")