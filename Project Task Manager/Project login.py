from PySimpleGUI import (
    Window, Button, Text, Image, Input, Column, VSeparator, Push, theme, popup, WIN_CLOSED, Checkbox, Frame, pickle
)

# Tema
theme('DarkPurple')

# Criando layout
layout_direita = [[Image(filename='Logo.png')]]

layout_esquerda = [
    [Text('Usiário'), Input(key='-USERNAME-')],
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
        linha = [[Checkbox(''), Input('')]]
        layout = [[Frame('TaskManager', layout=linha, key='container')], [Button(
            'Nova Tarefa'), Button('Resetar Tarefas'), [Button('Salvar Tarefas')]]]
        janela = Window('TaskManager', layout=layout, finalize=True)

        # Loop da janela de login
        while True:
            event, values = janela.read()

            if event == WIN_CLOSED:  # Verifica se o usuário fechou a janela de login
                break

            elif event == 'Nova Tarefa':
                janela.extend_layout(janela['container'], [
                                     [Checkbox(''), Input('')]])

            elif event == 'Resetar Tarefas':
                janela.close()
                janela = Window(
                    'TaskManager', layout=layout_esquerda, finalize=True)
            elif event == 'Salvar Tarefas':
                concluidas = []
                for row in janela['container'].Rows:
                    if row[0].get():
                        concluidas.append(row[1].get())

                with open('tarefas_concluidas.pkl', 'wb') as f:
                    pickle.dump(concluidas, f)

                popup('Tarefas salvas com sucesso!')
