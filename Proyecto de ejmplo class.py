class compra:
    arreglo_Nombre = []
    arreglo_Precio = []
    NumArt = []
    total = 0.0
    tx = ""

    def __init__(self):
        while self.tx != "0":
            self.arreglo1 = str (input ("Ingrese el nombre del producto: "))
            self.arreglo_Nombre.append(self.arreglo1)

            self.arreglo2 = float (input("Ingrese el precio del producto: "))

            self.Numero_art = int(input("Cuantos producto va a comprar: "))
            self.NumArt.append(self.Numero_art)
            
            if self.Numero_art >= 1:
                self.multi =  self.arreglo2 * self.Numero_art
                self.arreglo_Precio.append(self.multi)
            self.tx = input("Ingrese 0 para terminar o 1 para seguir agregando shop: ")

        for i in range (len (self.arreglo_Precio)):
            self.total = self.total + self.arreglo_Precio[i]

        print("Producto(s):\n")
        for j in range(0,len(self.arreglo_Nombre)):
            print("X",self.NumArt[j], self.arreglo_Nombre[j]," $",self.arreglo_Precio[j])
        print ("\nTotal: ","$",round(self.total,2))
def main():
    a = compra()
    while True:
        Choise = str(input("Desea realizar otra compra Si(S) y No (N): "))
        if Choise == "S":
            a.arreglo_Nombre.clear ()
            a.arreglo_Precio.clear()
            compra()
        else:
            break

if __name__ == "__main__":
    main()
