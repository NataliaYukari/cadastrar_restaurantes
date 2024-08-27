from Categoria import Categoria
import mysql.connector
from mysql.connector import Error

class Model:
  def __init__(self, user, password, host, database):
      try:
        self.conexao = mysql.connector.connect (
          user = user,
          password = password,
          host = host,
          database = database
        ) 
        if self.conexao.is_connected():
          print("Conectado ao banco de dados")

      except Error as erro:
         print(f"Não conectado ao banco de dados: {erro}")

      # Criação das categorias
      self.categoria1 = Categoria(1, "Familiar/casual")
      self.categoria2 = Categoria(2, "Fast food")
      self.categoria3 = Categoria(3, "Café")
      self.categoria4 = Categoria(4, "Luxo")
      self.categoria5 = Categoria(5, "Clássico")

  def cadastrarRestaurante(self, nome, localizacao, nota, categoria, culinaria, preco): 
    cursor = self.conexao.cursor()

    try:
      if categoria == "Familiar/casual":
        id_categoria = self.categoria1.id

      elif categoria == "Fast Food":
        id_categoria = self.categoria2.id

      elif categoria == "Café":
        id_categoria = self.categoria3.id

      elif categoria == "Luxo":
        id_categoria = self.categoria4.id

      elif categoria == "Clássico":
        id_categoria = self.categoria5.id

      sql = "INSERT INTO Restaurantes (nome, localizacao, nota, id_categoria, culinaria, preco) VALUES (%s, %s, %s, %s, %s, %s)"
      valores = (nome, localizacao, nota, id_categoria, culinaria, preco)
    
      cursor.execute(sql, valores)
      self.conexao.commit()
      print("Dados inseridos com sucesso")

    except mysql.connector.Error as erro:
      print(f" ao inserir dados: {erro}")  
      cursor.close()
      raise
       
    finally:
      cursor.close()

  def buscarRestaurante(self, nome_restaurante):
    cursor = self.conexao.cursor(dictionary=True)

    try: 
      sql = "SELECT id_restaurante, nome, localizacao, nota, id_categoria, culinaria, preco FROM Restaurantes WHERE nome = %s"
      valores = (nome_restaurante,)
      cursor.execute(sql, valores)
      restaurante = cursor.fetchone()
      cursor.close()

      return restaurante

    except mysql.connector.Error as erro:
      print(f"Erro ao buscar restaurante: {erro}")
      return None
    
    except Exception as erro2:
      print(f"Erro inesperado: {erro2}")
      return None

  def alterarRestaurante(self, id_restaurante, nome, localizacao, nota, categoria, culinaria, preco): 
    cursor = self.conexao.cursor()

    try:
      if categoria == "Familiar/casual":
        id_categoria = self.categoria1.id

      elif categoria == "Fast Food":
        id_categoria = self.categoria2.id

      elif categoria == "Café":
        id_categoria = self.categoria3.id

      elif categoria == "Luxo":
        id_categoria = self.categoria4.id

      elif categoria == "Clássico":
        id_categoria = self.categoria5.id

      sql2 = "UPDATE Restaurantes SET nome = %s, localizacao = %s, nota = %s, id_categoria = %s, culinaria = %s, preco = %s WHERE id_restaurante = %s"
      valores = (nome, localizacao, nota, id_categoria, culinaria, preco, id_restaurante)
    
      cursor.execute(sql2, valores)
      self.conexao.commit()
      print("Dados alterados com sucesso")

    except mysql.connector.Error as erro:
      print(f"Erro ao alterar dados: {erro}")  
      self.conexao.rollback()
       
    finally:
      cursor.close()
    
  def excluirRestaurante(self, nome):
    try:
      cursor = self.conexao.cursor()

      cursor.execute("SELECT id_restaurante FROM Restaurantes WHERE nome = %s", (nome,))
      id_restaurante = cursor.fetchone()

      cursor.execute("DELETE FROM Restaurantes WHERE id_restaurante = %s", (id_restaurante[0],))
      self.conexao.commit()
      print("Excluído com sucesso")

    except mysql.connector.Error as erro:
      print(f"Erro ao excluir dados: {erro}")
      self.conexao.rollback()

    finally:
      cursor.close()

  def consultarTodos(self):
    cursor = self.conexao.cursor()

    try:
      cursor.execute("SELECT * FROM Restaurantes")
      resultado = cursor.fetchall()
      cursor.close()
      
      if resultado:
        return resultado
      else:
        return None
      
    except mysql.connector.Error as erro:
      print(f"Erro ao buscar restaurantes: {erro}")
      return None
    
    finally:
      cursor.close()


