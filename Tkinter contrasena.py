from ast import Constant
from asyncio import constants
from cProfile import label
from tkinter import*
import tkinter as tk
from tkinter.messagebox import showerror, showinfo
ventana = tk.Tk()
ventana.geometry ("320x450")
ventana.title ("Login")
ventana.config(bg="black")

mano = tk.StringVar()

def login():
    global mano
    contra = "hola"
    while str (mano.get()) != str(contra):
        showerror (title="Erro",message="Password Incorrecto")
        return (entradaContra)
    showinfo(title="correcto",
    message="Password Value")

entradaContra= tk.Entry(ventana, textvariable= mano)
entradaContra.grid()

botonLogin = tk.Button(ventana, text= "Login", command= login)
botonLogin.grid()


ventana.mainloop()