from validacaoCPF import validarCpf
from validatorEmail import isEmailValido
import metodos
from metodos import inicializar, fechar, TipoDeContaErradoError, EmailSenhaIncorretoError, UsuárioNãoQuitadoError, ApagarUnicoAdmError

if __name__ == "InterfaceTkinter.windowDef":
    import InterfaceTkinter.windowDef as windowDef, InterfaceTkinter.textsDef as textsDef
elif __name__ == "__main__":
    import windowDef, textsDef

ContaAtual = None

def validarConta(email, senha, janela):
    inicializar()

    try:
        metodos.Login(email,senha)
    except EmailSenhaIncorretoError:
        janela.mensage("ERRO-EMAIL-SENHA-INCORRETO")
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
    else:
        global ContaAtual
        ContaAtual = metodos.Login(email,senha)
        janela.mensage("VALIDADO")

    fechar()

def cadastrarConta(nome:str,endereço:str,cpf:str,telefone:str,email:str,senha:str,senhaNovamente:str,type:int,janela):
    inicializar()

    if senha != senhaNovamente:
        janela.mensage("ERRO-SENHAS-DIFERENTES")
        return
    if not isEmailValido(email):
        janela.mensage("ERRO-EMAIL-INVALIDO")
        return
    if not validarCpf(email):
        janela.mensage("ERRO-CPF-INVALIDO")
        return
    if nome.strip() == "" or telefone.strip() == "" or endereço.strip() == "":
        janela.mensage("ERRO-CAMPOS-NULOS")
        return

    try:
        metodos.cadastroUsuario(nome,endereço,cpf,telefone,email,senha,type)
    except metodos.sqlite3.IntegrityError:
        janela.mensage("ERRO-EMAIL-USADO")
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
    else:
        janela.mensage("VALIDADO")

    fechar()

def pesquisarLivros():
    someVarInTheInterface = metodos.getLivros()

def proximaJanela(janela):
    janela.levantarJanela()