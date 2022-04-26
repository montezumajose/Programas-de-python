arreglo_impar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
total = 0

for i in range(0,len(arreglo_impar)):
    n = arreglo_impar[i]%2
    if n != 0:
        total = total + arreglo_impar [i]  
print(total)