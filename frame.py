from tkinter import*
import tkinter as tk

root = Tk()
root.title("Frame")
root.geometry("400x600")

frame1 = Frame(root, bg="blue")
frame1.pack(expand=True,fill="both")

frame2 = Frame(root,bg="black", cursor="spider")
frame2.pack(expand=True, fill="both")

boton1 = tk.Button(frame2, text="Hola")
boton1.pack(expand=True,side="right")


root.mainloop()