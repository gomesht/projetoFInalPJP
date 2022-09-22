from metodos import *
def menuInicial():
    while True:
        op = input("1 - Login\n2 - Cadastro\n3 - Fechar\n")
        match op:
            case "1":
                menuLogin()
            case "2":
                menuCadastro()
            case "3":
                break
            case _:
                print("Opção inválida!")
def menuLogin():
    while True:
        email = ("Email: ")
        senha = ("Senha: ")
        Login(email, senha)
        if Login(email, senha):
            if "admin":
                menuAdmin()
                break
            else:
                menuUser()
                break
        else:
            print("Usuário e/ou senha inválido(s)!")
            break
def menuCadastro():
    ...
def menuAdmin():
    ...
def menuUser():
    ...

