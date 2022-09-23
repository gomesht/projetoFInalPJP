from datetime import timedelta
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
        inicializar()
        cadastroUsuario(nome, endereco, cpf, telefone, email, senha, tipo)
        fechar()
    except:
        print("Erro ao cadastrar usuário!")
def menuAdmin():
    while True:
        op = input('1 - Empréstimo de livro\n2 - Devolução de livro\n3 - Ver usuário\n4 - Usuários em atraso\n5 - Cadastrar livro\n6 - Remover livro\n7 - Remover usuario\n8 - Sair\n ')
        match op:
            case '1':
                data_emprestimo = datetime.today()
                data_devolucao = data_emprestimo + timedelta(days = 7)
                id_usuario = int(input("ID do usuário: "))
                codigo_livro = int(input("Código do livro: "))
                inicializar()
                registrosEmprestimos(data_emprestimo, data_devolucao, id_usuario, codigo_livro, "emprestado")
                fechar()
            case '2':
                codigo = int(input("Código do livro:"))
                inicializar()
                devolucaoLivros(codigo)
                fechar()
            case '3':
                pass
            case '4':
                inicializar()
                print(usuariosComAtraso())
                fechar()
            case '5':
                nome = input("Nome do livro: ")
                autor = input("Autor do livro: ")
                genero = input("Gênero do livro: ")
                estante = input("Estante do livro: ")
                link = input("Link de amostra do livro: ")
                inicializar()
                cadastro_livros(nome, autor, genero, estante, link)
                fechar()

            case '6':
                inicializar()

                fechar()
            case '7':
                inicializar()
                
                fechar()
            case '8':
                break
            case _:
                print("Opção inválida!")
def menuUsuario():
    ...

