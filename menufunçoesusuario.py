from metodos import *
from datetime import timedelta,datetime

def painelUsuario(email,id):
    while True:
        op = input('1 - Pesquisar Livro\n2 - Reservar livro\n3 - Renovar livro\n4 - Sugerir Livro\n5 - Sair')
        match op:
            case '1':
                #tera alteraçoes
                inicializar()
                lista = getLivros()
                for i in lista:
                    print(f'Livro: {i[0]} / Autor: {i[1]} / Gênero: {i[2]} / Código: {i[3]} / Estante: {i[4]} / Link de Amostra: {i[5]}')
                fechar()
            case '2':
                #em vez de pedir o id do usuario, pegar altomaticamente.
                inicializar()
                data_emprestimo = datetime.today()
                data_devolucao = data_emprestimo + timedelta(days=7)
                c = 0
                while True:
                    if c == 5:
                        break
                    id_usuario = id
                    while True:
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
                        if c == 1 and disponibilidadeLivro(codigo_livro) == "disponivel":
                            registrosEmprestimos(data_emprestimo,data_devolucao,id_usuario,codigo_livro,'resevado')
                            print('\nLivro Reservado\n')
                            c = 5
                            break
                        else:
                            print('\nLivro já reservado\n')
                            c = 5
                            break                    
                fechar()
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
                        print('znLivro deve ter pelomenos 1 caractere\n')
                    else:
                        id_usuario = id
                        sugestoes_livros(livro,id_usuario)
                        break
                fechar()
            case '5':
                break
            case _:
                print('\nOpção incorreta\n')
