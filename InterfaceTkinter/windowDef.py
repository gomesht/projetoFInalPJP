import tkinter as tk
from tkinter import ttk

if __name__ == "InterfaceTkinter.windowDef":
    import InterfaceTkinter.functions as functions, InterfaceTkinter.textsDef as textsDef
elif __name__ == "__main__":
    import functions, textsDef

class ValoresInterface():
    """ Estrutura contendo todos os valores nescessários para a interface """

    @staticmethod
    def texts():
        """ Textos utilizados na interface """
        alltxt = {}
        for i in range(len(textsDef.allTranslatedTexts)):
            alltxt.update(  ((   tuple(textsDef.allTranslatedTexts.keys())[i] , tk.StringVar(master,tuple(textsDef.allTranslatedTexts.values())[i])   ),) )
        return alltxt

    @staticmethod
    @property
    def configurações_da_interface():
        """ Configurações de página do programa """
        return

class JanelaPrograma():
    """ Classe-auxiliar com os métodos que toda janela deve ter """
    def levantarJanela(self):
        self.tkraise()
        for wd in self.children.values():
            wd.tkraise()
        
class JanelaMenuInicial(tk.Frame, JanelaPrograma):
    """ Menu inicial """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.botão_login    = ttk.Button(self,textvariable=ValoresInterface.texts()['loginB'])
        self.botão_cadastro = ttk.Button(self,textvariable=ValoresInterface.texts()['cadastroB'])
        self.botão_fechar   = ttk.Button(self,textvariable=ValoresInterface.texts()['sairB'])

        self.botão_login.grid(column=0, row=0)
        self.botão_cadastro.grid(column=0, row=1)
        self.botão_fechar.grid(column=0, row=2)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

class JanelaLogin(tk.Frame, JanelaPrograma):
    """ Janela de login """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.value_entrada_email = tk.StringVar(self)
        self.value_entrada_senha = tk.StringVar(self)

        self.label_email   = ttk.Label(self, textvariable=ValoresInterface.texts()['emailL'])
        self.label_senha   = ttk.Label(self, textvariable=ValoresInterface.texts()['senhaL'])
        self.entrada_email = ttk.Entry(self, textvariable=self.value_entrada_email)
        self.entrada_senha = ttk.Entry(self, textvariable=self.value_entrada_senha)
        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar  = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'])

        # ttk.Label(self, text="b").grid(column=0,row=0)
        # ttk.Label(self, text="b").grid(column=0,row=1)
        # ttk.Label(self, text="b").grid(column=0,row=2)
        # ttk.Label(self, text="b").grid(column=0,row=3)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

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

        self.label_email           = ttk.Label(self, textvariable=ValoresInterface.texts()['voltarB'])
        self.label_senha           = ttk.Label(self, textvariable=ValoresInterface.texts()['voltarB'])
        self.label_senha_novamente = ttk.Label(self, textvariable=ValoresInterface.texts()['voltarB'])
        self.label_nome            = ttk.Label(self, textvariable=ValoresInterface.texts()['voltarB'])
        self.label_cpf             = ttk.Label(self, textvariable=ValoresInterface.texts()['voltarB'])
        self.label_endereço        = ttk.Label(self, textvariable=ValoresInterface.texts()['voltarB'])
        self.label_telefone        = ttk.Label(self, textvariable=ValoresInterface.texts()['voltarB'])

        self.entrada_email           = ttk.Entry(self, textvariable=self.value_entrada_email          )
        self.entrada_senha           = ttk.Entry(self, textvariable=self.value_entrada_senha          )
        self.entrada_senha_novamente = ttk.Entry(self, textvariable=self.value_entrada_senha_novamente)
        self.entrada_nome            = ttk.Entry(self, textvariable=self.value_entrada_nome           )
        self.entrada_cpf             = ttk.Entry(self, textvariable=self.value_entrada_cpf            )
        self.entrada_endereço        = ttk.Entry(self, textvariable=self.value_entrada_endereço       )
        self.entrada_telefone        = ttk.Entry(self, textvariable=self.value_entrada_telefone       )

        self.botão_validar = ttk.Button(self, textvariable=ValoresInterface.texts()['validarB'])
        self.botão_voltar  = ttk.Button(self, textvariable=ValoresInterface.texts()['voltarB'])

        # for i in range(0,10):
        #     ttk.Label(self, text="c").grid(column=i, row=i)

        self.master.update()
        self.place(in_=master, height=self.master.winfo_screenheight(), width=self.master.winfo_screenwidth())

class JanelaMenuInicialUsuário(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo usuário """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.botão_pesquisar_livro = tk.Button(self)
        self.botão_reservar_livro = tk.Button(self)
        self.botão_sugerir_livro = tk.Button(self)
        self.botão_alterar_senha = tk.Button(self)
        self.botão_sair = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaPesquisarLivros(tk.Frame, JanelaPrograma):
    """ Janela de pesquisa de livros """
    def __init__(self, master) -> None:
        super().__init__(master)

        # changes expected
        self.visualização_livros = tk.Button(self)
        self.scrollbar_visualização_livros = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaReservarLivro(tk.Frame, JanelaPrograma):
    """ Janela de reserva de livro """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_id = tk.Button(self)
        self.botão_validar = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaSugerirLivro(tk.Frame, JanelaPrograma): # Isso ainda vai existir?
    """ Janela de sugestão de livro """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.grid(column=0,row=0)

class JanelaAlterarSenha(tk.Frame, JanelaPrograma):
    """ Janela de mudança de senha """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_mudança_de_senha = tk.Button(self)
        self.entrada_mudança_de_senha_novamente = tk.Button(self)
        self.botão_validar = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaMenuADM(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.botão_emprestimo_livros = tk.Button(self)
        self.botão_devolução_livro = tk.Button(self)
        self.botão_ver_usuário = tk.Button(self)
        self.botão_usuários_em_atraso = tk.Button(self)
        self.botão_cadastrar_livro = tk.Button(self)
        self.botão_remover_livro = tk.Button(self)
        self.botão_remover_usuário = tk.Button(self)
        self.botão_cadastro_adm = tk.Button(self)
        self.botão_sair = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaEmprestimo(tk.Frame, JanelaPrograma):
    """ Janela para um ADM realizar os empréstimos aos usuários """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_id = tk.Button(self)
        self.entrada_código = tk.Button(self)
        self.botão_validar = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaDevolução(tk.Frame, JanelaPrograma):
    """ Janela para quitar um livro """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_código = tk.Button(self)
        self.botão_validar = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaVerUsuário(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_id = tk.Button(self)
        self.botão_validar = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaVerUsuáriosEmAtraso(tk.Frame, JanelaPrograma):
    """ Janela de visualização de usuários em atraso """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.visualização_usuários = tk.Button(self)
        self.scrollbar_visualização_usuários = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaCadastrarLivro(tk.Frame, JanelaPrograma):
    """ Janela de cadastro de livros """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_nome = tk.Button(self)
        self.entrada_autor = tk.Button(self)
        self.entrada_gênero = tk.Button(self)
        self.entrada_estante = tk.Button(self)
        self.entrada_link = tk.Button(self)
        self.botão_validar = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaRemoverLivro(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_codigo = tk.Button(self)
        self.botão_validar = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaRemoverUsuário(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_id = tk.Button(self)
        self.botão_validar = tk.Button(self)
        self.botão_voltar = tk.Button(self)

        self.grid(column=0,row=0)

class JanelaCadastroADM(tk.Frame, JanelaPrograma):
    """ Menu de uma conta de tipo ADM """
    def __init__(self, master) -> None:
        super().__init__(master)

        self.entrada_email = ttk.Button(self)
        self.entrada_senha = ttk.Button(self)
        self.entrada_senha_novamente = ttk.Button(self)
        self.entrada_nome = ttk.Button(self)
        self.entrada_cpf = ttk.Button(self)
        self.entrada_endereço = ttk.Button(self)
        self.entrada_telefone = ttk.Button(self)

        self.botão_validar = ttk.Button(self)
        self.botão_voltar = ttk.Button(self)

        self.grid(column=0,row=0)

class Master(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('')
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        self.resizable(True, True)

if __name__ == "InterfaceTkinter.windowDef":
    master = Master()
    j1 = JanelaMenuInicial(master)
    j2 = JanelaLogin(master)
    j3 = JanelaCadastro(master)
    
    j1.levantarJanela()
    master.mainloop()