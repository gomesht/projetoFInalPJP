import sqlite3, datetime, time
from datetime import date, timedelta
from typing import Tuple, overload
from validacaoCPF import validarCpf  
from abc import *          

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
	'Genero	TEXT,'
	'Codigo	INTEGER NOT NULL UNIQUE,'
	'Estante	TEXT,'
	'Link_de_Amostra	TEXT,'
	'PRIMARY KEY(Codigo AUTOINCREMENT)'
    ')')

def criarTabelaContas():

    cursor.execute('CREATE TABLE IF NOT EXISTS cadastro('
    'id	INTEGER NOT NULL UNIQUE,'
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
    'codigo_livro INTEGER NOT NULL,'
    'FOREIGN KEY (id_usuario) REFERENCES cadastro (id),'
    'FOREIGN KEY (codigo_livro) REFERENCES Livros (Codigo) ON DELETE CASCADE ON UPDATE CASCADE'
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

def cadastro_livros(l_nome,l_autor,l_genero,l_estante,l_link_amostra):

    cursor.execute('INSERT INTO Livros(Nome,Autor,Genero,Estante,"Link de Amostra") VALUES (?,?,?,?,?)',(l_nome,l_autor,l_genero,l_estante,l_link_amostra))
    conexao.commit()

def remover_livro(codigo):

    cursor.execute('DELETE FROM Livros WHERE Codigo = ? ', (codigo,))
    conexao.commit()

def getLivros(**filtros):
    """ Retorna os valores encontrados na tabela livros que são iguais aos valores entrados. A key de entrada deve ser igual ao nome da coluna procurada e o valor o valor a ser encontrado. 
    \nEx: \n 
    getLivros(Nome="Crime e Castigo", Autor="Dostoievsky")

    Isso retornará todos os nomes e os autores dos livros que correspondem ao que foi pedido. Algo como:\n
    (("Crime e Castigo","Dostoievsky", "ficção", " 1 ", "e1", "http: blabla.com" ),
    ("Crime e Castigo", "Dostoievsky", "ficção", " 55", "e1", "http: blabla.com" ),
    ("Crime e Castigo", "Dostoievsky", "ficção", "297", "e1", "http: blabla.com" ))\n

    """

    Nome = None
    Autor = None
    Genero = None
    Codigo = None
    Estante = None
    LdeAmostra = None
    count = 0
    for filtro in filtros:
        match filtro:
            case "Nome":
                Nome = tuple(filtros.values())[count]
            case "Autor":
                Autor = tuple(filtros.values())[count]
            case "Genero":
                Genero = tuple(filtros.values())[count]
            case "Codigo":
                Codigo = tuple(filtros.values())[count]
            case "Estante":
                Estante = tuple(filtros.values())[count]
            case "Link_de_amostra":
                LdeAmostra = tuple(filtros.values())[count]
            case _:
                if filtro.count("á") > 0 or filtro.count("ó") > 0 or filtro.count("ê") > 0:
                    raise ValueError(f"Filtro {filtro} não existe no banco de dados. \n Lembre-se que os nomes das variáveis não possuem acentos...")
                if filtro.lower() == "nome" or filtro.lower() == "autor" or filtro.lower() == "genero" or filtro.lower() == "codigo" or filtro.lower() == "estante" or filtro.lower() == "Link_de_amostra":
                    raise ValueError(f"Filtro {filtro} não existe no banco de dados. \n As variáveis estão com com a primeira letra maiúscula e o resto minúsculo?")
                raise ValueError(f"Filtro {filtro} não existe no banco de dados")

        count += 1
    
    valDeFiltragem = [ Nome,Autor,Genero,Codigo,Estante,LdeAmostra ]

    cursor.execute("SELECT * FROM Livros")

    resultados = []
    for item in cursor.fetchall():
        i = 0
        Valuable = True
        for index in item:
            if valDeFiltragem[i] != None:
                if index != valDeFiltragem[i]:
                    Valuable = False
                    break
            i += 1
        if Valuable:
            item = list(item)
            item.append(disponibilidadeLivro(item[3]))
            resultados.append(item)

    return resultados

def sugestoes_livros(livro,id_usuario):
    cursor.execute('INSERT INTO sugestoes(livro,id_usuario) VALUES (?,?)',(livro,id_usuario))
    conexao.commit()

def disponibilidadeLivro(codigo):
    cursor.execute('SELECT * FROM emprestimos')
    for item in cursor.fetchall():
        if codigo == item[3]:
            if date(time.strptime(item[1])[0],time.strptime(item[1])[1],time.strptime(item[1])[2]) <= date.today():
                return "atrasado"
            elif date(time.strptime(item[0])[0],time.strptime(item[0])[1],time.strptime(item[0])[2]) >= date.today():
                return "reservado"
            else:
                return "emprestado"
    return "disponivel"

########################################################################################
# Métodos de usuário
########################################################################################

def cadastroUsuario(nome, endereco, cpf, telefone, email, senha, tipo_de_conta):
    """tipo de conta 0 para admin e 1 para usuários"""
    
    cursor.execute("INSERT INTO cadastro (nome, endereco, cpf, telefone, email, senha, tipo_de_conta) VALUES (?,?,?,?,?,?,?)",(nome, endereco, cpf, telefone, email, senha, tipo_de_conta))
    conexao.commit()

def Login(email, senha):
    """Entrada email e senha de um usuário, saída True se email e senha estiverem corretos e Falso caso contrário."""

    cursor.execute('SELECT * FROM cadastro')
    for item in cursor.fetchall():
        if email == item[5] and senha == item[7]:
            if item[6] == 1:
                return UsuarioNormal(item[0])
            elif item[6] == 0:
                return UsuarioADM(item[0])
            elif item[6] > 1 or item[6] < 0:
                return Exception("Erro: encontrada conta com tipo inválido")
    raise EmailSenhaIncorretoError()

def remover_usuario(id):

    cursor.execute('DELETE FROM cadastro WHERE id = ? ', (id,))
    conexao.commit()

def EmprestimosUsuario(id):
    """Entrada ID do usuário, saída relatório dos emprestimos de livros com código do livro, data de emprestimo e data de devolução"""
    
    cursor.execute('SELECT codigo_livro, data_emprestimo, data_devolucao, id_usuario FROM emprestimos')
    emprestimos = []
    for line in cursor.fetchall():
        if line[3] == id:
            emprestimos.append(line)
    return emprestimos 
     
def usuariosComAtraso():
    """Retorna uma lista com os id dos usuários em atraso"""
    cursor.execute('SELECT id_usuario, status FROM emprestimos')
    idAtrasados = []
    for line in cursor.fetchall():
        data = str(line[1])
        data_atual = date.today()
        data_entrega = datetime.strptime(data, '%Y-%m-%d').date()
        if data_atual > data_entrega:
            idAtrasados.append(line[2])
    return idAtrasados

def getUsuario(id) -> Tuple:
    """ Retorna o usuario de acordo com o id """
    cursor.execute("SELECT * FROM cadastro")
    for conta in cursor.fetchall():
        if conta[0] == id:
            return conta
    raise ValueError("Nenhum usuário com este id")

def getID(email) -> int:
    """ Retorna o id de acordo com o email """
    cursor.execute("SELECT * FROM cadastro")
    for conta in cursor.fetchall():
        if conta[5] == email:
            return conta[0]
    raise ValueError("Nenhum usuário com este email")

def setInUsuarios(id:int, vr:str, vl:str):
    """ Muda a coluna (vr) pelo valor (vl) onde se encontra o id (id) """
    cursor.execute(f"UPDATE cadastro SET {vr} = ? WHERE id = ?", (vl, id))
    conexao.commit()

def countUsuários(tipo: int | None = None):
    cursor.execute("SELECT * FROM cadastro")
    i = 0
    for conta in cursor.fetchall():
        if tipo == None:
            i += 1
        elif conta[6] == tipo:
            i += 1

    return i

##############################################################################################
# Emprestimos
##############################################################################################

def registrosEmprestimos(data_emprestimo,data_devoluçao,id_usuario, codigo_livro):
    """Insere os dados de emprestimos do banco de dados"""
    cursor.execute('INSERT INTO emprestimos (data_emprestimo, data_devolucao, id_usuario, codigo_livro) VALUES (?,?,?,?)',(data_emprestimo,data_devoluçao,id_usuario, codigo_livro))
    conexao.commit()

@overload
def LeEmprestimos(livro, id: int): ...
@overload
def LeEmprestimos(usuario, id: int): ...

def LeEmprestimos(key, id):
    """ Lê todos os empréstimos relacionados a uma instância de usuário ou livro """

    if type(key) == UsuarioNormal or type(key) == UsuarioADM:
        idLoc = 2           
    elif type(key) == Livro:
        idLoc = 3
    else:
        raise TypeError

    resultados = []
    cursor.execute("SELECT * FROM emprestimos")
    for valor in cursor.fetchall():
        if valor[idLoc] == id:
            resultados.append(valor)

    return resultados

    # retorno = []
    # for resultado in resultados:
    #     retorno.append(Emprestimo(resultado[0],resultado[1],resultado[2],resultado[3]))
    # return retorno

def devolucaoLivros(codigo):

    cursor.execute('UPDATE emprestimos SET status = ? WHERE codigo_livro = ?', ('entregue', codigo))
    conexao.commit()

def renovaçãoEmprestimo(nova_data_devolução,codigo_livro):
    """Altera os dados de emprestimos do banco de dados"""
    cursor.execute('UPDATE emprestimos SET data_devoluçao = ? WHERE codigo_livro = ?', (nova_data_devolução,codigo_livro))
    conexao.commit()

##############################################################################################
# Classes
##############################################################################################

class Livro():
    """
    Representação de um livro do banco de dados \n 
    Possui duas sobrecargas na inicialização: na primeira,
    é criado um novo elemento na tabela usando os argumentos
    requisitados e se retorna uma instância de Livro que representa
    esse elemento, na segunda, se retorna uma instância de Livro 
    que corresponde ao argumento codigo (nenhum elemento é criado). 
    Tentar buscar um livro com um id inexistente também ocasionará
    em um erro. \n
    ATENÇÃO: Incompleta, setters das variáveis não estão funcionando
    ainda.
    """
    @overload
    def __init__(self, Nome: str, Autor: str, Genero: str, Estante: str, LdeAmostra: str): ... 
    @overload 
    def __init__(self, Codigo:int): ...

    def __init__(self, CodigoNome, Autor = None, Genero = None, Estante = None, LdeAmostra = None) -> None:
        if type(CodigoNome) == str:
            if type(CodigoNome) != str or type(Autor) != str or type(Genero) != str or type(Estante) != str or type(LdeAmostra) != str:
                raise TypeError()

            cadastro_livros(CodigoNome, Autor, Genero, Estante, LdeAmostra)
        else:
            if type(CodigoNome) != int:
                raise TypeError()
            
            self.__Codigo = CodigoNome

    @property
    def nome(self):
        return getLivros(Codigo=self.codigo)[0][0]

    @property
    def autor(self):
        return getLivros(Codigo=self.codigo)[0][1]

    @property
    def genero(self):
        return getLivros(Codigo=self.codigo)[0][2]
    
    @property
    def codigo(self):
        return self.__Codigo
    
    @property
    def estante(self):
        return getLivros(Codigo=self.codigo)[0][4]

    @property
    def linkDeAmostra(self):
        return getLivros(Codigo=self.codigo)[0][5]

    @property
    def disponibilidade(self):
        
        emprestimo = LeEmprestimos(self, self.codigo)
        dataEmp = datetime.date(int(emprestimo[0][0].split(" ")[0]),int(emprestimo[0][0].split(" ")[1]),int(emprestimo[0][0].split(" ")[2]))
        dataDev = datetime.date(int(emprestimo[0][1].split(" ")[0]),int(emprestimo[0][1].split(" ")[1]),int(emprestimo[0][1].split(" ")[2]))
        
        if len(emprestimo) > 0:
            if dataEmp > datetime.datetime.today().date():
                return "reservado"
            if dataDev < datetime.datetime.today().date():
                return "atrasado"
            else:
                return "emprestado"
        else:
            return "disponível"

    def apagar(self):
        """ 
        Apaga o elemento que esta instância referencia no banco de dados. A instância 
        continuará existindo, entretanto referenciando um elemento inexistente e 
        causará erros se for tentado acessar ou mudar estes valores 
        """
        remover_livro(self.codigo)

class Conta(ABC):
    """ 
    Representação abstrata de uma conta do banco de dados \n 
    Possui duas sobrecargas na inicialização: na primeira,
    é criado um novo elemento na tabela usando os argumentos
    requisitados e se retorna uma instância de Conta que representa
    esse elemento, na segunda, se retorna uma instância de Conta que
    corresponde ao argumento id (nenhum elemento é criado). Tentar
    criar uma conta com um email já em uso ocasionará em um erro. Tentar
    buscar uma conta com um id inexistente também ocasionará
    em um erro. \n
    ATENÇÃO: Esta classe, por ser abstrata, não deve ser instanciada.
    Para instanciar, use ContaNormal ou ContaADM no lugar.
    """
    @overload
    def __init__(self, nome: str, endereço: str, cpf: int, telefone: int, email: str, senha: str, tipo: int): ... 
    @overload 
    def __init__(self, id: int): ...

    def __init__(self, idNome = None, endereço = None, cpf = None, telefone = None, email = None, senha = None, tipo = None) -> None:
        if type(idNome) == str:
            if type(idNome) != str or type(endereço) != str or type(cpf) != str or type(telefone) != int or type(email) != str or type(senha) != str:
                raise TypeError("Algum(ns) Argumento(s) tem(têm) o tipo incorreto!")
            if not validarCpf(str(cpf)):
                raise ValueError("O cpf não é válido")
            if tipo != 0 and tipo != 1:
                raise ValueError("Tipo fora do raio previsto (0-1)")
        
            cadastroUsuario(idNome, endereço, cpf, telefone, email, senha, tipo)
        
            self.__id = getID(email)
        else:
            if type(idNome) != int:
                raise TypeError("Id não é integer")

            self.__id = idNome

    @property
    def nome(self):
        return getUsuario(self.id)[1]
    @nome.setter
    def nome(self,value):
        setInUsuarios(self.id,"Nome",value)

    @property
    def endereço(self):
        return getUsuario(self.id)[2]
    @endereço.setter
    def endereço(self, value):
        setInUsuarios(self.id,"Endereço",value)

    @property
    def cpf(self):
        return getUsuario(self.id)[3]
    @cpf.setter
    def cpf(self, value):
        if validarCpf(value):
            setInUsuarios(self.id,"Cpf",value)
        else:
            raise ValueError("CPF inapropriado")

    @property
    def telefone(self):
        return getUsuario(self.id)[4]
    @telefone.setter
    def telefone(self, value):
        setInUsuarios(self.id,"Telefone",value)

    @property
    def email(self):
        return getUsuario(self.id)[5]
    @email.setter
    def email(self, value):
        setInUsuarios(self.id,"Email",value)

    @property
    def senha(self):
        return getUsuario(self.id)[7]
    @senha.setter
    def senha(self, value):
        setInUsuarios(self.id,"Senha",value)

    @property
    def id(self):
        """ 
        Propriedade chave de uma classe Conta. 
        O id é a conexão entre a instância da Classe
        e as contas no banco de dados, portanto
        mudar o id significa mudar que conta a instância
        representa. \n
        ATENÇÃO: Isso significa que alterar o id da classe
        não vai mudar o id do banco de dados, apenas mudará 
        a conta usada.
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def livrosEmprestados(self):
        return LeEmprestimos(self, self.id)

    @abstractmethod
    def apagar(self):
        """ 
        Apaga o elemento que esta instância referencia no banco de dados. A instância 
        continuará existindo, entretanto referenciando um elemento inexistente e 
        causará erros se for tentado acessar ou mudar estes valores 
        """
        remover_usuario(self.id)

    @staticmethod
    def getConta(id):
        """ Insere o id e retorna diretamente uma instância de classe Usuário ou ADM dependendo do tipo de conta """
        try:
            conta = UsuarioNormal(id)
        except TipoDeContaErradoError:
            conta = UsuarioADM(id)
        except ValueError as error:
            raise ValueError(error)
        
        return conta
            
    def __str__(self) -> str:
        return f"Tipo: {type(self)}; Nome: {self.nome}; Endereço: {self.endereço}; Cpf: {self.cpf}; Telefone: {self.telefone}; Email: {self.email}; Senha: {self.senha}; Livros emprestados: {self.livrosEmprestados}"

class UsuarioNormal(Conta):
    @overload
    def __init__(self, nome: str, endereço: str, cpf: str, telefone: int, email: str, senha: str): ...
    @overload
    def __init__(self, id: int): ...    
    def __init__(self, idNome = None, endereço = None, cpf = None, telefone = None, email = None, senha = None):
        if type(idNome) == int:
            super().__init__(idNome)
            if getUsuario(idNome)[6] != 1:
                raise TipoDeContaErradoError(f"O id {idNome} referencia uma conta ADM. Use uma classe UsuarioADM no lugar")
        else:
            super().__init__(idNome, endereço, cpf, telefone, email, senha, 1)  
    def apagar(self):

        if len(self.livrosEmprestados) == 0:
            super().apagar()
        else:
            raise UsuárioNãoQuitadoError

class UsuarioADM(Conta):
    @overload
    def __init__(self, nome: str, endereço: str, cpf: str, telefone: int, email: str, senha: str): ...
    @overload
    def __init__(self, id: int): ...

    def __init__(self, idNome = None, endereço = None, cpf = None, telefone = None, email = None, senha = None):
        if type(idNome) == int:
            super().__init__(idNome)
            if getUsuario(idNome)[6] != 0:
                raise TipoDeContaErradoError(f"O id {idNome} referencia uma conta normal. Use uma classe UsuarioNormal no lugar")
        else:
            super().__init__(idNome, endereço, cpf, telefone, email, senha, 0)

    def apagar(self):
        if countUsuários(0) > 1:
            if len(self.livrosEmprestados) == 0:
                super().apagar()
            else:
                raise UsuárioNãoQuitadoError
        else:
            raise ApagarUnicoAdmError("Não é possível apagar o único ADM")

class Emprestimo():
    def __init__(self, dataEmprestimo, dataDevolução, id, codigo) -> None:
        self.__dataEmprestimo = dataEmprestimo
        self.__dataDevolução = dataDevolução
        self.__id = id
        self.__codigo = codigo

        cursor.execute("SELECT * FROM EMPRESTIMOS")
        for emp in cursor.fetchall():
            
            pass

    @property
    def dataEmprestimo(self):
        return self.__dataEmprestimo
    @property
    def dataDevolução(self):
        return self.__dataDevolução
    @property
    def id(self):
        return self.__id
    @property
    def codigo(self):
        return self.__codigo

    def extenderEmprestimo(self) -> None:
        novaData = self.dataDevolução # + Algo mais
        cursor.execute(f"UPDATE emprestimos SET data_devolucao = ? WHERE data_emprestimo = ?, data_devolucao = ?, id_usuario = ?, codigo_livro = ?", (novaData, self.dataEmprestimo, self.dataDevolução, self.id, self.codigo))
        conexao.commit()

##############################################################################################
# Exceptions 
##############################################################################################

class ApagarUnicoAdmError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class EmailSenhaIncorretoError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UsuárioNãoQuitadoError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TipoDeContaErradoError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)