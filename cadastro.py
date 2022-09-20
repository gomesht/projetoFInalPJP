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
    conexao = 
def armazenarNoDB():
    ...
