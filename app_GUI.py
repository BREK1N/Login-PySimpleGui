from os import system
import mysql.connector
from time import sleep
import PySimpleGUI as sg


def Tela_Login():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Usuario")],
        [sg.Input(key='User')],
        [sg.Text("Senha")],
        [sg.Input(key='senha')],
        [sg.Button("Login", key='login'), sg.Button('Cadastro', key='cadastro')],
        [sg.Text("", key='msg')],

    ]
    return sg.Window('Login', layout=layout, finalize=True)


def Tela_Cadastro():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Usuario")],
        [sg.Input(key='user_c')],
        [sg.Text("Senha")],
        [sg.Input(key='senha_c')],
        [sg.Button("Cadastrar", key='cadastrar')],
        [sg.Text("", key='msg1')],

    ]
    return sg.Window('Cadastro', layout=layout, finalize=True)


conexao = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='1234',
    database='bd_cadastro',
)
cursor = conexao.cursor()

janela1, janela2 = Tela_Login(), None

user = []  # Recebe os Usuarios do Banco de dados
while True:  # Loop do app
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:  # Finalizar o app
        break
    if window == janela1 and event == 'cadastro':  # 2° Opção Cadastro
        janela1.hide()
        janela2 = Tela_Cadastro()
    elif window == janela2 and event == 'cadastrar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == sg.WIN_CLOSED:  # Finalizar o app
        break

    if window == janela1 and event == 'login':  # 1º Opção Login
        usa = f'SELECT * FROM clientes'  # Verificar os Dados do BD
        cursor.execute(usa)  # Executa o comando acima
        res = cursor.fetchall()  # Me retorna os Dados do BD
        # "Filtra" AS informações do Banco de dados
        for i in res:
            for a in i:
                if a not in user:
                    user.append(a)
        if values['User'] in user:  # Verificar se o User digitado esta no BD
            sen = f'SELECT * FROM clientes'
            cursor.execute(sen)
            res = cursor.fetchall()
            # Verifica a Posição do Usuario na Lista User
            user.index(values['User'])
            # Verificar se a senha realmete desse User
            if values['senha'] == user[user.index(values['User']) + 1]:
                window['msg'].update("Login Feito com sucesso")
            else:
                window['msg'].update("Login incorreto ou inexistente")
        else:
            window['msg'].update("Login incorreto ou inexistente")

    # Verificar se a senha e igual ao User no cadastro
    if window == janela2 and event == 'cadastrar':
        if values['user_c'] == values['senha_c']:
            window['msg1'].update("O Usuario não poder ser igual a senha")
            sleep(3)
        else:
            print('-=' * 20)
            print("Foi registrado com sucesso")
            window['msg1'].update("Foi registrado com sucesso")
            # Enviar novos Dados no BD
            comando = f'''INSERT INTO clientes(nome_user, senha_user) VALUES ("{values['user_c']}", "{values['senha_c']}")'''
            cursor.execute(comando)
            conexao.commit()  # Editar o BD
            sleep(3)
