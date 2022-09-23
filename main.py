from metodos import *
def menuInicial():
    while True:
        op = input("1 - Login\n2 - Cadastro\n3 - Fechar\n")
        match op:
            case "1":
                menuLogin()
            case "2":
                menuCadastroUsuario()
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
            inicializar()
            cursor.execute('SELECT tipo_de_conta, email FROM cadastro')
            for line in cursor.fetchall():
                if line[1] == email:
                    tipo = line[0]
            
            if tipo == 0:
                menuAdmin()
                break
            else:
                menuUsuario()
                break
        else:
            print("Usuário e/ou senha inválido(s)!")
            break
def menuCadastroUsuario():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    while True:
        tipo = input("Tipo de conta (0 = Administrador|1 = Usuário): ")
        if tipo != "0" and tipo != "1":
            break
        else:
            print("Opção inválida! Digite 0 para Administrador ou 1 para Usuário.")
    email = input("E-mail: ")
    while True:
        senha = input("Digite uma senha: ")
        confirmaSenha = input("Digite a senha novamente")
        if senha == confirmaSenha:
            break
        else:
            print("As senhas precisam ser iguais! Digite novamente.")

    try:
        cadastroUsuario(nome, endereco, cpf, telefone, email, senha, tipo)
    except:
        print("Erro ao cadastrar usuário!")
def menuAdmin():
    ...
def menuUsuario():
    ...

