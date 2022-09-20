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


def cadastro():
    tipo_de_conta = int(input("Tipo de conta(0 admin/ 1 usuário "))
    nome = input("Nome: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    while True:
        senha = input("Senha: ")
        confirma_senha = input("Digite a senha novamente: ")
        if senha == confirma_senha:
            break
    
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

        ')')
    ...

def armazenar():

    ...

def cadastro_livros(l_nome,l_autor,l_genero,l_quantidade,l_estante,l_link_amostra):


    conexao = sqlite3.connect("DataBase.db")
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO Livros(Nome,Autor,Gênero,Quantidade,Estante,"Link de Amostra") VALUES (?,?,?,?,?,?)',(l_nome,l_autor,l_genero,l_quantidade,l_estante,l_link_amostra))
    cursor.close()
    conexao.close()

def remover_livro(codigo):
    conexao = sqlite3.connect("DataBase.db")
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM Livros WHERE Código = ? ', codigo)
    cursor.close()
    conexao.close()

cadastro_livros('O Bartolomeu','Jiroba Schuteke','Romance',2,'A','Algo')

