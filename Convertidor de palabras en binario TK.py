from tkinter import*
import tkinter as tk
from tkinter.messagebox import showerror

root = tk.Tk()
root.geometry("800x560")
root.title("Convertidor de texto a code binary")
root.config(background= "#DBFF3D")

parrafo = tk.StringVar()

def ejecutar():
    arreglo_parrafo = []
    binario = []
    tx = ""

    for i in range(0,len(parrafo.get())):
        arreglo = parrafo.get()[i]
        arreglo_parrafo.append(arreglo)

        if arreglo_parrafo [i] == ",":
            bina = "00101100"
            binario.append(bina)
        elif arreglo_parrafo [i] == ".":
            bina = "00101110"
            binario.append(bina)
        elif arreglo_parrafo [i] == ";":
            bina = "00111011"
            binario.append(bina)
        elif arreglo_parrafo [i] == ":":
            bina = "00111010"
            binario.append(bina)
        elif arreglo_parrafo [i] == '"':
            bina = "00100010"
            binario.append(bina)
        elif arreglo_parrafo [i] == " ":
            bina = "00100000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "A":
            bina = "01000001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Á":
            bina = "11000001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "B":
            bina = "01000010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "C":
            bina = "01000011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "D":
            bina = "01000100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "E":
            bina = "01000101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "É":
            bina = "11001001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "F":
            bina = "01000110"
            binario.append(bina)
        elif arreglo_parrafo [i] == "G":
            bina = "01000111"
            binario.append(bina)
        elif arreglo_parrafo [i] == "H":
            bina = "01001000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "I":
            bina = "01001001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Í":
            bina = "11001101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "J":
            bina = "01001010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "K":
            bina = "01001011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "L":
            bina = "01001100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "M":
            bina = "01001101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "N":
            bina = "01001110"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Ñ":
            bina = "11010001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "O":
            bina = "01001111"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Ó":
            bina = "11010011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "P":
            bina = "01010000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Q":
            bina = "01010001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "R":
            bina = "01010010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "S":
            bina = "01010011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "T":
            bina = "01010100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "U":
            bina = "01010101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Ú":
            bina = "11011010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Ü":
            bina = "11011100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "V":
            bina = "11011100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "W":
            bina = "01010111"
            binario.append(bina)
        elif arreglo_parrafo [i] == "X":
            bina = "01011000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Y":
            bina = "01011001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "Z":
            bina = "01011010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "a":
            bina = "01100001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "á":
            bina = "11100001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "b":
            bina = "01100010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "c":
            bina = "01100011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "d":
            bina = "01100100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "e":
            bina = "01100101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "é":
            bina = "11101001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "f":
            bina = "01100110"
            binario.append(bina)
        elif arreglo_parrafo [i] == "g":
            bina = "01100111"
            binario.append(bina)
        elif arreglo_parrafo [i] == "h":
            bina = "01101000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "i":
            bina = "01101001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "í":
            bina = "11101101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "j":
            bina = "01101010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "k":
            bina = "01101011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "l":
            bina = "01101100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "m":
            bina = "01101101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "n":
            bina = "01101110"
            binario.append(bina)
        elif arreglo_parrafo [i] == "ñ":
            bina = "11110001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "o":
            bina = "01101111"
            binario.append(bina)
        elif arreglo_parrafo [i] == "ó":
            bina = "11110011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "p":
            bina = "01110000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "q":
            bina = "01110001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "r":
            bina = "01110010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "s":
            bina = "01110011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "t":
            bina = "01110100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "u":
            bina = "01110101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "ú":
            bina = "11111010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "ü":
            bina = "11111100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "v":
            bina = "01110110"
            binario.append(bina)
        elif arreglo_parrafo [i] == "w":
            bina = "01110111"
            binario.append(bina)
        elif arreglo_parrafo [i] == "x":
            bina = "01111000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "y":
            bina = "01111001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "z":
            bina = "01111001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "0":
            bina = "00110000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "1":
            bina = "00110001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "2":
            bina = "00110010"
            binario.append(bina)
        elif arreglo_parrafo [i] == "3":
            bina = "00110011"
            binario.append(bina)
        elif arreglo_parrafo [i] == "4":
            bina = "00110100"
            binario.append(bina)
        elif arreglo_parrafo [i] == "5":
            bina = "00110101"
            binario.append(bina)
        elif arreglo_parrafo [i] == "6":
            bina = "00110110"
            binario.append(bina)
        elif arreglo_parrafo [i] == "7":
            bina = "00110111"
            binario.append(bina)
        elif arreglo_parrafo [i] == "8":
            bina = "00111000"
            binario.append(bina)
        elif arreglo_parrafo [i] == "9":
            bina = "00111001"
            binario.append(bina)
        elif arreglo_parrafo [i] == "10":
            bina = "00111010"
            binario.append(bina)
        else:
            print(showerror("Error", f"Hay signos que no se pueden traducir como {arreglo_parrafo[i]}"))
            break

    for j in range (0, len (binario)):
        tx += binario[j]
    SalidaTexto.insert(END, tx)

def copiar_al_portapapeles():
    root.clipboard_clear()
    copiar = SalidaTexto.get("1.0", "end")
    root.clipboard_append(copiar)

def limpiarTodo ():
    EntradaTexto.delete("0", "end")
    SalidaTexto.delete("1.0", "end")

def salir():
    root.destroy()

etiqueta1 = Label (root, text="Ingrese Texto", bg= "#00FFDD", font="Caslon 11 bold", borderwidth= 2, relief= "groove", fg="#000000")
etiqueta1.place(relheight= 0.04, relwidth= 0.19, relx= 0.35, rely= 0.15)

EntradaTexto = tk.Entry(root, textvariable= parrafo, bg="#EFFFFD", borderwidth = 3, relief= "solid", fg= "#002366", font="Rockwell 14")
EntradaTexto.place(relheight= 0.1, relwidth= 0.3, relx= 0.35, rely= 0.2)

EjecutarFuncion = tk.Button(root, text="Convertir", command= ejecutar, bg="#05DFD7",font="Caslon 11 bold", borderwidth= 2, relief= "groove", fg="#000000" )
EjecutarFuncion.place(relheight= 0.1, relwidth= 0.3, relx= 0.35, rely= 0.35)

SalidaTexto = tk.Text(root, width= 30, height= 10, bg="#EFFFFD", borderwidth = 3, relief= "solid", fg= "#002366", font="Rockwell 14")
SalidaTexto.place(relheight= 0.3, relwidth= 0.3, relx= 0.35, rely= 0.5)


copiar = Button(root, text="Copiar",command=copiar_al_portapapeles, bg="#05DFD7",font="Caslon 11 bold", borderwidth= 2, relief= "groove", fg="#000000")
copiar.place(relheight= 0.05, relwidth= 0.09, relx= 0.35, rely= 0.85)

limpiar = tk.Button(root, text="Limpiar", command= limpiarTodo, bg="#05DFD7",font="Caslon 11 bold", borderwidth= 2, relief= "groove", fg="#000000").place(relheight= 0.05, relwidth= 0.09, relx= 0.45, rely= 0.85)

salir = tk.Button(root, text= "Salir", command= salir, bg="#05DFD7",font="Caslon 11 bold", borderwidth= 2, relief= "groove", fg="#000000").place(relheight= 0.05, relwidth= 0.09, relx= 0.55, rely= 0.85)

root.mainloop()