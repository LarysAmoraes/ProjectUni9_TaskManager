#Importando Biblioteca
from PySimpleGUI import (
    Window, Button, Text, Image, Input, 
    Column, VSeparator, Push, theme
)
#Tema
theme('DarkPurple')
#Criando Layout
#Falta colocar a imagem

layout_direita = [
  [Image(filename='Logo.png')]
]

layout_esquerda = [

  [Text('E-mail:'), Input()], 
  [Text('Senha:'), Input(password_char='*')],    
  [Push(), Button('Login'), Push(), Button('Esqueci a Senha'), Push()]

]

layout = [
  [Column(layout_direita), VSeparator(), Column(layout_esquerda)]

]
window = Window(
    'Task Manager',
    layout=layout,
    element_justification='c'
)

window.read()

window.close()
