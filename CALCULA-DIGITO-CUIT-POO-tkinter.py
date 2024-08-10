import tkinter as tk
from tkinter import messagebox

class Ventana:

    def __init__(self, ventana1):
        self.ventana1 = ventana1
        self.prefi = ""

        self.ventana1.geometry("600x300+100+100")
        self.ventana1.title("OBTENER CUIT CUIL")
        self.label1 = tk.Label(self.ventana1, text="Ingrese opción")
        self.label1.grid(column=1, row=3)

        self.seleccion = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.ventana1,
                                     text="Masculino",
                                     justify="left",
                                     width="20",
                                     variable=self.seleccion,
                                     value=1)
        self.radio1.grid(column=1, row=4)

        self.radio2 = tk.Radiobutton(self.ventana1,
                                     text="Femenino",
                                     justify="left",
                                     width="20",
                                     variable=self.seleccion,
                                     value=2)
        self.radio2.grid(column=1, row=5)

        self.radio3 = tk.Radiobutton(self.ventana1,
                                     text="Empresa",
                                     justify="left",
                                     width="20",
                                     variable=self.seleccion,
                                     value=3)
        self.radio3.grid(column=1, row=6)

        self.label2 = tk.Label(self.ventana1,
                               text="Ingrese número de documento")
        self.label2.grid(column=1, row=9)

        self.label3 = tk.Label(self.ventana1, text="")
        self.label3.grid(column=1, row=16)

        self.label4 = tk.Label(self.ventana1, text="")
        self.label4.grid(column=1, row=18)

        self.dni = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana1,
                               width=8,
                               textvariable=self.dni)
        self.entry1.grid(column=2, row=9)

        self.botones()

    def botones(self):
        self.boton1 = tk.Button(self.ventana1, text="Obtener", command=self.valida)
        self.boton1.grid(column=3, row=27)
        self.boton2 = tk.Button(self.ventana1, text="Salir", command=self.salida)
        self.boton2.grid(column=3, row=30)

        self.ventana1.mainloop()

    def valida(self):
        self.label4.configure(text="")
        dni1 = self.dni.get()
        if len(dni1) != 8:
            texto_error = "Debe ingresar 8 dígitos"
            messagebox.showerror("Error", texto_error)
        elif not dni1.isnumeric():
            texto_error = "Debe ingresar solo números"
            messagebox.showerror("Error", texto_error)
        else:
            self.label3.configure(text="")
            self.selecciona()

    def selecciona(self):
        if self.seleccion.get() == 1:
            self.prefi = "20"
        elif self.seleccion.get() == 2:
            self.prefi = "27"
        else:
            self.prefi = "30"

        self.cuit = self.prefi + self.dni.get()
        algoritmo_cuit = (int(self.cuit[0]) * 5 +
                          int(self.cuit[1]) * 4 +
                          int(self.cuit[2]) * 3 +
                          int(self.cuit[3]) * 2 +
                          int(self.cuit[4]) * 7 +
                          int(self.cuit[5]) * 6 +
                          int(self.cuit[6]) * 5 +
                          int(self.cuit[7]) * 4 +
                          int(self.cuit[8]) * 3 +
                          int(self.cuit[9]) * 2) % 11

        if algoritmo_cuit == 0:
            digv = algoritmo_cuit
        elif algoritmo_cuit == 1 and self.prefi == '20':
            digv = 9
            self.prefi = '23'
        elif algoritmo_cuit == 1 and self.prefi == '27':
            digv = 4
            self.prefi = '23'
        else:
            digv = 11 - algoritmo_cuit

        numCUIT = f"Su número de CUIT es: {self.prefi}-{self.dni.get()}-{str(digv)}"
        self.label4.configure(text=numCUIT)

    def salida(self):
        self.ventana1.destroy()



if __name__ == '__main__':
    raiz = tk.Tk()
    a = Ventana(raiz)



