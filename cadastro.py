import sqlite3
class Cadastro:
    def __init__(self,nome, endereco, cpf, telefone, email, senha, tipo_de_conta) -> None:
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.tipo_de_conta = tipo_de_conta
    
    def validarNoDB(self):
        ...


def cadastro(tipo_de_conta, nome, cpf, endereco, telefone, email, senha):
    # while True:
    #     senha = input("Senha: ")
    #     confirma_senha = input("Digite a senha novamente: ")
    #     if senha == confirma_senha:
    #         break
    usuario = Cadastro(nome, endereco, cpf, telefone, email, senha, tipo_de_conta)

def criarTabelas():
    conexao = sqlite3.connect("DataBase.db")
    cursor = conexao.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS cadastro('
    'id	INTEGER,'
	'nome	TEXT NOT NULL,'
	'endereco	TEXT NOT NULL,'
	'cpf	TEXT NOT NULL UNIQUE,'
	'telefone	TEXT NOT NULL,'
	'email	TEXT NOT NULL UNIQUE,'
	'tipo_de_conta	INTEGER NOT NULL,'
	'senha	TEXT NOT NULL,'
	'PRIMARY KEY(id AUTOINCREMENT)'
    ')')
    cursor.execute('CREATE TABLE IF NOT EXISTS Livros('
    'Nome	TEXT NOT NULL,'
	'Autor	TEXT NOT NULL,'
	'Gênero	TEXT,'
	'Quantidade	INTEGER NOT NULL,'
	'Código	INTEGER NOT NULL UNIQUE,'
	'Estante	TEXT,'
	'Link de Amostra	TEXT,'
	'PRIMARY KEY(Código AUTOINCREMENT)'

        ')')
    ...

def armazenar():

    ...
