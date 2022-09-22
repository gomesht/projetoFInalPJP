import sqlite3
global cursor

def cadastroUsuario(nome, endereco, cpf, telefone, email, senha, tipo_de_conta):
    
    cursor.execute("INSERT INTO cadastro (nome, endereco, cpf, telefone, email, senha, tipo_de_conta) VALUES (?,?,?,?,?,?,?)",(nome, endereco, cpf, telefone, email, senha, tipo_de_conta))
    cursor.commit()
        
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
    'data_emprestimo TEXT NOT NULL,'
    'data_devolucao TEXT NOT NULL,'
    'id_usuario INTEGER NOT NULL,'
    'codigo_livro INTEGER NOT NULL'
    'status INTEGER NOT NUL'
    'FOREIGN KEY (id_usuario) REFERENCES cadastro (id) ON DELETE CASCADE ON UPDATE CASCADE'
    'FOREIGN KEY (codigo_livro) REFERENCES Livros (codigo) ON DELETE CASCADE ON UPDATE CASCADE'
    ')')


def criarTabelaSugestoes():
    cursor.execute('CREATE TABLE IF NOT EXISTS sugestoes ('
    'livro TEXT NOT NULL,'
    'id_usuario INTEGER NOT NULL,'
    'FOREIGN KEY (id_usuario) REFERENCES cadastro (id) ON DELETE CASCADE ON UPDATE CASCADE'
    ')')

def Login(email, senha):
    """Entrada email e senha de um usuário, saída True se email e senha estiverem corretos e Falso caso contrário."""

    validador = 0
    while True:
        # if validador == 1:
        #     break
        # if validador == 2:
        #     raise ValueError("Email ou senha Incorretos")
        # while True: 
        #     if email != "":
        #         break
        # while True:
        #     if senha != "":
        #         break
        cursor.execute('SELECT email,senha FROM cadastro')
        for item in cursor.fetchall():
            if email == item[0] and senha == item[1]:
                return True              
        return False

def remover_usuario(id):

    cursor.execute('DELETE FROM cadastro WHERE id = ? ', id)
    cursor.commit()

def EmprestimosUsuario(id):
    """Entrada ID do usuário, saída relatório dos emprestimos de livros com código do livro, data de emprestimo e data de devolução"""

    cursor.execute('SELECT codigo_livro, data_emprestimo, data_devolucao FROM emprestimos WHERE id_usuario = ?', id)
    return cursor.fetchall()
        





 # print(f"Código do livro: {item[0]} Data de empréstimo: {item[1]} Data de devolução: {item[2]}")




