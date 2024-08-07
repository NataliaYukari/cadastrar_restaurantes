import Categoria
import Culinaria

class Model:
    def __init__(self):
        self.categoria = Categoria(self)
        self.culinaria = Culinaria(self)

        self.id_restaurante = ''
        self.nome = ''
        self.localizacao = ''
        self.nota = ''
        self.preco = ''
        
