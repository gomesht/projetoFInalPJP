import sqlite3

def Login(email, senha):
    conexao = sqlite3.connect("DataBase.db")
    cursor = conexao.cursor()
    validador = 0

    while True:
        if validador == 1:
            break
        if validador == 2:
            raise ValueError("Email ou senha Incorretos")
        while True: 
            if email != "":
                break
        while True:
            if senha != "":
                break
        cursor.execute('SELECT email,senha FROM cadastro')
        for item in cursor.fetchall():
            if email == item[0] and senha == item[1]:
                validador = 1
                break
            else:
                validador = 2