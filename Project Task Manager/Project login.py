import sqlite3
from PySimpleGUI import (
    Window, Button, Text, Image, Input, Column, VSeparator, Push, theme, popup, WIN_CLOSED, Checkbox, Frame
)

# Tema
theme('DarkPurple')

# Funções de banco de dados
def criar_tabela_usuarios():
    conn = sqlite3.connect('login_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def registrar_usuario(name, email, password):
    conn = sqlite3.connect('login_database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def verificar_usuario(email, password):
    conn = sqlite3.connect('login_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        return True
    else:
        popup('Credenciais inválidas.')
        return False

# Criando o banco de dados e a tabela de usuários
criar_tabela_usuarios()

# Criando layout
layout_direita = [[Image(filename='Logo.png')]]

layout_esquerda = [
    [Text('E-mail:'), Input(key='-EMAIL-')],
    [Text('Senha:'), Input(password_char='*', key='-PASSWORD-')],
    [Push(), Button('Login', key='-LOGIN-'), Button('Registre-se'), Push()]
]

layout = [[Column(layout_direita), VSeparator(), Column(layout_esquerda)]]

window = Window(
    'Task Manager',
    layout=layout,
    element_justification='c'
)

# Loop principal do programa
while True:
    event, values = window.read()

    # Verifica se o usuário clicou no botão "Registre-se"
    if event == 'Registre-se':
        # Definir layout da janela de Registro
        register_layout = [
            [Text('Nome:'), Input(key='-NAME_REG-')],
            [Text('E-mail:'), Input(key='-EMAIL_REG-')],
            [Text('Senha:'), Input(password_char='*', key='-PASSWORD_REG-')],
            [Button('Cadastrar')]
        ]

        # Criando janela de registro
        register_window = Window('Cadastro de Usuários', register_layout)

        # Loop da janela de registro
        while True:
            event, values = register_window.read()

            # Verifica se o usuário clicou no botão "Cadastrar"
            if event == 'Cadastrar':
                # Obtém os valores dos campos do formulário
                name = values['-NAME_REG-']
                email = values['-EMAIL_REG-']
                password = values['-PASSWORD_REG-']

                # Registra o usuário no banco de dados
                if registrar_usuario(name, email, password):
                    register_window.close()
                    break
                else:
                    popup('E-mail já existente. Por favor, escolha outro.')

            # Ver
                        # Verifica se o usuário fechou a janela de registro
            if event == 'Fechar' or event == WIN_CLOSED:
                register_window.close()
                break

        popup('Registro de usuário concluído com sucesso!')

    # Adicionando função de login
    if event == '-LOGIN-':
        # Obtém os valores dos campos de login
        email = values['-EMAIL-']
        password = values['-PASSWORD-']

        # Verifica se as credenciais são válidas
        if verificar_usuario(email, password):
            popup('Login realizado com sucesso!')

            linha = [[Checkbox(''), Input('')]]
            layout = [[Frame('TaskManager', layout=linha, key='container')], [Button('Nova Tarefa'), Button('Resetar Tarefas')]]
            janela = Window('TaskManager', layout=layout, finalize=True)

            # Loop da janela de login
            while True:
                event, values = janela.read()

                if event == WIN_CLOSED: # Verifica se o usuário fechou a janela de login
                    break

                elif event == 'Nova Tarefa':
                    janela.extend_layout(janela['container'], [[Checkbox(''), Input('')]])

                elif event == 'Resetar Tarefas':
                    janela.close()
                    linha = [[Checkbox(''), Input('')]]
                    layout = [[Frame('TaskManager', layout=linha, key='container')], [Button('Nova Tarefa'), Button('Resetar Tarefas')]]
                    janela = Window('TaskManager', layout=layout, finalize=True)

            # Verifica se o usuário fechou a janela principal
            if event == WIN_CLOSED:
                break

            # Encerra a janela de login
            janela.close()

    # Verifica se o usuário fechou a janela principal
    if event == WIN_CLOSED:
        break

