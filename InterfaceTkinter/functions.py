import metodos
from metodos import inicializar, fechar, TipoDeContaErradoError, EmailSenhaIncorretoError, UsuárioNãoQuitadoError, ApagarUnicoAdmError

if __name__ == "InterfaceTkinter.windowDef":
    import InterfaceTkinter.windowDef as windowDef, InterfaceTkinter.textsDef as textsDef
elif __name__ == "__main__":
    import windowDef, textsDef

def logarConta(email, senha):
    inicializar()

    try:
        metodos.Login(email,senha)
    except TipoDeContaErradoError:
        ...
    except EmailSenhaIncorretoError:
        ...
    except Exception:
        ...

    ...
    
    fechar()

def cadastrarConta(nome,endereço,cpf,telefone,email,senha,type):
    inicializar()

    try:
        metodos.cadastroUsuario(nome,endereço,cpf,telefone,email,senha,type)
    except Exception:
        ...
    
    ...
    
    fechar()

def pesquisarLivros():
    someVarInTheInterface = metodos.getLivros()

def teste():
    textsDef.changerLanguage()
    windowDef.ValoresInterface.texts()