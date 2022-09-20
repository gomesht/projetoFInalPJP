import sqlite3

def Login():
    conexao = sqlite3.connect("cadastro_de_usuarios.db")
    cursor = conexao.cursor()
    validador = 0
    while True:
        if validador == 1:
            break
        if validador == 2:
            print('\nEmail ou senha incorretos\n')
        while True: 
            email = str(input('Email: ')).lower()
            if email != "":
                break
        while True:
            senha = str(input('Senha: '))
            if senha != "":
                break
        cursor.execute('SELECT email,senha FROM cadastro')
        for item in cursor.fetchall():
            if email == item[0] and senha == item[1]:
                validador = 1
                break
            else:
                validador = 2

Login()
                


        








