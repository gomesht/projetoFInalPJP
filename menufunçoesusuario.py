from metodos import *
from datetime import timedelta,datetime

def painelUsuario(email,id):
    while True:
        op = input('1 - Pesquisar Livro\n2 - Reservar livro\n3 - Renovar livro\n4 - Sugerir Livro\n5 - Sair')
        match op:
            case '1':
                #op = input('')
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
                    if c == 2:
                        break
                    id_usuario = id
                    codigo_livro = int(input("Código do livro: "))
                    cursor.execute('SELECT Codigo FROM Livros')
                    for i in cursor.fetchall():
                        if codigo_livro == i:
                            registrosEmprestimos(data_emprestimo,data_devolucao,id_usuario,codigo_livro,'resevado')
                            print('Livro Reservado')
                            c = 2
                            break
                        else:
                            c = 1                       
                fechar()
            case '3':
                inicializar()
                codigo_livro = int(input('Código do livro: '))
                data_devolucao = data_devolucao + timedelta(days=7)
                renovaçãoEmprestimo(data_devolucao,codigo_livro)
                print('Renovado com sucesso')
                fechar()
            case '4':
                inicializar()
                livro = str(input('Livro: '))
                id_usuario = id
                sugestoes_livros(livro,id_usuario)
                fechar()
            case '5':
                break
            case _:
                print('\nOpção incorreta\n')
painelUsuario()

# inicializar()
# lista_de_livros = list(getLivros())

# print(lista_de_livros[1][2])
# fechar()

# Gêneros de ficção
# Fantasia
# Ficção científica
# Distopia
# Ação e aventura
# Ficção Policial
# Horror
# Thriller e Suspense
# Ficção histórica
# Romance
# Ficção Feminina
# LGBTQ+
# Ficção Contemporânea
# Realismo mágico
# Graphic Novel
# Conto
# Young adult – Jovem adulto
# New adult – Novo Adulto 
# Infantil



# Gêneros de não ficção
# Memórias e autobiografia
# Biografia
# Gastronomia
# Arte e Fotografia
# Autoajuda
# História
# Viajem
# Crimes Reais
# Humor
# Ensaios
# Guias & Como fazer 
# Religião e Espiritualidade
# Humanidades e Ciências Sociais
# Paternidade e família
# Tecnologia e Ciência
# Infantil
