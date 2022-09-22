import sqlite3
global conexao, cursor

def inicializar():
    """ Inicializa o cursor do sql. Use isto antes de qualquer método deste arquivo"""
    global conexao, cursor

    conexao = sqlite3.connect("DataBase.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

def fechar():    
    """ Fecha o cursor do sql. Use isto depois de usar qualquer método deste arquivo """

    cursor.close()
    conexao.close()


def criarTabelaLivros():

    cursor.execute('CREATE TABLE IF NOT EXISTS Livros('
    'Nome	TEXT NOT NULL,'
	'Autor	TEXT NOT NULL,'
	'Gênero	TEXT,'
	'Código	INTEGER NOT NULL UNIQUE,'
	'Estante	TEXT,'
	'Link_de_Amostra	TEXT,'
	'PRIMARY KEY(Código AUTOINCREMENT)'
    ')')

def cadastro_livros(l_nome,l_autor,l_genero,l_quantidade,l_estante,l_link_amostra):

    cursor.execute('INSERT INTO Livros(Nome,Autor,Gênero,Quantidade,Estante,"Link de Amostra") VALUES (?,?,?,?,?,?)',(l_nome,l_autor,l_genero,l_quantidade,l_estante,l_link_amostra))
    

def remover_livro(codigo):

    cursor.execute('DELETE FROM Livros WHERE Código = ? ', codigo)


def getLivros(**filtros):
    """ Retorna os valores encontrados na tabela livros que são iguais aos valores entrados. A key de entrada deve ser igual ao nome da coluna procurada e o valor o valor a ser encontrado. 
    \nEx: \n 
    getLivros(Nome="Crime e Castigo", Autor="Dostoievsky")

    Isso retornará todos os nomes e os autores dos livros que correspondem ao que foi pedido. Algo como:\n
    (("Crime e Castigo","Dostoievsky"),("Crime e Castigo","Dostoievsky"),("Crime e Castigo","Dostoievsky"))\n

    Caso você queira que outras informações sejam retornadas, adicione-as com o valor None. Assim, elas serão retornadas entretanto serão ignoradas na filtragem. 
    Ex:\n
    getLivros(Nome="Crime e Castigo", Autor="Dostoievsky", Código=None)

    Isso retornará algo como:\n
    (("Crime e Castigo","Dostoievsky", 996),("Crime e Castigo","Dostoievsky", 0),("Crime e Castigo","Dostoievsky", 20))\n

    """
    filtersSTR = ""
    for filtro in filtros:
        filtersSTR += filtro + ", "
    filtersSTR = filtersSTR[0:-2]

    cursor.execute("SELECT " + filtersSTR + " FROM Livros")

    resultados = []
    for item in cursor.fetchall():
        i = 0
        Valuable = True
        for index in item:
            if tuple(filtros.values())[i] != None:
                if index != tuple(filtros.values())[i]:
                    Valuable = False
                    break
            i += 1
        if Valuable:
            resultados.append(item)
    
    return resultados