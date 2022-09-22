import sqlite3, datetime
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

def criarTabelaContas():

    cursor.execute('CREATE TABLE IF NOT EXISTS cadastro('
    'id	INTEGER,'
	'nome	TEXT NOT NULL,'
	'endereco	TEXT NOT NULL,'
	'cpf	TEXT NOT NULL UNIQUE,'
	'telefone	TEXT NOT NULL,'
	'email	TEXT NOT NULL UNIQUE,'
	'tipo_de_conta	INTEGER NOT NULL,'
	'senha	TEXT NOT NULL,'
	'PRIMARY KEY(id AUTOINCREMENT)'
    ')')  

def criarTabelaEmprestimos():

    cursor.execute('CREATE TABLE IF NOT EXISTS emprestimos ('
    'data_emprestimo BLOB NOT NULL,'
    'data_devolucao BLOB NOT NULL,'
    'id_usuario INTEGER NOT NULL,'
    'codigo_livro INTEGER NOT NULL'
    'status TEXT NOT NULL'
    'FOREIGN KEY (id_usuario) REFERENCES cadastro (id) ON DELETE CASCADE ON UPDATE CASCADE'
    'FOREIGN KEY (codigo_livro) REFERENCES Livros (codigo)'
    ')')


def criarTabelaSugestoes():
    cursor.execute('CREATE TABLE IF NOT EXISTS sugestoes ('
    'livro TEXT NOT NULL,'
    'id_usuario INTEGER NOT NULL,'
    'FOREIGN KEY (id_usuario) REFERENCES cadastro (id) ON DELETE CASCADE ON UPDATE CASCADE'
    ')')

########################################################################################
# Métodos de livros
########################################################################################

def cadastro_livros(l_nome,l_autor,l_genero,l_quantidade,l_estante,l_link_amostra):

    cursor.execute('INSERT INTO Livros(Nome,Autor,Gênero,Quantidade,Estante,"Link de Amostra") VALUES (?,?,?,?,?,?)',(l_nome,l_autor,l_genero,l_quantidade,l_estante,l_link_amostra))
    conexao.commit()

def remover_livro(codigo):

    cursor.execute('DELETE FROM Livros WHERE Código = ? ', (codigo,))
    conexao.commit()

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

def sugestoes_livros(livro,id_usuario):
    cursor.execute('INSERT INTO sugestoes(livro,id_usuario) VALUES (?,?)',(livro,id_usuario))
    conexao.commit()

########################################################################################
# Métodos de usuário
########################################################################################

def cadastroUsuario(nome, endereco, cpf, telefone, email, senha, tipo_de_conta):
    """tipo de conta 0 para admin e 1 para usuários"""
    
    cursor.execute("INSERT INTO cadastro (nome, endereco, cpf, telefone, email, senha, tipo_de_conta) VALUES (?,?,?,?,?,?,?)",(nome, endereco, cpf, telefone, email, senha, tipo_de_conta))
    conexao.commit()

def Login(email, senha):
    """Entrada email e senha de um usuário, saída True se email e senha estiverem corretos e Falso caso contrário."""

    cursor.execute('SELECT email,senha FROM cadastro')
    for item in cursor.fetchall():
        if email == item[0] and senha == item[1]:
            return True              
    return False

def remover_usuario(id):

    cursor.execute('DELETE FROM cadastro WHERE id = ? ', (id,))
    cursor.commit()


def EmprestimosUsuario(id):
    """Entrada ID do usuário, saída relatório dos emprestimos de livros com código do livro, data de emprestimo e data de devolução"""

    cursor.execute('SELECT codigo_livro, data_emprestimo, data_devolucao FROM emprestimos WHERE id_usuario = ?', (id,))
    return cursor.fetchall()

def atualizaStatus():
    """Altera o status dos usuários em atraso para 0"""
    data_atual = datetime()
    cursor.execute('UPDATE emprestimos SET status = ? WHERE data_atual > data_entrega', 'atrasado')
    conexao.commit()

def usuariosComAtraso():
    """Retorna uma lista com os id dos usuários em atraso"""
    cursor.execute('SELECT id_usuario FROM emprestimos WHERE status = ?', 'atrasado')
    return cursor.fetchall()

def baixaEmprestimo(codigo):

    cursor.execute('UPDATE emprestimos SET status = ? WHERE codigo_livro = ?', ('entregue', codigo))
    conexao.commit()
