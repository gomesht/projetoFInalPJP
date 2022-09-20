import sqlite3

def inicializar():
    """ Inicializa o cursor do sql. Use isto antes de qualquer método deste arquivo"""
    global conexão, cursor

    conexão = sqlite3.connect("DataBase.db")
    cursor = conexão.cursor()

def getLivros(**filtros):
    
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
    """ Fecha o cursor do sql. Use isto depois de usar qualquer método deste arquivo"""

    cursor.close()
    conexão.close()


inicializar()
print(getLivros(Nome="teste", Autor="teste", Código = None))
fechar()