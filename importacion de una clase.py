import tkinter as tk
from POO import lamparas

def resultado1():
    a = lamparas(palanca = False)
    b = lamparas(palanca=True)
    while True:
        tx = input("\n\nMenu \n\n 1 para prender \n\n 0 para apagar \n\n x para terminar \n\n >>> ")
        if tx == "0":
            a.interructor()
        elif tx == "1":
            b.interructor()
        else:
            break
    print("Termino")
vent = tk.Tk()
vent.geometry("400x300")

boton = tk.Button(text="Resultado",command=resultado1)
boton.pack(expand= True, fill="both")

vent.mainloop()