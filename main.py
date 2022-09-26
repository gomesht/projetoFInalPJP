from datetime import timedelta
from classes import *
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
        email = input("Email: ")
        senha = input("Senha: ")
        inicializar()
        try:
            conta = Login(email, senha)
        except EmailSenhaIncorreto:
            print("Usuário e/ou senha inválido(s)!")

            # inicializar()
            # cursor.execute('SELECT tipo_de_conta, email FROM cadastro')
            # for line in cursor.fetchall():
            #     if line[1] == email:
            #         tipo = line[0]
            
        if type(conta) == UsuarioADM:
            menuAdmin()
            break
        else:
            menuUsuario()
            break
    
def menuCadastroUsuario():
    
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    while True:
        senha = input("Digite uma senha: ")
        confirmaSenha = input("Digite a senha novamente")
        if senha == confirmaSenha:
            break
        else:
            print("As senhas precisam ser iguais! Digite novamente.")

    inicializar()
    try:    
        contaCadastrada = UsuarioNormal(nome, endereco, cpf, telefone, email, senha)
    except:
        print("Erro ao cadastrar usuário!")

    fechar()

    menuUsuario(contaCadastrada)
        
        
    
def menuAdmin(conta):
    while True:
        op = input('1 - Empréstimo de livro\n2 - Devolução de livro\n3 - Ver usuário\n4 - Usuários em atraso\n5 - Cadastrar livro\n6 - Remover livro\n7 - Remover usuario\n8 - Cadastro Admin\n9 - Sair\n ')
        match op:
            case '1':
                data_emprestimo = datetime.today()
                data_devolucao = data_emprestimo + timedelta(days = 7)
                id_usuario = int(input("ID do usuário: "))
                codigo_livro = int(input("Código do livro: "))
                inicializar()
                registrosEmprestimos(str(data_emprestimo), str(data_devolucao), id_usuario, codigo_livro, "emprestado")
                fechar()
            case '2':
                codigo = int(input("Código do livro:"))
                inicializar()
                devolucaoLivros(codigo)
                fechar()
            case '3':
                # esperar classe ficar pronta para implementar
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
                codigo = int(input("Excluir livro com o código: "))
                inicializar()
                remover_livro(codigo)
                fechar()
            case '7':
                id_user = int(input("Apagar usuário com ID: ")) 
                inicializar()
                remover_usuario(id_user)
                fechar()
            case '8':
                nome = input("Nome: ")
                telefone = input("Telefone: ")
                endereco = input("Endereço: ")
                cpf = input("CPF: ")
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

                    UsuarioADM(nome, endereco, cpf, telefone, email, senha)

                    fechar()
                except:
                    print("Erro ao cadastrar usuário!")

                
            case '9':
                break
            case _:
                print("Opção inválida!")
def menuUsuario():
    ...

