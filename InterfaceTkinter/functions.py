import sqlite3
from typing import Literal
from validacaoCPF import validarCpf
from validatorEmail import isEmailValido
import metodos, datetime, time, tkinter.messagebox as mtk, InterfaceTkinter.textsDef as textsDef
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

    if nome == "" or endereço == "" or cpf == "" or telefone == "" or email == "" or senha == "" or senhaNovamente == "":
        janela.mensage("ERRO-CAMPOS-NULOS")
        fechar()
        return
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

    try:
        global ContaAtual
        if type == 1:
            ContaAtual = metodos.UsuarioNormal(nome,endereço,cpf,telefone,email,senha)
        else:
            ContaAtual = metodos.UsuarioADM(nome,endereço,cpf,telefone,email,senha)
    except metodos.sqlite3.IntegrityError:
        janela.mensage("ERRO-VALOR-DUPLICADO")
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
    else:
        janela.mensage("VALIDADO")

    fechar()

def logOut(janela):
    ContaAtual = None
    janela.mensage("LOGOUT")

def proximaJanela(janela):
    janela.levantarJanela()

def emprestimoLivro(cod:str, tipoAção:Literal['r','e','q'], janela, id = None):  
    if not cod.isnumeric():
        janela.mensage("ERRO-ENTRADA-INVALIDA")
        return
    if tipoAção == 'e':
        if not id.isnumeric():
            janela.mensage("ERRO-ENTRADA-INVALIDA")
            return
        else:
            id = int(id)
    cod = int(cod)

    inicializar()

    try:
        Livro(cod)
    except ValueError:
       janela.mensage("ERRO-CODIGO-INEXISTENTE")
       fechar()
       return

    if Livro(cod).disponibilidade != 'disponível' and tipoAção != 'q':
        janela.mensage("ERRO-LIVRO-INDISPONIVEL")
        fechar()
        return
    elif Livro(cod).disponibilidade == 'disponível' and tipoAção == 'q':
        janela.mensage("REDUNDANCIA")
        fechar()
        return

    match tipoAção:
        case "r":
            edate = 7
            id = ContaAtual.id
        case "e":
            edate = 0
        case "q":
            metodos.devolucaoLivros(cod)
            janela.mensage("SUCESSO")
            fechar()
            return

    dataDeEmprestimo = str(datetime.date.today() + datetime.timedelta(edate+0)).replace("-", " ")
    dataDeDevolução  = str(datetime.date.today() + datetime.timedelta(edate+7)).replace("-", " ")

    try:
        metodos.registrosEmprestimos(dataDeEmprestimo, dataDeDevolução, id, cod)
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
        fechar()
        return

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

def cadastrarLivro(nome:str,autor:str,gênero:str,estante:str,link:str,janela:str):
    if nome == "" or autor == "" or gênero == "" or estante == "" or link == "":
        janela.mensage("ERRO-CAMPOS-NULOS")
        return

    confirmation = mtk.askyesno(textsDef.allTranslatedTexts['confirmaçaoadicionarlivroTP'].get(), textsDef.allTranslatedTexts['confirmaçaoadicionarlivroMP'].get())

    if not confirmation:
        janela.mensage("CANCELADO")
        return

    inicializar()
    try:
        metodos.cadastro_livros(nome,autor,gênero,estante,link)
    except Exception as a:
        janela.mensage("ERRO-DESCONHECIDO")
        print(type(a), a)
        return
    else:
        janela.mensage("SUCESSO")
    fechar()

def remover(key:str, isLivro:bool, janela):
    if not key.isnumeric:
        janela.mensage("ERRO-CAMPO-INVÁLIDO")
        return

    key = int(key)
    inicializar()
    if isLivro:
        try:
            metodos.remover_livro(key)
        except sqlite3.IntegrityError:
            janela.mensage("ERRO-LIVRO-USADO")

    else:
        try:
            metodos.remover_livro(key)
        except sqlite3.IntegrityError:
            janela.mensage("ERRO-USUARIO-INQUITADO")

    fechar()

    janela.mensage("SUCESSO")

def verUsuario(key:str, janela):
    if not key.isnumeric():
        janela.mensage("ERRO-CAMPOS-NULOS")
        return
    
    key = int(key)

    inicializar()
    try:
        global _conta
        _conta = Conta.getConta(key)
        _conta.nome
    except ValueError:
        janela.mensage("ERRO-ID-INEXISTENTE")
        fechar()
        return
    except Exception:
        janela.mensage("ERRO-DESCONHECIDO")
        fechar()
        return

    _id         = textsDef.allTranslatedTexts['idexibiçãoL'].get()
    _nome       = textsDef.allTranslatedTexts['nomeexibiçaoL'].get()
    _endereço   = textsDef.allTranslatedTexts['endereçoexibiçaoL'].get()
    _email      = textsDef.allTranslatedTexts['emailexibiçaoL'].get()
    _cpf        = textsDef.allTranslatedTexts['cpfexibiçãoL'].get()
    _telefone   = textsDef.allTranslatedTexts['telefoneexibiçaoL'].get()
    _tipo       = textsDef.allTranslatedTexts['tipodecontaL'].get()

    _id         += " " + str(_conta.id)
    _nome       += " " + _conta.nome
    _endereço   += " " + _conta.endereço
    _email      += " " + _conta.email
    _cpf        += " " + _conta.cpf
    _telefone   += " " + _conta.telefone

    if type(_conta) == UsuarioNormal:
        _tipo   += " " + textsDef.allTranslatedTexts['normal'].get()
    else:
        _tipo   += " " + textsDef.allTranslatedTexts['administrador'].get()

    strfinal = _id + "\n" + _nome + "\n" + _endereço + "\n" + _email + "\n" + _cpf + "\n" + _telefone + "\n" + _tipo       

    mtk.showinfo(textsDef.allTranslatedTexts['tituloexibiçãoL'].get(), strfinal)

    janela.mensage("SUCESSO")
    fechar()

def carregarInformações(janela, isLivros):
    
    if isLivros:
        inicializar()
        livros = metodos.getLivros()
        fechar()

        janela.atualizar(livros)
    else:
        inicializar()
        ids = metodos.usuariosComAtraso()

        users = []
        for id in ids:
            users.append([Conta.getConta(id).id, Conta.getConta(id).nome, Conta.getConta(id).cpf, Conta.getConta(id).endereço, Conta.getConta(id).telefone, Conta.getConta(id).email])
        fechar()

        janela.atualizar(users)

#