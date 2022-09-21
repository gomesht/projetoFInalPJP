import sqlite3
from FiltragemLivros import inicializar, fechar
global conexao, cursor

def criarTabelaLivros():
    
    inicializar()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS Livros('
    'Nome	TEXT NOT NULL,'
	'Autor	TEXT NOT NULL,'
	'Gênero	TEXT,'
	'Código	INTEGER NOT NULL UNIQUE,'
	'Estante	TEXT,'
	'Link_de_Amostra	TEXT,'
	'PRIMARY KEY(Código AUTOINCREMENT)'
    ')')
    
    fechar()

def cadastro_livros(l_nome,l_autor,l_genero,l_quantidade,l_estante,l_link_amostra):

    inicializar()

    cursor.execute('INSERT INTO Livros(Nome,Autor,Gênero,Quantidade,Estante,"Link de Amostra") VALUES (?,?,?,?,?,?)',(l_nome,l_autor,l_genero,l_quantidade,l_estante,l_link_amostra))
    
    fechar()

def remover_livro(codigo):

    inicializar()

    cursor.execute('DELETE FROM Livros WHERE Código = ? ', codigo)

    fechar()