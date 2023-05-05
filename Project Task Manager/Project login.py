#Importando Biblioteca
from PySimpleGUI import (
    Window, Button, Text, Image, Input, 
    Column, VSeparator, Push, theme, popup, WIN_CLOSED
)

#Tema

theme('DarkPurple')

#Criando Layout

layout_direita = [  [Image(filename='Logo.png')] #Imagem inserid pelo caminho no C:
]

#Criando sistema de Login
layout_esquerda = [

  [Text('E-mail:'), Input(key='-USERNAME-')], 
  [Text('Senha:'), Input(password_char='*', key='-PASSWORD-')],    
  [Push(), Button('Login', key='-LOGIN-'), Button('Esqueci a Senha'), Button('Registre-se'), Push()]

]

layout = [
  [Column(layout_direita), VSeparator(), Column(layout_esquerda)]

]

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
      
    #Definir layout da janela de Registro
      
    register_layout =[
      [Text('Nome:'), Input('')],
      [Text('E-mail:'), Input('')],
      [Text('Senha:'),Input('')],
      [Button('Cadastrar')]
    ]
      
    #Criando Janela de registro
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


    # Verifica se o usuário fechou a janela de login
    if event == WIN_CLOSED:
        break
    
#Adicionando evento ao botão de login
# Verifica se o usuário clicou no botão "Login"
    if event == '-LOGIN-':
      # Obtenha os valores de nome de usuário e senha inseridos
      username = values['-USERNAME-']
      password = values['-PASSWORD-']

      # Verifique se as credenciais estão corretas
      if username == 'usuario' and password == 'senha':
        # Feche a janela de login
        window.close()

        # Abra a janela de tarefas
        import PySimpleGUI as sg
        from PySimpleGUI import (
          Window, Button, Text, Image, Input, Column, VSeparator, Push, theme, popup
            )

        def criar_janela_inicial():
        # código de criação da janela ...

          janela = criar_janela_inicial()

          while True:
            event, values = janela.read()
            if event == sg.WIN_CLOSED:
              break
              if event == 'Adicionar Tarefa':
                janela.extend_layout(janela['container'], [[sg.Checkbox(''), Input('')]] )
              elif event == 'Resetar Tarefas':
                janela.close()
                janela = criar_janela_inicial()
        
      else:
      # Credenciais incorretas, exibir mensagem de erro
        popup('Credenciais incorretas. Por favor, tente novamente.')

    # Verifica se o usuário fechou a janela de login
    if event == WIN_CLOSED:
        break


   
# Encerra o programa
window.close()
