'''
Se hizo un arreglo para que el usuario ingresara numeros enteros, pero el usuario antes debe de decir la cantidad 
de numeros a ingresar para que se puedan sumar los numeros ingresados en el arreglo. El resultado de la suma sale
en pantalla.
'''
suma = 0
arreglo_super = []
leer = 0
contador = 0
resultado = 0

leer = int(input("¿Cuántos números va a ingresar?: "))
while contador != leer:
    suma = int(input(f"Número {contador+1} : "))
    arreglo_super.append(suma)
    resultado = resultado + arreglo_super [contador]
    contador+= 1
print("La sumatoria es: ",resultado)