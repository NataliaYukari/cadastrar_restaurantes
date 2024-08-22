import RestauranteModel as Model

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def escolherOpcao(self, opcao):
        if opcao == "novo":
            return self.view.telaCadastro()
        elif opcao == "alterar":
            return self.view.telaPesquisaAlterar()
        elif opcao == "ver":
            return self.view.telaPesquisaConsulta()
        elif opcao == "lista":
            return self.view.telaLista()

    def cadastrarRestaurante(self, nome, localizacao, nota, categoria, culinaria, preco):
        try:
            self.model.cadastrarRestaurante(nome, localizacao, nota, categoria, culinaria, preco)
            self.view.alertSucesso("Cadastrado")

        except Exception as erro:
            self.view.alertErro(f" ao cadastrar: {erro}")

    def buscarRestaurante(self, nome_restaurante):
        try:
            restaurante = self.model.buscarRestaurante(nome_restaurante)

            if restaurante:
                self.id_restaurante = restaurante['id_restaurante']
                self.view.telaAlterar(restaurante)

            else:
                self.view.alertErro(": restaurante não encontrado")

        except Exception as erro:
            self.view.alertErro(f" ao buscar restaurante: {erro}")

    def alterarRestaurante(self, nome, localizacao, nota, categoria, culinaria, preco):
        try:
            self.model.alterarRestaurante(self.id_restaurante, nome, localizacao, nota, categoria, culinaria, preco)
            self.view.alertSucesso("Alterado")

        except Exception as erro:
            self.view.alertErro(f" ao alterar: {erro}")

    def excluirRestaurante(self, nome):
        try:
            self.model.excluirRestaurante(nome)
            self.view.alertSucesso("Excluído")

        except Exception as erro:
            self.view.alertErro(f" ao excluir: {erro}")      

    def buscarRestauranteConsulta(self, nome_restaurante):
        try:
            restaurante = self.model.buscarRestaurante(nome_restaurante)

            if restaurante:
                self.view.telaConsulta(restaurante)

            else:
                self.view.alertErro(": restaurante não encontrado")

        except Exception as erro:
            self.view.alertErro(f" ao buscar restaurante: {erro}")

    def consultarTodos(self):
        registros = self.model.consultarTodos()
        return registros