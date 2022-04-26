arreglo =[23,1,45,78,90,13]
numero = 0
numero = int(input("Ingrese un numero: "))


for i in range(0,6):
    numa = arreglo[i]
    if numa == numero:
        break

if numa == numero:
    print("El numero ",numero," esta  en el espacio ",i)
else:
    print("No se encuentra")