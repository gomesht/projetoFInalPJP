import sqlite3
from FiltragemLivros import inicializar, fechar
global conexao, cursor

class Cadastro:
    def __init__(self,nome, endereco, cpf, telefone, email, senha, tipo_de_conta) -> None:
        inicializar()
        cursor.execute("INSERT INTO cadastro (nome, endereco, cpf, telefone, email, senha, tipo_de_conta) VALUES (?,?,?,?,?,?,?)",(nome, endereco, cpf, telefone, email, senha, tipo_de_conta))
        fechar()

def criarTabelasContas():
    inicializar()
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
    fechar()

def Login(email, senha):
    inicializar()
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
                fechar()
                return True
                
            else:
                fechar()
                return False

def remover_usuario(id):

    inicializar
    cursor.execute('DELETE FROM cadastro WHERE id = ? ', id)
    fechar()
