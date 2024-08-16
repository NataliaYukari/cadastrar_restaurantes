from RestauranteController import Controller
from RestauranteView import View
from RestauranteModel import Model
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    model = Model(user="root", password="1234", host="localhost", database="catalogo_restaurantes")
    view = View(root)

    controller = Controller(model, view)

    view.set_controller(controller)
    root.mainloop()