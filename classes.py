from typing import overload
from validacaoCPF import * 
from metodos import *      
from abc import *          

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

    def __init__(self, Codigo, Nome, Autor, Genero, Estante, LdeAmostra) -> None:
        if not Codigo:
            if type(Nome) != str or type(Autor) != str or type(Genero) != str or type(Estante) != str or type(LdeAmostra) != str:
                raise TypeError()

            cadastro_livros(Nome, Autor, Genero, Estante, LdeAmostra)
        else:
            if type(Codigo) != int:
                raise TypeError()
            
            self.__Codigo = Codigo

    @property
    def nome(self):
        return getLivros(self.codigo)[3]
    @nome.setter
    def nome(self,value):
        self.__nome = value

    @property
    def codigo(self):
        return self.__Codigo
    @codigo.setter
    def codigo(self,value):
        self.__Codigo = value

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

    @abstractmethod
    def apagar(self):
        """ 
        Apaga o elemento que esta instância referencia no banco de dados. A instância 
        continuará existindo, entretanto referenciando um elemento inexistente e 
        causará erros se for tentado acessar ou mudar estes valores 
        """
        remover_usuario(self.id)

    def __str__(self) -> str:
        return f"Tipo: {type(self)}; Nome: {self.nome}; Endereço: {self.endereço}; Cpf: {self.cpf}; Telefone: {self.telefone}; Email: {self.email}; Senha: {self.senha}"

class UsuarioNormal(Conta):
    @overload
    def __init__(self, nome: str, endereço: str, cpf: str, telefone: int, email: str, senha: str): ...
    @overload
    def __init__(self, id: int): ...

    def __init__(self, idNome = None, endereço = None, cpf = None, telefone = None, email = None, senha = None):
        if type(idNome) == int:
            super().__init__(idNome)
            if getUsuario(idNome)[6] != 1:
                raise ValueError(f"O id {idNome} referencia uma conta ADM. Use uma classe UsuarioADM no lugar")
        else:
            super().__init__(idNome, endereço, cpf, telefone, email, senha, 1)

    def apagar(self):
        super().apagar()

class UsuarioADM(Conta):
    @overload
    def __init__(self, nome: str, endereço: str, cpf: str, telefone: int, email: str, senha: str): ...
    @overload
    def __init__(self, id: int): ...

    def __init__(self, idNome = None, endereço = None, cpf = None, telefone = None, email = None, senha = None):
        if type(idNome) == int:
            super().__init__(idNome)
            if getUsuario(idNome)[6] != 0:
                raise ValueError(f"O id {idNome} referencia uma conta normal. Use uma classe UsuarioNormal no lugar")
        else:
            super().__init__(idNome, endereço, cpf, telefone, email, senha, 0)

    def apagar(self):
        if countUsuários(0) > 1:
            super().apagar()
        else:
            raise ApagarUnicoAdmError("Não é possível apagar o único ADM")

class ApagarUnicoAdmError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)