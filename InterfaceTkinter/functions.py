from validacaoCPF import validarCpf
from validatorEmail import isEmailValido
import metodos, datetime, time
from metodos import Conta, UsuarioNormal, UsuarioADM, Livro, disponibilidadeLivro, inicializar, fechar, TipoDeContaErradoError, EmailSenhaIncorretoError, UsuárioNãoQuitadoError, ApagarUnicoAdmError

if __name__ == "InterfaceTkinter.windowDef":
    import InterfaceTkinter.windowDef as windowDef, InterfaceTkinter.textsDef as textsDef
elif __name__ == "__main__":
    import windowDef, textsDef

ContaAtual = None

def validarConta(email, senha, janela):
    inicializar()

    if email.strip() == "" or senha.strip == "":
        janela.mensage("ERRO-CAMPOS-NULOS")
        fechar()
        return

    try:
        metodos.Login(email,senha)
    except EmailSenhaIncorretoError:
        janela.mensage("ERRO-EMAIL-SENHA-INCORRETO")
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
    else:
        global ContaAtual
        ContaAtual = metodos.Login(email,senha)
        if type(metodos.Login(email,senha)) == UsuarioNormal:
            janela.mensage("VALIDADO-USUARIO")
        else:
            janela.mensage("VALIDADO-ADM")

    fechar()

def cadastrarConta(nome:str,endereço:str,cpf:str,telefone:str,email:str,senha:str,senhaNovamente:str,type:int,janela):
    inicializar()

    if not isEmailValido(email):
        janela.mensage("ERRO-EMAIL-INVALIDO")
        fechar()
        return
    if not validarCpf(cpf):
        janela.mensage("ERRO-CPF-INVALIDO")
        fechar()
        return
    if senha != senhaNovamente:
        janela.mensage("ERRO-SENHAS-DIFERENTES")
        fechar()
        return
    if not metodos.requisitosSenha(senha):
        janela.mensage("ERRO-SENHA-INVALIDA")
        fechar()
        return
    if nome.strip() == "" or telefone.strip() == "" or endereço.strip() == "":
        janela.mensage("ERRO-CAMPOS-NULOS")
        fechar()
        return

    try:
        global ContaAtual
        if type == 1:
            ContaAtual = metodos.UsuarioNormal(nome,endereço,cpf,telefone,email,senha)
        else:
            ContaAtual = metodos.UsuarioADM(nome,endereço,cpf,telefone,email,senha)
    except metodos.sqlite3.IntegrityError:
        janela.mensage("ERRO-EMAIL-USADO")
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
    else:
        janela.mensage("VALIDADO")

    fechar()

def logOut(janela):
    ContaAtual = None
    janela.mensage("LOGOUT")

def pesquisarLivros():
    someVarInTheInterface = metodos.getLivros()

def proximaJanela(janela):
    janela.levantarJanela()

def reservarLivro(cod, janela):
    if not cod.isnumeric():
        janela.mensage("ERRO-ENTRADA-INVALIDA")
        return
    
    cod = int(cod)

    inicializar()

    disponibilidadeLivro(cod)
    try:
        Livro(cod)
    except ValueError:
       janela.mensage("ERRO-CODIGO-INEXISTENTE")
       fechar()
       return

    if Livro(cod).disponibilidade != 'disponível':
        janela.mensage("ERRO-LIVRO-INDISPONIVEL")
        fechar()
        return

    dataDeEmprestimo = str(datetime.date.today() + datetime.timedelta(7)).replace("-", " ")
    dataDeDevolução = str(datetime.date.today() + datetime.timedelta(14)).replace("-", " ")

    try:
        metodos.registrosEmprestimos(dataDeEmprestimo, dataDeDevolução, ContaAtual.id, cod)
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
        fechar()
    else:
        janela.mensage("SUCESSO")
        fechar()

def addSugestão(nome:str, janela):
    inicializar()
    if nome.strip() == "":
        janela.mensage("ERRO-CAMPO-NULO")
        fechar()
    else:
        if not (nome,ContaAtual.id) in metodos.getSugestões():
            metodos.sugestoes_livros(nome.strip(),ContaAtual.id)
        janela.mensage("SUCESSO")
        fechar()

def alterarSenha(senhaAntiga:str, senhaNova:str, senhaNovaNovamente:str, janela):
    inicializar()
    if senhaAntiga.strip() == "" or senhaNova.strip() == "" or senhaNovaNovamente.strip() == "": 
        janela.mensage("ERRO-CAMPOS-NULOS")
        fechar()
        return

    senhaAntiga, senhaNova, senhaNovaNovamente = senhaAntiga.strip(), senhaNova.strip(), senhaNovaNovamente.strip()
    try:
        metodos.Login(ContaAtual.email,senhaAntiga)
    except EmailSenhaIncorretoError:
        janela.mensage("ERRO-SENHA-INCORRETA")
        fechar()
        return
    except TipoDeContaErradoError:
        janela.mensage("ERRO-CRITICO")
        fechar()
        return
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
        fechar()
        return

    if senhaNova != senhaNovaNovamente:
        janela.mensage("ERRO-SENHAS-DIFERENTES")
        fechar()
        return

    if not metodos.requisitosSenha(senhaNova):
        janela.mensage("ERRO-SENHA-FRACA")
        fechar()
        return

    ContaAtual.senha = senhaNova
    fechar()
    janela.mensage("SUCESSO")