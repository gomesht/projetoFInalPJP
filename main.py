from datetime import timedelta, date
from metodos import *
from validacaoCPF import validarCpf
from validatorEmail import isEmailValido

def menuInicial():
    inicializar()
    criarTabelaDadosInativos()
    criarTabelaContas()
    criarTabelaLivros()
    criarTabelaEmprestimos()
    criarTabelaSugestoes()
    fechar()

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
        senha = input("Senha: ")
        global cache_senha
        cache_senha = senha
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
        nome = input("Nome: ").title()
        telefone = int(input("Telefone: "))
        endereco = input("Endereço: ").title()
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
                if requisitosSenha(senha):
                    break
                else:
                    print("\nSenha fraca")
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
                if id_usuario not in usuariosComAtraso():
                    if len(LeEmprestimos(True, id_usuario)) < 3:
                        inicializar()
                        registrosEmprestimos(str(data_emprestimo).replace("-", " "), str(data_devolucao).replace("-", " "), id_usuario, codigo_livro)
                        print('\nLivro Alugado com sucesso')
                        fechar()
                    else:
                        print("\nO empréstimo não pode ser realizado pois o usuário já tem 3 emprestimos ativos.\n")
                else:
                    print("\nO empréstimo não pode ser realizado pois o usuário tem livro(s) em atraso.")
            case '2':
                codigo = int(input("Código do livro:"))
                inicializar()
                devolucaoLivros(codigo)
                fechar()
            case '3':
                #Arrumar e melhorar
                id_usuario = int(input("ID do usuário: ")) 
                print(Conta.getConta(id_usuario))
            case '4':
                #melhorar
                inicializar()
                print(usuariosComAtraso())
                fechar()
            case '5':
                #Melhorar/padronizar estantes
                print('')
                nome = input("Nome do livro: ").title()
                autor = input("Autor do livro: ").title()
                genero = input("Gênero do livro: ").title()
                estante = input("Estante do livro: ").upper()
                link = input("Link de amostra do livro: ")
                inicializar()
                cadastro_livros(nome, autor, genero, estante, link)
                print('\nLivro cadastrado com sucesso')
                fechar()
            case '6':
                #melhorar
                codigo = int(input("Excluir livro com o código: "))
                inicializar()
                remover_livro(codigo)
                fechar()
            case '7':
                #melhorar
                id_user = int(input("Apagar usuário com ID: "))
                try: 
                    inicializar()
                    Conta.getConta(id_user).apagar() # SUGESTÃO: usar Conta.getConta(id_user).apagar() no lugar. Assim, as verificações (Se a conta é a única ADM, se o usuário tem livros em atraso) serão feitas e retornaram erros a serem tratados aqi usando o try
                except:
                    print('Erro ao apagar')    
                    fechar()
            case '8':
                while True:
                    senha = input('digite sua senha: ')
                    if senha == cache_senha:
                        break
                    else:
                        print("Senha incorreta")
                
                nome = input("Nome: ").title()
                telefone = input("Telefone: ")
                endereco = input("Endereço: ").title()
                cpf = input('CPF: ')

                while not validarCpf(cpf):
                    print("CPF inválido, digite novamente:")
                    cpf = input("CPF: ")
                        
                email = input('Email: ').lower()

                while not isEmailValido(email):
                    print('\nEmail invalido, digite novamente\n')
                    email = input("E-mail: ").lower()

                while True:
                    senha = input("Digite uma senha: ")
                    confirmaSenha = input("Digite a senha novamente: ")
                    if senha == confirmaSenha:
                        break
                    else:
                        print("As senhas precisam ser iguais! Digite novamente.")
                try:
                    inicializar()

                    UsuarioADM(nome, endereco, cpf, telefone, email, senha)

                    fechar()
                except Exception as a:
                    print("Erro ao cadastrar usuário!", a)

                
            case '9':
                break
            case _:
                print("Opção inválida!")
def menuUsuario(id):
    while True:
        print('1 - Pesquisar Livro\n2 - Reservar livro\n3 - Renovar livro\n4 - Sugerir Livro\n5 - Alterar senha\n6 - Sair')
        op = input('')
        match op:
            case '1':
                #tera alteraçoes
                #arrumar erro disponibilidade
                inicializar()
                lista = getLivros()
                print('')
                for i in lista:
                    print(f'Livro: {i[0]} / Autor: {i[1]} / Gênero: {i[2]} / Código: {i[3]} / Estante: {i[4]} / Link de Amostra: {i[5]} / Status: {i[6]}')
                print('')
                fechar()
            case '2':
                #não deixar revervar mais de 3 livros
                inicializar()
                data_emprestimo = date.today()
                data_devolucao = data_emprestimo + timedelta(days = 7)
                c = 0
                while True:
                    if c == 5:
                        break
                    id_usuario = id
                        
                    while True:
                        codigo_livro = input("\nCódigo do livro: ")
                        try:
                            Livro(int(codigo_livro))
                        except Exception:
                            print('\nCodigo do livro não existe')
                        else:
                            break
                    if Livro(int(codigo_livro)).disponibilidade == "disponível":
                        

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
                    data_emprestimo = date.today()                    
                    data_devolucao = data_emprestimo + timedelta(days = 7)                 
                    while True:
                        codigo_livro = input("Código do livro: ")

                        try:  
                            Livro(int(codigo_livro))                   
                        except Exception:
                            print('Codigo do livro não existe')
                        else:
                            break                  
                    renovaçãoEmprestimo(str(data_devolucao).replace("-", " "),codigo_livro)
                    print('\nRenovado com sucesso\n')
                    fechar()
                    break
            case '4':
                inicializar()
                while True:
                    livro = str(input('Livro: '))
                    if livro == "":
                        print('\nLivro deve ter pelomenos 1 caractere\n')
                    else:
                        id_usuario = id
                        sugestoes_livros(livro,id_usuario)
                        print('Sua sugestão foi guardado, obrigado xD')
                        break
                fechar()
            case '5':
                b = 0
                while True:
                    global cache_senha
                    if b == 1:
                        break
                    senha_atual = input('\nDigite sua senha atual: \n')
                    if senha_atual == cache_senha:
                        while True:
                            senha = input("Digite sua nova senha: ")
                            senha1 = input("Repita sua nova senha: \n")
                            if senha == senha1:
                                if requisitosSenha(senha):
                                    inicializar()
                                    setInUsuarios(id, 'senha', senha)
                                    fechar()
                                    b = 1
                                    break
                                else:
                                    print("\nSenha fraca\n")
                            else:
                                print("\nAs senhas precisam ser iguais")
                    else:
                        print('\nSenha incorreta')
            case '6':
                break
            case _:
                print('\nOpção incorreta\n')

if __name__ == "__main__":
    menuInicial()


