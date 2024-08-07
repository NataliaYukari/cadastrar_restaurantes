import RestauranteController as Controller
import tkinter as tk
import sys



class View:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x350")
        self.controller = Controller(self)

        #Valores que serão passados ao controller
        self.telaPrincipal()

        self.root.bind('<Escape>', self.close)
        self.root.mainloop()

    def telaPrincipal(self):
        container = tk.Frame(self.window)
        container.pack()

        labelTitulo = tk.Label(container, width=320, text="Bem-vindo ao Guia de restaurantes!")
        labelTitulo.grid(column=0, row=0, padx=5, pady=5)

        labelSubTitulo = tk.Label(container, width=185, text="Escolha sua opção abaixo: ")
        labelSubTitulo.grid(column=0, row=1, padx=5, pady=5)

        buttonNovoRestaurante = tk.Button(container, width=178, height=66, text="Novo restaurante")
        buttonNovoRestaurante.grid(column=0, row=2, padx=5, pady=5)

        buttonAlterarRestaurante = tk.Button(container, width=178, height=66, text="Alterar/Excluir restaurante")
        buttonAlterarRestaurante.grid(column=1, row=2, padx=5, pady=5)

        buttonVerRestaurante = tk.Button(container, width=178, height=66, text="Ver um restaurante")
        buttonVerRestaurante.grid(column=0, row=3, padx=5, pady=5)

        buttonListaRestaurantes = tk.Button(container, width=178, height=66, text="Lista de restaurantes")
        buttonListaRestaurantes.grid(column=1, row=3, padx=5, pady=5)

    def escolherOpcao(self):
        


