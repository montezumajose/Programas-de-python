precio = 0.0
descuento = 0.0
total_a_pagar = 0.0

precio = float(input("Ingrese precio total a pagar: "))

if precio >= 151:
    descuento = precio * 0.15
    total_a_pagar = precio - descuento
    total_a_pagar = round (total_a_pagar,2)
    print ("Precio total a pagar: ",precio)
    print ("Monto a cobrar: ",total_a_pagar)
elif precio <= 150:
    descuento = precio * 0.1
    total_a_pagar = precio - descuento
    total_a_pagar = round (total_a_pagar,2)
    print ("Precio total a pagar: ",precio)
    print ("Monto a cobrar: ",total_a_pagar)
else:
    print ("Error, por favor introduzca un precio")