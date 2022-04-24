from os import system
import mysql.connector
from time import sleep

conexao = mysql.connector.connect(
    host='127.0.0.1', #coloque o ip do seu BD
    user='root',    #nome de User do seu BD
    password='1234', # a senha do BD
    database='bd_cadastro', # o nome do schema do seu BD
)
cursor = conexao.cursor()


def menu(): # Função com o menu no terminal
    print("-=" * 20)
    print(" " * 18, "MENU")
    print("-=" * 20)
    print("[1]-Login\n[2]-Cadastro\n[3]-sair")
    Opc = int(input("Opção: "))
    return Opc


def Cadastro(): # Função cadastro Terminal
    User_cad = input("Usuario: ")
    Pass_cad = input("Senha: ")
    return User_cad, Pass_cad


def Login(): # Função Login Terminal
    user = input("Usuario: ")
    Pass = input("Senha: ")
    return user, Pass

user = [] # Recebe os Usuarios do Banco de dados
while True: # Loop do app
    sleep(5) # Espera 5 segundos para inicar o app
    system('cls')
    opc = menu()
    if opc == 1: # 1º Opção Login
        login, senha = Login() # Inicia a Função Login
        usa = f'SELECT * FROM clientes' #Verificar os Dados do BD
        cursor.execute(usa) # Executa o comando acima
        res = cursor.fetchall() # Me retorna os Dados do BD
        # "Filtra" AS informações do Banco de dados
        for i in res: 
            for a in i:
                if a not in user:
                    user.append(a)
        if login in user: # Verificar se o User digitado esta no BD
            sen = f'SELECT * FROM clientes'
            cursor.execute(sen)
            res = cursor.fetchall()
            user.index(login) # Verifica a Posição do Usuario na Lista User
            if senha == user[user.index(login) + 1]: # Verificar se a senha realmete desse User
                print("-=" * 20)
                print("Login Feito com sucesso")
            else:
                print("-=" * 20)
                print("Login incorreto ou inexistente")
        else:
            print("-=" * 20)
            print("Login incorreto ou inexistente")

    if opc == 2: # 2° Opção Cadastro
        user_c, senha_c = Cadastro()
        if user_c == senha_c: # Verificar se a senha e igual ao User no cadastro
            print("O Usuario não poder ser igual a senha")
        else:
            print('-=' * 20)
            print("Foi registrado com sucesso")
            comando = f'INSERT INTO clientes(nome_user, senha_user) VALUES ("{user_c}", "{senha_c}")' # Enviar novos Dados no BD
            cursor.execute(comando)
            conexao.commit()# Editar o BD
    if opc == 3: # Finalizar o app
        break
