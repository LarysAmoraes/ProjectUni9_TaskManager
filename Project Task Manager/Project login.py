from PySimpleGUI import (
    Window, Button, Text, Image, Input, Column, VSeparator, Push, theme, popup, WIN_CLOSED, Checkbox, Frame
)

# Tema
theme('DarkPurple')

# Criando layout
layout_direita = [[Image(filename='Logo.png')]]

layout_esquerda = [
    [Text('E-mail:'), Input(key='-USERNAME-')],
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
            [Text('Nome:'), Input('')],
            [Text('Senha:'), Input('')],
            [Text('E-mail'), Input('')],
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
                name = values[0]
                email = values[1]

                # Salva os valores em algum lugar ou envia para o backend processar

                # Fecha a janela de registro
                register_window.close()
                break

            # Verifica se o usuário fechou a janela de registro
            if event == 'Fechar' or event == WIN_CLOSED:
                register_window.close()
                break

        popup('Registro de usuário concluído com sucesso!')

    # Adicionando função de login
    if event == '-LOGIN-':
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

