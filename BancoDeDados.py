import mysql.connector
from mysql.connector import Error

class BancoDeDados:
    def __init__(self, user, password, host, bd):
        self.user = user
        self.password = password
        self.host = host
        self.bd = bd
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect
            user = self.user
            password = self.password
            host = self.host
            bd = self.bd 
            
            
            if self.connection.is_connected():
                print("Conectado ao banco de dados com sucesso")

        except Error as e:
            print("Erro ao conectar ao banco de dados: " + e)

    def encerrar_conexao(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados encerrada")