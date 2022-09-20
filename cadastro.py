import sqlite3
class Cadastro:
    def __init__(self,nome, endereco, cpf, telefone, email, senha, tipo_de_conta) -> None:
        conexao = sqlite3.connect("DataBase.db")
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO cadastro (nome, endereco, cpf, telefone, email, senha, tipo_de_conta) VALUES (?,?,?,?,?,?,?)",(nome, endereco, cpf, telefone, email, senha, tipo_de_conta))
        cursor.close()
        conexao.close()
        
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
	'Código	INTEGER NOT NULL UNIQUE,'
	'Estante	TEXT,'
	'Link de Amostra	TEXT,'
	'PRIMARY KEY(Código AUTOINCREMENT)'

        ')')
    cursor.close()
    conexao.close()

def Login(email, senha):
    conexao = sqlite3.connect("DataBase.db")
    cursor = conexao.cursor()
    validador = 0

    while True:
        if validador == 1:
            break
        if validador == 2:
            raise ValueError("Email ou senha Incorretos")
        while True: 
            if email != "":
                break
        while True:
            if senha != "":
                break
        cursor.execute('SELECT email,senha FROM cadastro')
        for item in cursor.fetchall():
            if email == item[0] and senha == item[1]:
                cursor.close()
                conexao.close()
                return True
                
            else:
                cursor.close()
                conexao.close()
                return False

def armazenar():

    ...
