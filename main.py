from datetime import timedelta, date
from metodos import *
from validacaoCPF import validarCpf
from validatorEmail import isEmailValido

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
        email = input("Email: ").lower()
        senha = input("Senha: ").lower()
        inicializar()
        
        try:
            global conta
            conta = Login(email, senha)
            
        
        except EmailSenhaIncorretoError  :
            print("Usuário e/ou senha inválido(s)!")
            conta = None
        
            # inicializar()
            # cursor.execute('SELECT tipo_de_conta, email FROM cadastro')
            # for line in cursor.fetchall():
            #     if line[1] == email:
            #         tipo = line[0]
        
        if conta != None:
            if type(conta) == UsuarioADM:
                menuAdmin(conta)
                break
            elif type(conta) == UsuarioNormal:
                menuUsuario(conta.id)
                break
        
def menuCadastroUsuario():
    while True:
        inicializar()
        nome = input("Nome: ").capitalize()
        telefone = int(input("Telefone: "))
        endereco = input("Endereço: ").capitalize()
        cpf = input("CPF: ")
        
        while not validarCpf(cpf):
            print("CPF inválido, digite novamente:")
            cpf = input("CPF: ")

        email = input("E-mail: ").lower()

        while not isEmailValido(email):
            print('\nEmail invalido, digite novamente\n')
            email = input("E-mail: ").lower()

        while True:
            senha = input("\nDigite sua senha: ")
            confirmaSenha = input("Digite sua senha novamente: ")           
            if senha == confirmaSenha:
                break
            else:
                print("As senhas precisam ser iguais! Digite novamente.")
        try:            
            contaCadastrada = UsuarioNormal(nome, endereco, cpf, telefone, email, senha)
            print('\nCadastro Concluido\n')
            menuInicial()
        except Exception as erro:
            print("Erro ao cadastrar usuário!", erro)
            fechar()

    # menuUsuario(contaCadastrada)
        
        
    
def menuAdmin(conta):
    while True:
        op = input('1 - Empréstimo de livro\n2 - Devolução de livro\n3 - Ver usuário\n4 - Usuários em atraso\n5 - Cadastrar livro\n6 - Remover livro\n7 - Remover usuario\n8 - Cadastro Admin\n9 - Sair\n ')
        match op:
            case '1':
                data_emprestimo = date.today()
                data_devolucao = data_emprestimo + timedelta(days = 7)
                id_usuario = int(input("ID do usuário: "))
                codigo_livro = int(input("Código do livro: "))
                usuario = getUsuario(id_usuario)
                if id_usuario not in usuariosComAtraso():
                    if len(LeEmprestimos(usuario, id_usuario)) < 3:
                        inicializar()
                        registrosEmprestimos(str(data_emprestimo), str(data_devolucao), id_usuario, codigo_livro)
                        fechar()
                    else:
                        print("O empréstimo não pode ser realizado pois o usuário já tem 3 emprestimos ativos.")
                else:
                    print("O empréstimo não pode ser realizado pois o usuário tem livro(s) em atraso.")
            case '2':
                codigo = int(input("Código do livro:"))
                inicializar()
                devolucaoLivros(codigo)
                fechar()
            case '3':
                id_usuario = int(input("ID do usuário: ")) 
                print(Conta.getConta(id_usuario))
            case '4':
                inicializar()
                print(usuariosComAtraso())
                fechar()
            case '5':
                nome = input("Nome do livro: ").capitalize()
                autor = input("Autor do livro: ").capitalize()
                genero = input("Gênero do livro: ").capitalize()
                estante = input("Estante do livro: ").upper()
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
                try: 
                    inicializar()
                    Conta.getConta(id_user).apagar() # SUGESTÃO: usar Conta.getConta(id_user).apagar() no lugar. Assim, as verificações (Se a conta é a única ADM, se o usuário tem livros em atraso) serão feitas e retornaram erros a serem tratados aqi usando o try
                except:
                    print('Erro ao apagar')    
                    fechar()
            case '8':
                nome = input("Nome: ").capitalize()
                telefone = input("Telefone: ")
                endereco = input("Endereço: ").capitalize()
                cpf = input("CPF: ")
                email = input("E-mail: ").lower()
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
def menuUsuario(id):
    while True:
        print('1 - Pesquisar Livro\n2 - Reservar livro\n3 - Renovar livro\n4 - Sugerir Livro\n5 - Sair')
        op = input('')
        match op:
            case '1':
                #tera alteraçoes
                inicializar()
                lista = getLivros()
                print('')
                for i in lista:
                    print(f'Livro: {i[0]} / Autor: {i[1]} / Gênero: {i[2]} / Código: {i[3]} / Estante: {i[4]} / Link de Amostra: {i[5]}')
                print('')
                fechar()
            case '2':
                inicializar()
                data_emprestimo = date.today()
                data_devolucao = data_emprestimo + timedelta(days = 7)
                c = 0
                while True:
                    if c == 5:
                        break
                    id_usuario = id
                        
                    while True:
                        codigo_livro = int(input("Código do livro: "))
                        try:
                            Livro(codigo_livro)
                        except Exception:
                            print('Codigo do livro não existe')
                        else:
                            break
                    if Livro(codigo_livro).disponibilidade == "disponível":
                        

                        registrosEmprestimos(str(data_emprestimo).replace("-", " "), str(data_devolucao).replace("-", " "), id_usuario, codigo_livro)
                        print('\nLivro Reservado\n')
                        fechar()
                        break
                    else:
                        print('\nLivro já reservado\n')
                        fechar()
                        break                    
            case '3':
                inicializar()
                while True:                    
                    data_devolucao = data_devolucao + timedelta(days=7)
                    codigo_livro = int(input("Código do livro: "))
                    c = 0
                    while True:
                        if c == 2:
                            print('\nCodigo incorreto\n')
                            break
                        if c == 1:
                            break
                        cursor.execute("SELECT Codigo FROM Livros")
                        for i in cursor.fetchall():
                            if codigo_livro == i[0]:
                                c = 1
                                break
                            else:
                                c = 2
                    if c == 1:
                        renovaçãoEmprestimo(data_devolucao,codigo_livro)
                        print('\nRenovado com sucesso\n')
                        break
                    else:
                        print('\nNão foi possivel renovar\n')
                fechar()
            case '4':
                inicializar()
                while True:
                    livro = str(input('Livro: '))
                    if livro == "":
                        print('\nLivro deve ter pelomenos 1 caractere\n')
                    else:
                        id_usuario = id
                        sugestoes_livros(livro,id_usuario)
                        break
                fechar()
            case '5':
                break
            case _:
                print('\nOpção incorreta\n')

menuInicial()
