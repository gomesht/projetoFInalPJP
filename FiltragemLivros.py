import sqlite3

def inicializar():
    """ Inicializa o cursor do sql. Use isto antes de qualquer método deste arquivo"""
    global conexao, cursor

    conexao = sqlite3.connect("DataBase.db")
    cursor = conexao.cursor()

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
def fechar():    
    """ Fecha o cursor do sql. Use isto depois de usar qualquer método deste arquivo """

    cursor.close()
    conexao.close()


inicializar()

print(getLivros(Nome="teste", Autor="teste", Código = None))

fechar()