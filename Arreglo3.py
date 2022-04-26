'''
Se hizo un arreglo de 5 valores numericos, en este caso son enteros y luego en el segundo arreglo se colocó
el orden invertido, gracias al ciclo for y el resultado sale en pantalla (Se muestran los dos arreglos).
'''
arreglo1 =[24,67,8,12,45]
arreglo2 =[]
contador = 5
'''
for i in range (4,-1,-1):
    num = arreglo1 [i]
    arreglo2.append(num)
print(arreglo1),print(arreglo2)
'''
while contador != 0:
    contador = contador -1
    print(contador)
    numero = arreglo1 [contador]
    arreglo2.append(numero)
print(arreglo1),print(arreglo2)