from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import Menu, ttk

from InterfaceTkinter.functions import proximaJanela

if __name__ == "InterfaceTkinter.windowDef":
    import InterfaceTkinter.functions as functions, InterfaceTkinter.textsDef as textsDef
elif __name__ == "__main__":
    import functions, textsDef

class ValoresInterface():
    """ Estrutura contendo todos os valores nescessários para a interface """

    @staticmethod
    def texts():
        """ Textos utilizados na interface """
        return textsDef.allTranslatedTexts

    @staticmethod
    def atualizarTexts(idioma = None):
        """ Atualiza os textos da interface variando com o argumento idioma """
        textsDef.changerLanguage(master, idioma)

    @staticmethod
    @property
    def configurações_da_interface():
        """ Configurações de página do programa """
        return

class JanelaPrograma(ABC):
    """ Classe-auxiliar com os métodos que toda janela deve ter """
    def levantarJanela(self):
        self.tkraise()
        for wd in self.children.values():
            wd.tkraise()

    @abstractmethod
    def mensage(self, msg:str):
        print(msg)

class JanelaMenuInicial(tk.Frame, JanelaPrograma):
    """ Menu inicial """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.botão_login    = ttk.Button(self,textvariable=ValoresInterface.texts()['loginB'],command=lambda:functions.proximaJanela(jl))
        self.botão_cadastro = ttk.Button(self,textvariable=ValoresInterface.texts()['cadastroB'],command=lambda:functions.proximaJanela(jcd))
        self.botão_fechar   = ttk.Button(self,textvariable=ValoresInterface.texts()['sairB'],command=self.master.quit)

        self.botão_login.grid(column=0, row=0)
        self.botão_cadastro.grid(column=0, row=1)
        self.botão_fechar.grid(column=0, row=2)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        ...

class JanelaLogin(tk.Frame, JanelaPrograma):
    """ Janela de login """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_entrada_email = tk.StringVar(self)
        self.value_entrada_senha = tk.StringVar(self)

        self.label_email    = ttk.Label(self, textvariable=ValoresInterface.texts()['emailL'])
        self.label_senha    = ttk.Label(self, textvariable=ValoresInterface.texts()['senhaL'])
        self.entrada_email  = ttk.Entry(self, textvariable=self.value_entrada_email)
        self.entrada_senha  = ttk.Entry(self, textvariable=self.value_entrada_senha)
        self.botão_validar  = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda jnl=self:functions.validarConta(self.value_entrada_email.get(),self.value_entrada_senha.get(),jnl))
        self.botão_voltar   = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:functions.proximaJanela(jmi))
        self.label_errormsg = ttk.Label(self, textvariable=None, foreground="red")

        self.label_email    .grid(column=0,row=0)
        self.label_senha    .grid(column=0,row=1)
        self.entrada_email  .grid(column=1,row=0)
        self.entrada_senha  .grid(column=1,row=1)
        self.botão_validar  .grid(column=0,row=2)
        self.botão_voltar   .grid(column=1,row=2)
        self.label_errormsg .grid(column=3,row=2)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == "ERRO-CAMPOS-NULOS":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errocamposnulos'])
        if msg == "ERRO-EMAIL-SENHA-INCORRETO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errosenhaincorreta'])
        if msg == "ERRO-DESCONHECIDO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errodesconhecido'])
        if msg == "CLEAR":
            self.label_errormsg = None
        if msg == "VALIDADO-USUARIO":
            proximaJanela(jmiu)
        if msg == "VALIDADO-ADM":
            proximaJanela(jmiadm)

class JanelaCadastro(tk.Frame, JanelaPrograma):
    """ Janela de cadastro """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_entrada_email           = tk.StringVar(self)
        self.value_entrada_senha           = tk.StringVar(self)
        self.value_entrada_senha_novamente = tk.StringVar(self)
        self.value_entrada_nome            = tk.StringVar(self)
        self.value_entrada_cpf             = tk.StringVar(self)
        self.value_entrada_endereço        = tk.StringVar(self)
        self.value_entrada_telefone        = tk.StringVar(self)

        self.label_email             = ttk.Label(self, textvariable=ValoresInterface.texts()['emailL'])
        self.label_senha             = ttk.Label(self, textvariable=ValoresInterface.texts()['senhaL'])
        self.label_senha_novamente   = ttk.Label(self, textvariable=ValoresInterface.texts()['senhanovamenteL'])
        self.label_nome              = ttk.Label(self, textvariable=ValoresInterface.texts()['nomeL'])
        self.label_cpf               = ttk.Label(self, textvariable=ValoresInterface.texts()['cpfL'])
        self.label_endereço          = ttk.Label(self, textvariable=ValoresInterface.texts()['endereçoL'])
        self.label_telefone          = ttk.Label(self, textvariable=ValoresInterface.texts()['telefoneL'])
        self.label_errormsg          = ttk.Label(self, textvariable=None, foreground='red')

        self.entrada_email           = ttk.Entry(self, textvariable=self.value_entrada_email          )
        self.entrada_senha           = ttk.Entry(self, textvariable=self.value_entrada_senha          )
        self.entrada_senha_novamente = ttk.Entry(self, textvariable=self.value_entrada_senha_novamente)
        self.entrada_nome            = ttk.Entry(self, textvariable=self.value_entrada_nome           )
        self.entrada_cpf             = ttk.Entry(self, textvariable=self.value_entrada_cpf            )
        self.entrada_endereço        = ttk.Entry(self, textvariable=self.value_entrada_endereço       )
        self.entrada_telefone        = ttk.Entry(self, textvariable=self.value_entrada_telefone       )

        self.botão_validar           = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.cadastrarConta(self.value_entrada_nome.get(), self.value_entrada_endereço.get(), self.value_entrada_cpf.get(),self.value_entrada_telefone.get(),self.value_entrada_email.get(),self.value_entrada_senha.get(),self.value_entrada_senha_novamente.get(),1,self))
        self.botão_voltar            = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:functions.proximaJanela(jmi))

        self.label_email            .grid(column=0, row=0) 
        self.label_senha            .grid(column=0, row=1) 
        self.label_senha_novamente  .grid(column=0, row=2) 
        self.label_nome             .grid(column=0, row=3) 
        self.label_cpf              .grid(column=0, row=4) 
        self.label_endereço         .grid(column=0, row=5) 
        self.label_telefone         .grid(column=0, row=6)

        self.entrada_email          .grid(column=1, row=0) 
        self.entrada_senha          .grid(column=1, row=1) 
        self.entrada_senha_novamente.grid(column=1, row=2) 
        self.entrada_nome           .grid(column=1, row=3) 
        self.entrada_cpf            .grid(column=1, row=4) 
        self.entrada_endereço       .grid(column=1, row=5) 
        self.entrada_telefone       .grid(column=1, row=6) 

        self.botão_validar          .grid(column=0, row=7) 
        self.botão_voltar           .grid(column=1, row=7) 
        self.label_errormsg         .grid(column=0,row=8)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == "ERRO-EMAIL-USADO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['erroemailusado'])
        if msg == "ERRO-DESCONHECIDO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errodesconhecido'])
        if msg == "ERRO-EMAIL-INVALIDO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['erroemailinvalido'])
        if msg == "ERRO-CPF-INVALIDO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errocpfinvalido'])
        if msg == "ERRO-SENHAS-DIFERENTES":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errosenhasdiferentes'])
        if msg == "ERRO-CAMPOS-NULOS":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errocamposnulos'])
        if msg == "ERRO-SENHA-INVALIDA":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errosenhainsuficiente'])
        if msg == "VALIDADO":
            proximaJanela(jmiu)

class JanelaMenuInicialUsuário(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo usuário """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.label_saudar = ttk.Label(self,textvariable=ValoresInterface.texts()['saudaçaoL'])
        self.botão_pesquisar_livro = ttk.Button(self,textvariable=ValoresInterface.texts()['psqlivroB'], command=lambda:functions.proximaJanela(jpl))
        self.botão_reservar_livro = ttk.Button(self,textvariable=ValoresInterface.texts()['rsvlibroB'], command=lambda:functions.proximaJanela(jrsl))
        self.botão_sugerir_livro = ttk.Button(self,textvariable=ValoresInterface.texts()['sgrlivroB'], command=lambda:functions.proximaJanela(jsl))
        self.botão_alterar_senha = ttk.Button(self,textvariable=ValoresInterface.texts()['altsenhaB'], command=lambda:functions.proximaJanela(jals))
        self.botão_sair = ttk.Button(self, textvariable=ValoresInterface.texts()['sairB'], command=lambda:functions.logOut(self))

        self.label_saudar          .grid(column=0,row=0)
        self.botão_pesquisar_livro .grid(column=0,row=1)
        self.botão_reservar_livro  .grid(column=0,row=2)
        self.botão_sugerir_livro   .grid(column=0,row=3)
        self.botão_alterar_senha   .grid(column=0,row=4)
        self.botão_sair            .grid(column=0,row=5)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == 'LOGOUT':
            functions.proximaJanela(jmi)

class JanelaPesquisarLivros(tk.Frame, JanelaPrograma):
    """ Janela de pesquisa de livros """
    def __init__(self, master) -> None:
        super().__init__(master)

        # changes expected
        self.visualização_livros = ttk.Treeview(self)
        self.scrollbar_visualização_livros = ttk.Scrollbar(self,orient='vertical')
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'],command=lambda:proximaJanela(jmiu))

        self.visualização_livros            .grid(column=0,row=0)
        self.scrollbar_visualização_livros  .grid(column=0,row=0)
        self.botão_voltar                   .grid(column=0,row=1)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        ...

class JanelaReservarLivro(tk.Frame, JanelaPrograma):
    """ Janela de reserva de livro """
    def __init__(self, master) -> None:
        super().__init__(master)
        self.value_id = tk.StringVar(self)

        self.entrada_id = ttk.Entry(self)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiu))

        self.entrada_id    .grid(column=0,row=0)
        self.botão_validar .grid(column=0,row=1)
        self.botão_voltar  .grid(column=1,row=1)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaSugerirLivro(tk.Frame, JanelaPrograma):
    """ Janela de sugestão de livro """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_livrosugerido = tk.StringVar(self)

        self.label_explain = ttk.Label(self, textvariable=ValoresInterface.texts()['sugerirlivrosL'])
        self.entry_livrosugerido = ttk.Entry(self)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'],command=lambda:proximaJanela(jmiu))

        self.label_explain      .grid(column=0,row=0)
        self.entry_livrosugerido.grid(column=0,row=1, sticky=tk.W)
        self.botão_validar      .grid(column=0,row=2, sticky=tk.W)
        self.botão_voltar       .grid(column=0,row=2, sticky=tk.E)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        ...

class JanelaAlterarSenha(tk.Frame, JanelaPrograma):
    """ Janela de mudança de senha """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_senha_atual = tk.StringVar(self)
        self.value_mudança_de_senha = tk.StringVar(self)
        self.value_mudança_de_senha_novamente = tk.StringVar(self)

        self.label_senha_atual = ttk.Label(self, textvariable=ValoresInterface.texts()['senhaL'])
        self.label_mudança_de_senha = ttk.Label(self, textvariable=ValoresInterface.texts()['novasenhaL'])
        self.label_mudança_de_senha_novamente = ttk.Label(self, textvariable=ValoresInterface.texts()['novasenhanovamenteL'])
        self.entrada_senha_atual = ttk.Entry(self, textvariable=self.value_senha_atual)
        self.entrada_mudança_de_senha = ttk.Entry(self, textvariable=self.value_mudança_de_senha)
        self.entrada_mudança_de_senha_novamente = ttk.Entry(self, textvariable=self.value_mudança_de_senha_novamente)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiu))

        self.label_senha_atual                  .grid(column=0,row=0)
        self.label_mudança_de_senha             .grid(column=0,row=1)
        self.label_mudança_de_senha_novamente   .grid(column=0,row=2)
        self.entrada_senha_atual                .grid(column=1,row=0)
        self.entrada_mudança_de_senha           .grid(column=1,row=1)
        self.entrada_mudança_de_senha_novamente .grid(column=1,row=2)
        self.botão_validar                      .grid(column=0,row=3)
        self.botão_voltar                       .grid(column=1,row=3)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaMenuADM(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.label_saudaçao             = ttk.Label(self, textvariable=ValoresInterface.texts()['saudaçaoL'])
        self.botão_emprestimo_livros    = ttk.Button(self, textvariable=ValoresInterface.texts()['emprestimosB'], command=lambda:proximaJanela(je))
        self.botão_devolução_livro      = ttk.Button(self, textvariable=ValoresInterface.texts()['devoluçoesB'], command=lambda:proximaJanela(jd))
        self.botão_ver_usuário          = ttk.Button(self, textvariable=ValoresInterface.texts()['verusuarioB'], command=lambda:proximaJanela(jvu))
        self.botão_usuários_em_atraso   = ttk.Button(self, textvariable=ValoresInterface.texts()['usuariosematrasoB'], command=lambda:proximaJanela(jvuea))
        self.botão_cadastrar_livro      = ttk.Button(self, textvariable=ValoresInterface.texts()['cadastrolivrosB'], command=lambda:proximaJanela(jcl))
        self.botão_remover_livro        = ttk.Button(self, textvariable=ValoresInterface.texts()['removerlivrosB'], command=lambda:proximaJanela(jrl))
        self.botão_remover_usuário      = ttk.Button(self, textvariable=ValoresInterface.texts()['removerusuariosB'], command=lambda:proximaJanela(jru))
        self.botão_cadastro_adm         = ttk.Button(self, textvariable=ValoresInterface.texts()['cadastroadmB'], command=lambda:proximaJanela(jcadm))
        self.botão_sair                 = ttk.Button(self, textvariable=ValoresInterface.texts()['sairB'], command=lambda:proximaJanela(jmi))

        self.label_saudaçao          .grid(column=0,row=0)
        self.botão_emprestimo_livros .grid(column=0,row=1)
        self.botão_devolução_livro   .grid(column=1,row=1)
        self.botão_ver_usuário       .grid(column=0,row=2)
        self.botão_usuários_em_atraso.grid(column=1,row=2)
        self.botão_cadastrar_livro   .grid(column=0,row=3)
        self.botão_remover_livro     .grid(column=1,row=3)
        self.botão_remover_usuário   .grid(column=0,row=4)
        self.botão_cadastro_adm      .grid(column=1,row=4)
        self.botão_sair              .grid(column=0,row=5)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaEmprestimo(tk.Frame, JanelaPrograma):
    """ Janela para um ADM realizar os empréstimos aos usuários """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_id = tk.StringVar(self)
        self.value_codigo = tk.StringVar(self)

        self.label_id = ttk.Label(self, textvariable=ValoresInterface.texts()['entradaidL'])
        self.label_codigo = ttk.Label(self, textvariable=ValoresInterface.texts()['entradacodL'])
        self.entrada_id = ttk.Entry(self, textvariable=self.value_id)
        self.entrada_codigo = ttk.Entry(self, textvariable=self.value_codigo)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))

        self.label_id       .grid(column=0,row=0)
        self.label_codigo   .grid(column=0,row=1)
        self.entrada_id     .grid(column=1,row=0)
        self.entrada_codigo .grid(column=1,row=1)
        self.botão_validar  .grid(column=0,row=2)
        self.botão_voltar   .grid(column=1,row=2)
        
        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaDevolução(tk.Frame, JanelaPrograma):
    """ Janela para quitar um livro """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_código = tk.StringVar(self)

        self.label_código = ttk.Label(self, textvariable=ValoresInterface.texts()['entradacodL'])
        self.entrada_código = ttk.Entry(self, textvariable=self.value_código)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))

        self.label_código   .grid(column=0,row=0)
        self.entrada_código .grid(column=1,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaVerUsuário(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_id = tk.StringVar(self)

        self.label_id = ttk.Label(self, textvariable=ValoresInterface.texts()['entradaidL'])
        self.entrada_id = ttk.Entry(self, textvariable=self.value_id)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))

        self.label_id       .grid(column=0,row=0)
        self.entrada_id     .grid(column=1,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str): ...

class JanelaVerUsuáriosEmAtraso(tk.Frame, JanelaPrograma):
    """ Janela de visualização de usuários em atraso """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.visualização_usuários = ttk.Treeview(self, )
        self.scrollbar_visualização_usuários = ttk.Scrollbar(self)
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))

        self.visualização_usuários          .grid(column=0,row=0)
        self.scrollbar_visualização_usuários.grid(column=0,row=0)
        self.botão_voltar                   .grid(column=0,row=1)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaCadastrarLivro(tk.Frame, JanelaPrograma):
    """ Janela de cadastro de livros """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_nome    = tk.StringVar(self)
        self.value_autor   = tk.StringVar(self)
        self.value_gênero  = tk.StringVar(self)
        self.value_estante = tk.StringVar(self)
        self.value_link    = tk.StringVar(self)

        self.label_nome = ttk.Label(self, textvariable=ValoresInterface.texts()['entradanomeL'])
        self.label_autor = ttk.Label(self, textvariable=ValoresInterface.texts()['entradaautorL'])
        self.label_gênero = ttk.Label(self, textvariable=ValoresInterface.texts()['entradageneroL'])
        self.label_estante = ttk.Label(self, textvariable=ValoresInterface.texts()['entradaestanteL'])
        self.label_link = ttk.Label(self, textvariable=ValoresInterface.texts()['entradalinkL'])
        self.entrada_nome = ttk.Entry(self, textvariable=self.value_nome   )
        self.entrada_autor = ttk.Entry(self, textvariable=self.value_autor  )
        self.entrada_gênero = ttk.Entry(self, textvariable=self.value_gênero )
        self.entrada_estante = ttk.Entry(self, textvariable=self.value_estante)
        self.entrada_link = ttk.Entry(self, textvariable=self.value_link   )
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))

        self.label_nome     .grid(column=0,row=0)
        self.label_autor    .grid(column=0,row=1)
        self.label_gênero   .grid(column=0,row=2)
        self.label_estante  .grid(column=0,row=3)
        self.label_link     .grid(column=0,row=4)

        self.entrada_nome   .grid(column=1,row=0)
        self.entrada_autor  .grid(column=1,row=1)
        self.entrada_gênero .grid(column=1,row=2)
        self.entrada_estante.grid(column=1,row=3)
        self.entrada_link   .grid(column=1,row=4)
        self.botão_validar  .grid(column=0,row=5)
        self.botão_voltar   .grid(column=1,row=5)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaRemoverLivro(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_codigo = tk.StringVar(self)

        self.label_codigo = ttk.Label(self, textvariable=ValoresInterface.texts()['entradacodL'])
        self.entrada_codigo = ttk.Entry(self, textvariable=self.value_codigo)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))

        self.label_codigo   .grid(column=0,row=0)
        self.entrada_codigo .grid(column=1,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaRemoverUsuário(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_id = tk.StringVar(self)

        self.label_id = ttk.Label(self, textvariable=ValoresInterface.texts()['entradaidL'])
        self.entrada_id = ttk.Entry(self, textvariable=self.value_id)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))

        self.label_id       .grid(column=0,row=0)
        self.entrada_id     .grid(column=1,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class JanelaCadastroADM(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_email           = tk.StringVar(self)
        self.value_senha           = tk.StringVar(self)
        self.value_senha_novamente = tk.StringVar(self)
        self.value_nome            = tk.StringVar(self)
        self.value_cpf             = tk.StringVar(self)
        self.value_endereço        = tk.StringVar(self)
        self.value_telefone        = tk.StringVar(self)

        self.label_email           = ttk.Label(self, textvariable=ValoresInterface.texts()['emailL'])
        self.label_senha           = ttk.Label(self, textvariable=ValoresInterface.texts()['senhaL'])
        self.label_senha_novamente = ttk.Label(self, textvariable=ValoresInterface.texts()['senhanovamenteL'])
        self.label_nome            = ttk.Label(self, textvariable=ValoresInterface.texts()['nomeL'])
        self.label_cpf             = ttk.Label(self, textvariable=ValoresInterface.texts()['cpfL'])
        self.label_endereço        = ttk.Label(self, textvariable=ValoresInterface.texts()['endereçoL'])
        self.label_telefone        = ttk.Label(self, textvariable=ValoresInterface.texts()['telefoneL'])

        self.entrada_email = ttk.Entry(self,textvariable=self.value_email)
        self.entrada_senha = ttk.Entry(self,textvariable=self.value_senha)
        self.entrada_senha_novamente = ttk.Entry(self,textvariable=self.value_senha_novamente)
        self.entrada_nome = ttk.Entry(self,textvariable=self.value_nome)
        self.entrada_cpf = ttk.Entry(self,textvariable=self.value_cpf)
        self.entrada_endereço = ttk.Entry(self,textvariable=self.value_endereço)
        self.entrada_telefone = ttk.Entry(self,textvariable=self.value_telefone)

        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))

        self.label_email            .grid(column=0,row=0)
        self.label_senha            .grid(column=0,row=1)
        self.label_senha_novamente  .grid(column=0,row=2)
        self.label_nome             .grid(column=0,row=3)
        self.label_cpf              .grid(column=0,row=4)
        self.label_endereço         .grid(column=0,row=5)
        self.label_telefone         .grid(column=0,row=6)

        self.entrada_email          .grid(column=1,row=0)
        self.entrada_senha          .grid(column=1,row=1)
        self.entrada_senha_novamente.grid(column=1,row=2)
        self.entrada_nome           .grid(column=1,row=3)
        self.entrada_cpf            .grid(column=1,row=4)
        self.entrada_endereço       .grid(column=1,row=5)
        self.entrada_telefone       .grid(column=1,row=6)

        self.botão_validar          .grid(column=0,row=7)
        self.botão_voltar           .grid(column=1,row=7)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        ...

class Master(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('')
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        self.resizable(True, True)

        menuI = Menu(self)
        self.configure(menu=menuI)

        menuIlinguagem = Menu(menuI, tearoff=0)
        menuIlinguagem.add_command(label='pt', command=lambda:ValoresInterface.atualizarTexts('pt'))
        menuIlinguagem.add_command(label='fr', command=lambda:ValoresInterface.atualizarTexts('fr'))
        menuIlinguagem.add_command(label='en', command=lambda:ValoresInterface.atualizarTexts('en'))
        menuI.add_cascade(label="Mudar idioma",menu=menuIlinguagem)

if __name__ == "InterfaceTkinter.windowDef":
    master = Master()
    ValoresInterface.atualizarTexts()

    jmi = JanelaMenuInicial(master)
    jl = JanelaLogin(master)
    jcd = JanelaCadastro(master)

    jmiu = JanelaMenuInicialUsuário(master)
    jpl  = JanelaPesquisarLivros(master)
    jrsl = JanelaReservarLivro(master)
    jsl  = JanelaSugerirLivro(master)
    jals  = JanelaAlterarSenha(master)

    jmiadm = JanelaMenuADM(master)
    je = JanelaEmprestimo(master)
    jd = JanelaDevolução(master)
    jvu = JanelaVerUsuário(master)
    jvuea = JanelaVerUsuáriosEmAtraso(master)
    jcl = JanelaCadastrarLivro(master)
    jrl = JanelaRemoverLivro(master)
    jru = JanelaRemoverUsuário(master)
    jcadm = JanelaCadastroADM(master)

    jmi.levantarJanela()
    master.mainloop()