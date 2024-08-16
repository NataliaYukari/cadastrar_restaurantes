import RestauranteController as Controller
from RestauranteController import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Toplevel
from tkinter import messagebox
import sys



class View:
    def __init__(self, root):
        self.controller = None

        #Elementos usados no componentes
        #Cores
        self.yellow = "#FBEA91"
        self.orange = "#FBD26A"
        self.red = "#FF7E36"
        self.darkyellow = "#FFE457"
        self.white = "#FFFFFF"

        #Fontes
        self.fonteT1 = ("Times New Roman", 20, "bold")
        self.fonteT2 = ("Times New Roman", 18, "bold")
        self.fonteT3 = ("Times New Roman", 16)
        self.fonteT4 = ("Times New Roman", 16, "bold")

        self.root = root
        self.root.title("Catálogo de restaurantes")
        self.root.configure(bg=self.yellow)
        self.root.geometry("500x550")

        #Valores que serão passados ao controller
        self.telaPrincipal()
        # self.telaAlterar()
        # self.telaConsulta()
        # self.telaLista()
        # self.alertSucesso("Cadastro")

    def set_controller(self, controller):
        self.controller = controller

    def telaPrincipal(self):

        #Definindo o tamanho dos botões
        largura = 13
        altura = 2

        #Tamanho de margem
        margemx= 20
        margemy = 20

        self.frameTelaPrincipal = tk.Frame(self.root, bg=self.yellow)
        self.frameTelaPrincipal.pack(fill="both", expand=True)

        topContainer = tk.Frame(self.frameTelaPrincipal, bg=self.yellow)
        topContainer.pack()

        labelTitulo = tk.Label(topContainer, text="Bem-vindo ao guia de restaurantes!", font=self.fonteT1, bg=self.yellow)
        labelTitulo.pack(padx=10, pady=(120, 10))
        labelSubTitulo = tk.Label(topContainer, text="Escolha sua opção abaixo: ", font=self.fonteT2, bg=self.yellow)
        labelSubTitulo.pack()

        bottomContainer = tk.Frame(self.frameTelaPrincipal, bg=self.yellow)
        bottomContainer.pack(pady=15, padx=15)

        buttonNovoRestaurante = tk.Button(bottomContainer, width=largura, height=altura, text="Novo restaurante", font=self.fonteT3, bg=self.orange,
                                          command=lambda: self.escolherOpcao("novo"))
        buttonNovoRestaurante.grid(column=0, row=0, padx=margemx, pady=margemy, sticky="nsew")

        buttonAlterarRestaurante = tk.Button(bottomContainer, width=largura, height=altura, text="Alterar/Excluir \nrestaurante", font=self.fonteT3, bg=self.orange,
                                             command=lambda: self.escolherOpcao("alterar"))
        buttonAlterarRestaurante.grid(column=1, row=0, padx=margemx, pady=margemy, sticky="nsew")

        buttonVerRestaurante = tk.Button(bottomContainer, width=largura, height=altura, text="Ver um \nrestaurante", font=self.fonteT3, bg=self.orange,
                                         command=lambda: self.escolherOpcao("ver"))
        buttonVerRestaurante.grid(column=0, row=1, padx=margemx, pady=margemy, sticky="nsew")

        buttonListaRestaurantes = tk.Button(bottomContainer, width=largura, height=altura, text="Lista de \nrestaurantes", font=self.fonteT3, bg=self.orange,
                                            command=lambda: self.escolherOpcao("lista"))
        buttonListaRestaurantes.grid(column=1, row=1, padx=margemx, pady=margemy, sticky="nsew")

        self.root.bind('<Escape>', self.close)

    def escolherOpcao(self, opcao):
        #Encaminha para o controller a opção escolhida na tela principal
        self.controller.escolherOpcao(opcao)

    def telaCadastro(self):
        self.frameTelaPrincipal.pack_forget()

        self.frameTelaCadastro = tk.Frame(self.root, bg=self.yellow)
        self.frameTelaCadastro.pack(fill="both", expand=True)

        #Tamanho dos componentes
        largura = 18
        altura= 2

        #Tamanho de margem
        margemx = 10
        margemy = 5

        topContainer = tk.Frame(self.frameTelaCadastro, bg=self.yellow)
        topContainer.pack()
        labelTitulo = tk.Label(topContainer, text="Cadastro de novo restaurante", font=self.fonteT2, bg=self.yellow)
        labelTitulo.pack(padx=10, pady=(20, 10))

        bottomContainer = tk.Frame(self.frameTelaCadastro, bg=self.yellow)
        bottomContainer.pack(padx=10, pady=10)

        labelNome = tk.Label(bottomContainer, width=largura, text="Nome do restaurante: ", font=self.fonteT3, bg=self.yellow)
        labelNome.grid(column=0, row=0, padx=margemx, pady=margemy, sticky="e")

        self.entryNome = tk.Entry(bottomContainer, width=largura, font=self.fonteT3, bg=self.white)
        self.entryNome.grid(column=0, row=1, padx=margemx, pady=margemy, sticky="nsew")

        labelLocalizacao = tk.Label(bottomContainer, width=largura, height=altura, text="Localização: ", font=self.fonteT3, bg=self.yellow)
        labelLocalizacao.grid(column=0, row=2, padx=margemx, pady=margemy, sticky="w")

        self.entryLocalizacao = tk.Entry(bottomContainer, width=largura, font=self.fonteT3, bg=self.white)
        self.entryLocalizacao.grid(column=0, row=3, padx=margemx, pady=margemy, sticky="nsew")       

        labelNota = tk.Label(bottomContainer, width=largura, height=altura, text="Nota: ", font=self.fonteT3, bg=self.yellow)
        labelNota.grid(column=0, row=4, padx=margemx, pady=margemy, sticky="w")

        #Radiobutton de nota
        radioContainer = tk.Frame(bottomContainer, bg=self.yellow)
        radioContainer.grid(column=0, row=5, padx=5, pady=5)

        self.radioNota = tk.IntVar()
        self.radioNota.set(None)
        radio1 = tk.Radiobutton(radioContainer, text="1", variable=self.radioNota, value=1, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        radio1.grid(column=0, row=0, padx=1, pady=1)

        radio2 = tk.Radiobutton(radioContainer, text="2", variable=self.radioNota, value=2, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        radio2.grid(column=1, row=0, padx=1, pady=1)
        
        radio3 = tk.Radiobutton(radioContainer, text="3", variable=self.radioNota, value=3, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        radio3.grid(column=2, row=0, padx=1, pady=1)

        radio4 = tk.Radiobutton(radioContainer, text="4", variable=self.radioNota, value=4, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        radio4.grid(column=3, row=0, padx=1, pady=1)

        radio5 = tk.Radiobutton(radioContainer, text="5", variable=self.radioNota, value=5, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        radio5.grid(column=4, row=0, padx=1, pady=1)

        labelCategoria = tk.Label(bottomContainer, width=largura, height=altura, text="Categoria: ", font=self.fonteT3, bg=self.yellow)
        labelCategoria.grid(column=1, row=0, padx=margemx, pady=margemy, sticky="w")

        #Combobox de categoria de restaurante
        self.categoria = tk.StringVar()
        comboCategoria = ttk.Combobox(bottomContainer, width=largura, font=self.fonteT3, textvariable=self.categoria,
                                      values=["Familiar/Casual", "Fast Food", "Café", "Luxo", "Clássico "])
        comboCategoria.grid(column=1, row=1, padx=margemx, pady=margemy, sticky="nsew")

        labelCulinaria = tk.Label(bottomContainer, width=largura, height=altura, text="Culinária servida: ", font=self.fonteT3, bg=self.yellow)
        labelCulinaria.grid(column=1, row=2, padx=margemx, pady=margemy, sticky="w")

        self.entryCulinaria = tk.Entry(bottomContainer, width=largura, font=self.fonteT3, bg=self.white)
        self.entryCulinaria.grid(column=1, row=3, padx=margemx, pady=margemy, sticky="nsew")  

        labelPreco = tk.Label(bottomContainer, width=largura, height=altura, text="Faixa de preço: ", font=self.fonteT3, bg=self.yellow)
        labelPreco.grid(column=1, row=4, padx=margemx, pady=margemy, sticky="w")

        #Combobox de faixa de preço
        self.preco = tk.StringVar()
        comboPreco = ttk.Combobox(bottomContainer, width=largura, font=self.fonteT3, textvariable=self.preco,
                                  values=["$", "$$", "$$$"])
        comboPreco.grid(column=1, row=5, padx=margemx, pady=margemy)

        #Botões
        buttonCadastro = tk.Button(bottomContainer, width=12, height=2, font=self.fonteT4, text="Cadastrar", bg=self.orange,
                                   command=self.cadastrarRestaurante)
        buttonCadastro.grid(column=0, row=6, padx=margemx, pady=40, sticky="e")

        buttonVoltar = self.buttonRetornar(bottomContainer, self.frameTelaCadastro)
        buttonVoltar.grid(column=1, row=6, padx=margemx, pady=40, sticky="w")

    def cadastrarRestaurante(self):
        nome = self.entryNome.get()
        localizacao = self.entryLocalizacao.get()
        nota = self.radioNota.get()
        categoria = self.categoria.get()
        culinaria = self.entryCulinaria.get()
        preco = self.preco.get()

        # CARECE DE CONFIRMAÇÃO 
        # Verifica se todos os campos foram preenchidos
        if nome and localizacao and nota and categoria and culinaria and preco:
            self.controller.cadastrarRestaurante(nome, localizacao, nota, categoria, culinaria, preco)
        else:
            self.alertErro(": preencha todos os campos")

    def telaAlterar(self, restaurante): 
        self.frameTelaPesquisa.pack_forget()

        self.frameTelaAlterar = tk.Frame(self.root, bg=self.yellow)
        self.frameTelaAlterar.pack(fill="both", expand=True)

        #Tamanho dos componentes
        largura = 18
        altura= 2

        #Tamanho de margem
        margemx = 10
        margemy = 5

        topContainer = tk.Frame(self.frameTelaAlterar, bg=self.yellow)
        topContainer.pack()
        labelTitulo = tk.Label(topContainer, text="Alterar/excluir restaurante", font=self.fonteT2, bg=self.yellow)
        labelTitulo.pack(padx=10, pady=(20, 10))

        bottomContainer = tk.Frame(self.frameTelaAlterar, bg=self.yellow)
        bottomContainer.pack(padx=10, pady=5)

        labelNome = tk.Label(bottomContainer, width=largura, text="Nome do restaurante: ", font=self.fonteT3, bg=self.yellow)
        labelNome.grid(column=0, row=0, padx=margemx, pady=margemy, sticky="e")

        self.entryNomeAlterar = tk.Entry(bottomContainer, width=largura, font=self.fonteT3, bg=self.white)
        self.entryNomeAlterar.grid(column=0, row=1, padx=margemx, pady=margemy, sticky="nsew")
        self.entryNomeAlterar.delete(0, tk.END)
        self.entryNomeAlterar.insert(0, restaurante['nome'])

        labelLocalizacao = tk.Label(bottomContainer, width=largura, height=altura, text="Localização: ", font=self.fonteT3, bg=self.yellow)
        labelLocalizacao.grid(column=0, row=2, padx=margemx, pady=margemy, sticky="w")

        self.entryLocalizacaoAlterar = tk.Entry(bottomContainer, width=largura, bg=self.white, font=self.fonteT3)
        self.entryLocalizacaoAlterar.grid(column=0, row=3, padx=margemx, pady=margemy, sticky="nsew")       
        self.entryLocalizacaoAlterar.delete(0, tk.END)
        self.entryLocalizacaoAlterar.insert(0, restaurante['localizacao'])

        labelNota = tk.Label(bottomContainer, width=largura, height=altura, text="Nota: ", font=self.fonteT3, bg=self.yellow)
        labelNota.grid(column=0, row=4, padx=margemx, pady=margemy, sticky="w")

        #Radiobutton de nota
        radioContainer = tk.Frame(bottomContainer, bg=self.yellow)
        radioContainer.grid(column=0, row=5, padx=5, pady=5)

        self.radioNotaAlterar = tk.IntVar()
        self.radioNotaAlterar.set(restaurante['nota'])
        self.radio1 = tk.Radiobutton(radioContainer, text="1", variable=self.radioNotaAlterar, value=1, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        self.radio1.grid(column=0, row=0, padx=1, pady=1)

        self.radio2 = tk.Radiobutton(radioContainer, text="2", variable=self.radioNotaAlterar, value=2, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        self.radio2.grid(column=1, row=0, padx=1, pady=1)
        
        self.radio3 = tk.Radiobutton(radioContainer, text="3", variable=self.radioNotaAlterar, value=3, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        self.radio3.grid(column=2, row=0, padx=1, pady=1)

        self.radio4 = tk.Radiobutton(radioContainer, text="4", variable=self.radioNotaAlterar, value=4, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        self.radio4.grid(column=3, row=0, padx=1, pady=1)

        self.radio5 = tk.Radiobutton(radioContainer, text="5", variable=self.radioNotaAlterar, value=5, font=self.fonteT3, bg=self.yellow, anchor=tk.W)
        self.radio5.grid(column=4, row=0, padx=1, pady=1)

        labelCategoria = tk.Label(bottomContainer, width=largura, height=altura, text="Categoria: ", font=self.fonteT3, bg=self.yellow)
        labelCategoria.grid(column=1, row=0, padx=margemx, pady=margemy, sticky="w")

        #Combobox de categoria de restaurante
        self.comboCategoriaAlterar = ttk.Combobox(bottomContainer, width=largura, font=self.fonteT3, values=["Familiar/Casual", "Fast Food", "Café", "Luxo", "Clássico "])
        self.comboCategoriaAlterar.grid(column=1, row=1, padx=margemx, pady=margemy, sticky="nsew")
        categorias = {1: "familiar/Casual", 2: "Fast Food", 3: "Café", 4: "Luxo", 5:"Clássico"}
        self.comboCategoriaAlterar.set(categorias.get(restaurante['id_categoria']))

        labelCulinaria = tk.Label(bottomContainer, width=largura, height=altura, text="Culinária servida: ", font=self.fonteT3, bg=self.yellow)
        labelCulinaria.grid(column=1, row=2, padx=margemx, pady=margemy, sticky="w")

        self.entryCulinariaAlterar = tk.Entry(bottomContainer, width=largura, font=self.fonteT3, bg=self.white)
        self.entryCulinariaAlterar.grid(column=1, row=3, padx=margemx, pady=margemy, sticky="nsew")  
        self.entryCulinariaAlterar.delete(0, tk.END)
        self.entryCulinariaAlterar.insert(0, restaurante['culinaria'])

        labelPreco = tk.Label(bottomContainer, width=largura, height=altura, text="Faixa de preço: ", font=self.fonteT3, bg=self.yellow)
        labelPreco.grid(column=1, row=4, padx=margemx, pady=margemy, sticky="w")

        #Combobox de faixa de preço
        self.comboPrecoAlterar = ttk.Combobox(bottomContainer, width=largura, font=self.fonteT3, values=["$", "$$", "$$$"])
        self.comboPrecoAlterar.grid(column=1, row=5, padx=margemx, pady=margemy)
        self.comboPrecoAlterar.set(restaurante['preco'])

        #Botões
        buttonContainer = tk.Frame(self.frameTelaAlterar, bg=self.yellow)
        buttonContainer.pack(padx=10, pady=5)

        buttonExcluir = tk.Button(buttonContainer, width=10, height=2, font=self.fonteT4, text="Excluir", bg=self.red,
                                  command=self.excluirRestaurante)
        buttonExcluir.grid(column=0, row=0, padx=margemx, pady=margemy)

        buttonCadastro = tk.Button(buttonContainer, width=10, height=2, font=self.fonteT4, text="Alterar", bg=self.orange,
                                   command=self.alterarRestaurante)
        buttonCadastro.grid(column=1, row=0, padx=margemx, pady=margemy)

        buttonVoltar = self.buttonRetornar(buttonContainer, self.frameTelaAlterar)
        buttonVoltar.grid(column=2, row=0, padx=margemx, pady=margemy)

    def alterarRestaurante(self):
        nome = self.entryNomeAlterar.get()
        localizacao = self.entryLocalizacaoAlterar.get()
        nota = self.radioNotaAlterar.get()
        categoria = self.comboCategoriaAlterar.get()
        culinaria = self.entryCulinariaAlterar.get()
        preco = self.comboPrecoAlterar.get()

        # CARECE DE CONFIRMAÇÃO 
        # Verifica se todos os campos foram preenchidos
        if nome and localizacao and nota and categoria and culinaria and preco:
            self.controller.alterarRestaurante(nome, localizacao, nota, categoria, culinaria, preco)
        else:
            self.alertErro(": preencha todos os campos")       

    def excluirRestaurante(self):
        nome = self.entryNomeAlterar.get()
        self.controller.excluirRestaurante(nome)

    def telaPesquisaAlterar(self):
        #Tamanho de margem
        margemx= 20
        margemy= 20

        self.frameTelaPrincipal.pack_forget()

        self.frameTelaPesquisa = tk.Frame(self.root, bg=self.yellow)
        self.frameTelaPesquisa.pack(fill="both", expand=True)

        topContainer = tk.Frame(self.frameTelaPesquisa, bg=self.yellow)
        topContainer.pack()

        labelNome = tk.Label(topContainer, text="Digite o nome do restaurante: ", font=self.fonteT2, bg=self.yellow)
        labelNome.pack(padx=margemx, pady=(140, 20))

        self.entryNomeAlterar = tk.Entry(topContainer, font=self.fonteT3, bg="white", width=50)
        self.entryNomeAlterar.pack(padx=margemx, pady=margemy)

        bottomContainer = tk.Frame(self.frameTelaPesquisa, bg=self.yellow)
        bottomContainer.pack()

        buttonPesquisar = tk.Button(bottomContainer, text="Pesquisar", font=self.fonteT4, bg=self.orange, width=12, height=2,
                                    command=self.buscarRestaurante)    
        buttonPesquisar.grid(column=0, row=0, padx=margemx, pady=margemy, sticky="w")

        buttonVoltar = self.buttonRetornar(bottomContainer, self.frameTelaPesquisa)
        buttonVoltar.grid(column=1, row=0, padx=margemx, pady=margemy, sticky="e")       

    def buscarRestaurante(self):
        nome_restaurante = self.entryNomeAlterar.get()
        self.controller.buscarRestaurante(nome_restaurante)

    def telaConsulta(self, restaurante):
        self.framePesquisaConsulta.pack_forget()

        self.frameTelaConsulta = tk.Frame(self.root, bg=self.yellow)
        self.frameTelaConsulta.pack(fill="both", expand=True) 

        #Medidas de margem
        margemx = 20
        margemy= 15

        topContainer = tk.Frame(self.frameTelaConsulta, bg=self.yellow)
        topContainer.pack()

        labelTitulo = tk.Label(topContainer, text="Consultar um restaurante", bg=self.yellow, font=self.fonteT2)
        labelTitulo.pack(padx=10, pady=(30, 10))

        midContainer = tk.Frame(self.frameTelaConsulta, bg=self.yellow)
        midContainer.pack(fill="both", expand=True)

        labelNome = tk.Label(midContainer, text="Nome do restaurante: ", bg=self.yellow, font=self.fonteT3)
        labelNome.grid(column=0, row=0, padx=margemx, pady=margemy, sticky="w") 

        outNome = tk.Label(midContainer, text=restaurante['nome'], bg=self.yellow, font=self.fonteT3)
        outNome.grid(column=1, row=0, padx=margemx, pady=margemy)

        labelCategoria = tk.Label(midContainer, text="Categoria: ", bg=self.yellow, font=self.fonteT3)
        labelCategoria.grid(column=0, row=1, padx=margemx, pady=margemy, sticky="w")

        categorias = {1: "familiar/Casual", 2: "Fast Food", 3: "Café", 4: "Luxo", 5:"Clássico"}
        outCategoria = tk.Label(midContainer, text=categorias.get(restaurante['id_categoria']), bg=self.yellow, font=self.fonteT3)
        outCategoria.grid(column=1, row=1, padx=margemx, pady=margemy)

        labelComida = tk.Label(midContainer, text="Comida: ", bg=self.yellow, font=self.fonteT3)
        labelComida.grid(column=0, row=2, padx=margemx, pady=margemy, sticky="w")

        outCulinaria = tk.Label(midContainer, text=restaurante['culinaria'], bg=self.yellow, font=self.fonteT3)
        outCulinaria.grid(column=1, row=2, padx=margemx, pady=margemy)       

        labelLocalizacao = tk.Label(midContainer, text="Localização: ", bg=self.yellow, font=self.fonteT3)
        labelLocalizacao.grid(column=0, row=3, padx=margemx, pady=margemy, sticky="w")

        outLocalizacao = tk.Label(midContainer, text=restaurante['localizacao'], bg=self.yellow, font=self.fonteT3)
        outLocalizacao.grid(column=1, row=3, padx=margemx, pady=margemy)

        labelPreco = tk.Label(midContainer, text="Faixa de preço: ", bg=self.yellow, font=self.fonteT3)
        labelPreco.grid(column=0, row=4, padx=margemx, pady=margemy, sticky="w")

        outPreco = tk.Label(midContainer, text=restaurante['preco'], bg=self.yellow, font=self.fonteT3)
        outPreco.grid(column=1, row=4, padx=margemx, pady=margemy)

        labelNota = tk.Label(midContainer, text="Nota: ", bg=self.yellow, font=self.fonteT3)
        labelNota.grid(column=0, row=5, padx=margemx, pady=margemy, sticky="w")

        outNota = tk.Label(midContainer, text=restaurante['nota'], bg=self.yellow, font=self.fonteT3)
        outNota.grid(column=1, row=5, padx=margemx, pady=margemy)

        bottomContainer = tk.Frame(self.frameTelaConsulta, bg=self.yellow)
        bottomContainer.pack()

        buttonVoltar = self.buttonRetornar(bottomContainer, self.frameTelaConsulta)
        buttonVoltar.pack(padx=margemx, pady=(20, 40))

    def telaPesquisaConsulta(self):
        #Tamanho de margem
        margemx= 20
        margemy= 20

        self.frameTelaPrincipal.pack_forget()

        self.framePesquisaConsulta = tk.Frame(self.root, bg=self.yellow)
        self.framePesquisaConsulta.pack(fill="both", expand=True)

        topContainer = tk.Frame(self.framePesquisaConsulta, bg=self.yellow)
        topContainer.pack()

        labelNome = tk.Label(topContainer, text="Digite o nome do restaurante: ", font=self.fonteT2, bg=self.yellow)
        labelNome.pack(padx=margemx, pady=(140, 20))

        self.entryNomeConsulta = tk.Entry(topContainer, font=self.fonteT3, bg="white", width=50)
        self.entryNomeConsulta.pack(padx=margemx, pady=margemy)

        bottomContainer = tk.Frame(self.framePesquisaConsulta, bg=self.yellow)
        bottomContainer.pack()

        buttonPesquisar = tk.Button(bottomContainer, text="Pesquisar", font=self.fonteT4, bg=self.orange, width=12, height=2,
                                    command=self.buscarRestauranteConsulta)    
        buttonPesquisar.grid(column=0, row=0, padx=margemx, pady=margemy, sticky="w")

        buttonVoltar = self.buttonRetornar(bottomContainer, self.framePesquisaConsulta)
        buttonVoltar.grid(column=1, row=0, padx=margemx, pady=margemy, sticky="e")  

    def buscarRestauranteConsulta(self):
        nome_restaurante =self.entryNomeConsulta.get()
        self.controller.buscarRestauranteConsulta(nome_restaurante)

    def telaLista(self): 
        registros = self.consultarTodos()
        self.frameTelaPrincipal.pack_forget()

        self.frameTelaLista = tk.Frame(self.root, bg=self.yellow)
        self.frameTelaLista.pack(fill="both", expand=True)    

        topContainer = tk.Frame(self.frameTelaLista, bg=self.yellow)
        topContainer.pack()

        labelTitulo = tk.Label(topContainer, text="Restaurantes visitados", bg=self.yellow, font=self.fonteT2)
        labelTitulo.pack(padx=10, pady=(30, 20))

        midContainer = tk.Frame(self.frameTelaLista, bg=self.yellow)
        midContainer.pack()

        lista = scrolledtext.ScrolledText(midContainer, width=40, height=15, wrap=tk.WORD, bg=self.yellow, font=self.fonteT3)
        lista.delete("1.0", tk.END)
        for registro in registros:
            linha = f"{registro[0]}. {registro[1]}\t\t{registro[2]}\t\t{registro[6]}\n"
            lista.insert(tk.END, linha)
        lista.pack()

        bottomContainer = tk.Frame(self.frameTelaLista, bg=self.yellow)
        bottomContainer.pack()

        buttonVoltar = self.buttonRetornar(bottomContainer, self.frameTelaLista)
        buttonVoltar.pack(padx=20, pady=(30, 40))

    def consultarTodos(self):
        registros = self.controller.consultarTodos()
        return registros

    def buttonRetornar(self, container, tela):
        button = tk.Button(container, width=12, height=2, font=self.fonteT4, text="Voltar", bg=self.darkyellow,
                                 command=lambda: self.retornarTelaPrincipal(tela))
        return button
        
    def retornarTelaPrincipal(self, tela):
        tela.pack_forget()

        self.frameTelaPrincipal.pack(fill="both", expand=True)

    def  alertSucesso(self, mensagem):
        self.root.withdraw()

        alerta = Toplevel()
        alerta.geometry("300x150")
        alerta.configure(bg=self.yellow)

        label = tk.Label(alerta, text=mensagem + " com sucesso!", pady=20, bg=self.yellow, font=self.fonteT3)
        label.pack()

        button = tk.Button(alerta, width=12, height=2, font=self.fonteT4, text="OK", bg=self.darkyellow,
                           command=lambda: self.fecharJanela(alerta))
        button.pack(pady=20)

    def  alertErro(self, mensagem):
        self.root.withdraw()

        alerta = Toplevel()
        alerta.geometry("300x150")
        alerta.configure(bg=self.yellow)

        label = tk.Label(alerta, text="Erro" + mensagem, pady=20, bg=self.yellow, font=self.fonteT3)
        label.pack()

        button = tk.Button(alerta, width=12, height=2, font=self.fonteT4, text="OK", bg=self.darkyellow,
                           command=lambda: self.fecharJanela(alerta))
        button.pack(pady=20)
    
    def fecharJanela(self, tela):
        if tela:
            tela.destroy()

        self.root.deiconify()

    def close(self, evento=None):
        sys.exit()





