from abc import ABC, abstractmethod
import tkinter as tk, tkinter.ttk as ttk, tkinter.messagebox as mtk
import tkinter.font as ftk
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

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
    def fonte():
        """ Tamanho do texto e fonte usados """
        if 'Old English Text MT' in ftk.families():
            return ('Old English Text MT', 20)
        elif 'Mongolian Baiti' in ftk.families():
            return ('Mongolian Baiti', 20)
        elif 'Comic Sans MS' in ftk.families():
            return ('Comic Sans MS', 20)

    @staticmethod
    def tamanhoJanela(self):
        """ Tamanho do texto usado """
        return f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}'

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

        self.value_entrada_email = tk.StringVar(self, "ricardo@hotmail.com")
        self.value_entrada_senha = tk.StringVar(self, "757275")

        self.label_email    = ttk.Label(self, textvariable=ValoresInterface.texts()['emailL'])
        self.label_senha    = ttk.Label(self, textvariable=ValoresInterface.texts()['senhaL'])
        self.entrada_email  = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_email)
        self.entrada_senha  = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_senha)
        self.botão_validar  = ttk.Button(self,textvariable=ValoresInterface.texts()['validarB'], command=lambda jnl=self:functions.validarConta(self.value_entrada_email.get().strip(),self.value_entrada_senha.get().strip(),jnl))
        self.botão_voltar   = ttk.Button(self,textvariable=ValoresInterface.texts()['voltarB'], command=lambda:functions.proximaJanela(jmi))
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

        self.entrada_email           = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_email          )
        self.entrada_senha           = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_senha          )
        self.entrada_senha_novamente = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_senha_novamente)
        self.entrada_nome            = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_nome           )
        self.entrada_cpf             = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_cpf            )
        self.entrada_endereço        = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_endereço       )
        self.entrada_telefone        = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_entrada_telefone       )

        self.botão_validar           = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.cadastrarConta(self.value_entrada_nome.get().strip(), self.value_entrada_endereço.get().strip(), self.value_entrada_cpf.get().strip(),self.value_entrada_telefone.get().strip(),self.value_entrada_email.get().strip(),self.value_entrada_senha.get().strip(),self.value_entrada_senha_novamente.get().strip(),1,self))
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

        self.visualização_livros = ttk.Treeview(self, columns=["nome","autor","genero","codigo","estante","link"], show='headings')
        self.visualização_livros.heading('nome', text="nome")
        self.visualização_livros.column('#1', width=500, anchor='center')
        self.visualização_livros.heading('autor', text="autor")
        self.visualização_livros.column('#2', width=400, anchor='center')
        self.visualização_livros.heading('genero', text="genero")
        self.visualização_livros.column('#3', width=400, anchor='center')
        self.visualização_livros.heading('codigo', text="codigo")
        self.visualização_livros.column('#4', width=100, anchor='center')
        self.visualização_livros.heading('estante', text="estante")
        self.visualização_livros.column('#5', width=75, anchor='center')
        self.visualização_livros.heading('link', text="link")
        self.visualização_livros.column('#6', width=300, anchor='center')

        self.scrollbar_visualização_livros = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.visualização_livros.yview)
        self.visualização_livros.configure(yscrollcommand=self.scrollbar_visualização_livros.set)

        self.botão_reload = ttk.Button(self, textvariable=ValoresInterface.texts()['reloadB'],command=lambda:functions.carregarInformações(self, True))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'],command=lambda:proximaJanela(jmiu))

        functions.carregarInformações(self, True)

        self.visualização_livros            .grid(column=0,row=0,columnspan=4)
        self.scrollbar_visualização_livros  .grid(column=5,row=0, sticky='ns')
        self.botão_reload                   .grid(column=0,row=1, sticky='w')
        self.botão_voltar                   .grid(column=0,row=1, sticky='e')


        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def atualizar(self, values):
        self.visualização_livros.delete(*self.visualização_livros.get_children())

        for livro in values:
            self.visualização_livros.insert('', tk.END, values=livro)

    def mensage(self, msg:str):
        ...

class JanelaReservarLivro(tk.Frame, JanelaPrograma):
    """ Janela de reserva de livro """
    def __init__(self, master) -> None:
        super().__init__(master)
        self.value_codigo = tk.StringVar(self)

        self.label_codigo = ttk.Label(self, textvariable=ValoresInterface.texts()['codigoL'])
        self.entrada_codigo = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_codigo)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.emprestimoLivro(self.entrada_codigo.get().strip(),'r', self))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiu))
        self.label_erro = tk.Label(self)

        self.entrada_codigo .grid(column=0,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)
        self.label_erro     .grid(column=0,row=2)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == "ERRO-ENTRADA-INVALIDA":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['erronan'], foreground='red')
        if msg == "ERRO-CODIGO-INEXISTENTE":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errocodigodesconhecido'], foreground='red')
        if msg == "ERRO-LIVRO-INDISPONIVEL":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errolivroemuso'], foreground='red')
        if msg == "ERRO-DESCONHECIDO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errodesconhecido'], foreground='red')
        if msg == "SUCESSO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'], foreground='green')

class JanelaSugerirLivro(tk.Frame, JanelaPrograma):
    """ Janela de sugestão de livro """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_livrosugerido = tk.StringVar(self)

        self.label_explain = ttk.Label(self, textvariable=ValoresInterface.texts()['sugerirlivrosL'])
        self.entry_livrosugerido = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_livrosugerido)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.addSugestão(self.value_livrosugerido.get().strip(), jsl))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'],command=lambda:proximaJanela(jmiu))
        self.label_erro = ttk.Label(self)

        self.label_explain      .grid(column=0,row=0)
        self.entry_livrosugerido.grid(column=0,row=1, sticky=tk.W)
        self.botão_validar      .grid(column=0,row=2, sticky=tk.W)
        self.botão_voltar       .grid(column=0,row=2, sticky=tk.E)
        self.label_erro         .grid(column=0,row=3, sticky=tk.W)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == "ERRO-CAMPO-NULO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errocamposnulos'], foreground='red')
        if msg == "SUCESSO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'], foreground='green')

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
        self.entrada_senha_atual = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_senha_atual)
        self.entrada_mudança_de_senha = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_mudança_de_senha)
        self.entrada_mudança_de_senha_novamente = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_mudança_de_senha_novamente)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.alterarSenha(self.value_senha_atual.get().strip(), self.value_mudança_de_senha.get().strip(), self.value_mudança_de_senha_novamente.get().strip(), self))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiu))
        self.label_erro = ttk.Label(self)

        self.label_senha_atual                  .grid(column=0,row=0)
        self.label_mudança_de_senha             .grid(column=0,row=1)
        self.label_mudança_de_senha_novamente   .grid(column=0,row=2)
        self.entrada_senha_atual                .grid(column=1,row=0)
        self.entrada_mudança_de_senha           .grid(column=1,row=1)
        self.entrada_mudança_de_senha_novamente .grid(column=1,row=2)
        self.botão_validar                      .grid(column=0,row=3)
        self.botão_voltar                       .grid(column=1,row=3)
        self.label_erro                         .grid(column=0,row=4)


        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        if msg == "ERRO-CAMPOS-NULOS":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errocamposnulos'], foreground='red')
        if msg == "ERRO-SENHA-INCORRETA": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errosenhaerrada'], foreground='red')
        if msg == "ERRO-CRITICO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errocritico'], foreground='red')
        if msg == "ERRO-DESCONHECIDO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errodesconhecido'], foreground='red')
        if msg == "ERRO-SENHAS-DIFERENTES":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errosenhasdiferentes'], foreground='red')
        if msg == "ERRO-SENHA-FRACA":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errosenhainsuficiente'], foreground='red')
        if msg == "SUCESSO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'], foreground='green')

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
        self.entrada_id = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_id)
        self.entrada_codigo = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_codigo)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.emprestimoLivro(self.value_codigo.get().strip(),'e',self,self.value_id.get().strip()))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))
        self.label_erro = ttk.Label(self)

        self.label_id       .grid(column=0,row=0)
        self.label_codigo   .grid(column=0,row=1)
        self.entrada_id     .grid(column=1,row=0)
        self.entrada_codigo .grid(column=1,row=1)
        self.botão_validar  .grid(column=0,row=2)
        self.botão_voltar   .grid(column=1,row=2)
        self.label_erro     .grid(column=0,row=3, columnspan=3)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        if msg == "ERRO-ENTRADA-INVALIDA":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['erronan'], foreground='red')
        if msg == "ERRO-CODIGO-INEXISTENTE":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errocodigodesconhecido'], foreground='red')
        if msg == "ERRO-LIVRO-INDISPONIVEL":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errolivroemuso'], foreground='red')
        if msg == "ERRO-DESCONHECIDO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errodesconhecido'], foreground='red')
        if msg == "ERRO-EMPRESTIMOS-DEMAIS":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errousuarionolimite'], foreground='red')
        if msg == "SUCESSO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'], foreground='green')

class JanelaDevolução(tk.Frame, JanelaPrograma): 
    """ Janela para quitar um livro """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_código = tk.StringVar(self)

        self.label_código = ttk.Label(self, textvariable=ValoresInterface.texts()['entradacodL'])
        self.entrada_código = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_código)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.emprestimoLivro(self.value_código.get().strip(), 'q', self))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))
        self.label_erro = ttk.Label(self)

        self.label_código   .grid(column=0,row=0)
        self.entrada_código .grid(column=1,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)
        self.label_erro     .grid(column=0,row=2)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        if msg == "ERRO-ENTRADA-INVALIDA":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['erronan'], foreground='red')
        if msg == "ERRO-CODIGO-INEXISTENTE":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errocodigodesconhecido'], foreground='red')
        if msg == "ERRO-LIVRO-INDISPONIVEL":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errolivroemuso'], foreground='red')
        if msg == "ERRO-DESCONHECIDO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errodesconhecido'], foreground='red')
        if msg == "REDUNDANCIA":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgjaquitado'], foreground='yellow')
        if msg == "SUCESSO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'], foreground='green')

class JanelaVerUsuário(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_id = tk.StringVar(self)

        self.label_id = ttk.Label(self, textvariable=ValoresInterface.texts()['entradaidL'])
        self.entrada_id = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_id)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.verUsuario(self.value_id.get(), self))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))
        self.label_erro = ttk.Label(self)

        self.label_id       .grid(column=0,row=0)
        self.entrada_id     .grid(column=1,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)
        self.label_erro     .grid(column=0,row=2)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == "ERRO-CAMPOS-NULOS": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['erronan'],foreground='red')
        if msg == "ERRO-ID-INEXISTENTE": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['erroiddesconhecido'],foreground='red')
        if msg == "ERRO-DESCONHECIDO": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errodesconhecido'],foreground='red')
        if msg == "SUCESSO": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'],foreground='green')

class JanelaVerUsuáriosEmAtraso(tk.Frame, JanelaPrograma):
    """ Janela de visualização de usuários em atraso """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.visualização_usuarios = ttk.Treeview(self, columns=["id","nome","cpf","endereço","telefone","email"], show='headings')
        self.visualização_usuarios.heading('id', text="id")
        self.visualização_usuarios.column('#1', width=200, anchor='center')
        self.visualização_usuarios.heading('nome', text="nome")
        self.visualização_usuarios.column('#2', width=200, anchor='center')
        self.visualização_usuarios.heading('cpf', text="cpf")
        self.visualização_usuarios.column('#3', width=300, anchor='center')
        self.visualização_usuarios.heading('endereço', text="endereço")
        self.visualização_usuarios.column('#4', width=300, anchor='center')
        self.visualização_usuarios.heading('telefone', text="telefone")
        self.visualização_usuarios.column('#5', width=400, anchor='center')
        self.visualização_usuarios.heading('email', text="email")
        self.visualização_usuarios.column('#6', width=500, anchor='center')

        self.scrollbar_visualização_usuarios = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.visualização_usuarios.yview)
        self.visualização_usuarios.configure(yscrollcommand=self.scrollbar_visualização_usuarios.set)

        self.botão_reload = ttk.Button(self, textvariable=ValoresInterface.texts()['reloadB'],command=lambda:functions.carregarInformações(self, False))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'],command=lambda:proximaJanela(jmiadm))

        functions.carregarInformações(self, False)

        self.visualização_usuarios            .grid(column=0,row=0,columnspan=4)
        self.scrollbar_visualização_usuarios  .grid(column=5,row=0, sticky='ns')
        self.botão_reload                     .grid(column=0,row=1)
        self.botão_voltar                     .grid(column=1,row=1)


        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def atualizar(self, values):
        self.visualização_usuarios.delete(*self.visualização_usuarios.get_children())

        for user in values:
            self.visualização_usuarios.insert('', tk.END, values=user)

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
        self.entrada_nome = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_nome   )
        self.entrada_autor = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_autor  )
        self.entrada_gênero = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_gênero )
        self.entrada_estante = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_estante)
        self.entrada_link = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_link   )
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.cadastrarLivro(self.value_nome.get().strip(), self.value_autor.get().strip(), self.value_gênero.get().strip(), self.value_estante.get().strip(), self.value_link.get().strip(), self))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))
        self.label_erro = ttk.Label(self)

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
        self.label_erro     .grid(column=0,row=6)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == "ERRO-CAMPOS-NULOS": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errocamposnulos'],foreground='red')
        if msg == "CANCELADO": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgcancelado'],foreground='yellow')
        if msg == "ERRO-DESCONHECIDO": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errodesconhecido'],foreground='red')
        if msg == "SUCESSO": 
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'],foreground='green')

class JanelaRemoverLivro(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_codigo = tk.StringVar(self)

        self.label_codigo   = ttk.Label(self, textvariable=ValoresInterface.texts()['entradacodL'])
        self.entrada_codigo = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_codigo)
        self.botão_validar  = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.remover(self.value_codigo.get().strip(), True, self))
        self.botão_voltar   = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))
        self.label_erro     = ttk.Label(self)

        self.label_codigo   .grid(column=0,row=0)
        self.entrada_codigo .grid(column=1,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)
        self.label_erro     .grid(column=0,row=2)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == "ERRO-CAMPO-INVÁLIDO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['erronan'], foreground='red')
        if msg == "ERRO-USUARIO-INQUITADO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errolivroinquitado'])
        if msg == "SUCESSO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'], foreground='green')

class JanelaRemoverUsuário(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_id = tk.StringVar(self)

        self.label_id = ttk.Label(self, textvariable=ValoresInterface.texts()['entradaidL'])
        self.entrada_id = ttk.Entry(self, font=ValoresInterface.fonte(),  textvariable=self.value_id)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.remover(self.value_id.get().strip(), False, self))
        self.botão_voltar = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'], command=lambda:proximaJanela(jmiadm))
        self.label_erro = ttk.Label(self)

        self.label_id       .grid(column=0,row=0)
        self.entrada_id     .grid(column=1,row=0)
        self.botão_validar  .grid(column=0,row=1)
        self.botão_voltar   .grid(column=1,row=1)
        self.label_erro     .grid(column=0,row=2)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

    def mensage(self, msg:str):
        if msg == "ERRO-CAMPO-INVÁLIDO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['erronan'], foreground='red')
        if msg == "ERRO-USUARIO-INQUITADO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['errousuarioinquitado'])
        if msg == "SUCESSO":
            self.label_erro.configure(textvariable=ValoresInterface.texts()['msgsucesso'], foreground='green')

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
        self.label_errormsg        = ttk.Label(self)

        self.entrada_email = ttk.Entry(self, font=ValoresInterface.fonte(), textvariable=self.value_email)
        self.entrada_senha = ttk.Entry(self, font=ValoresInterface.fonte(), textvariable=self.value_senha)
        self.entrada_senha_novamente = ttk.Entry(self, font=ValoresInterface.fonte(), textvariable=self.value_senha_novamente)
        self.entrada_nome = ttk.Entry(self, font=ValoresInterface.fonte(), textvariable=self.value_nome)
        self.entrada_cpf = ttk.Entry(self, font=ValoresInterface.fonte(), textvariable=self.value_cpf)
        self.entrada_endereço = ttk.Entry(self, font=ValoresInterface.fonte(), textvariable=self.value_endereço)
        self.entrada_telefone = ttk.Entry(self, font=ValoresInterface.fonte(), textvariable=self.value_telefone)

        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'], command=lambda:functions.cadastrarConta(self.value_nome.get().strip(), self.value_endereço.get().strip(), self.value_cpf.get().strip(), self.value_telefone.get().strip(), self.value_email.get().strip(), self.value_senha.get().strip(), self.value_senha_novamente.get().strip(), 0, self))
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

        self.label_errormsg         .grid(column=0,row=8)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())


    def mensage(self, msg:str):
        if msg == "ERRO-VALOR-DUPLICADO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['erroemailusado'], foreground='red')
        if msg == "ERRO-DESCONHECIDO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errodesconhecido'], foreground='red')
        if msg == "ERRO-EMAIL-INVALIDO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['erroemailinvalido'], foreground='red')
        if msg == "ERRO-CPF-INVALIDO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errocpfinvalido'], foreground='red')
        if msg == "ERRO-SENHAS-DIFERENTES":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errosenhasdiferentes'], foreground='red')
        if msg == "ERRO-CAMPOS-NULOS":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errocamposnulos'], foreground='red')
        if msg == "ERRO-SENHA-INVALIDA":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['errosenhainsuficiente'], foreground='red')
        if msg == "VALIDADO":
            self.label_errormsg.configure(textvariable=ValoresInterface.texts()['msgsucesso'], foreground='green')

class Master(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('')
        self.geometry(ValoresInterface.tamanhoJanela(self))
        self.resizable(True, True)

        menuI = tk.Menu(self)
        self.configure(menu=menuI)

        menuIlinguagem = tk.Menu(menuI, tearoff=0)
        menuIlinguagem.add_command(label='pt', command=lambda:ValoresInterface.atualizarTexts('pt'))
        menuIlinguagem.add_command(label='fr', command=lambda:ValoresInterface.atualizarTexts('fr'))
        menuIlinguagem.add_command(label='en', command=lambda:ValoresInterface.atualizarTexts('en'))
        menuI.add_cascade(label="Mudar idioma",menu=menuIlinguagem)

if __name__ == "InterfaceTkinter.windowDef":
    master = Master()
    ValoresInterface.atualizarTexts()

    ftk.nametofont('TkDefaultFont').configure(size=20, family=ValoresInterface.fonte()[0])
    ttk.Style().configure('Treeview', rowheight=60, columnwidth=80)

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