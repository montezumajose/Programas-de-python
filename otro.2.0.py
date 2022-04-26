contador = 0
resultado = 0
for i in range (1,151):
    contador = i % 2
    if contador != 0:
        resultado = contador + i
print ("la suma es de",resultado)