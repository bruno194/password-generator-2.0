import PySimpleGUI as sg
import random


sg.theme('Purple')
def principal():
    estilo = [
        [sg.Text('site/programa'), sg.Input(key='sp')],
        [sg.Text('quantidade de caracteres '), sg.Combo(values=list(range(1, 20)),key='caracteres',default_value=1,size=(4,1))],
        [sg.Button('gerar senha'),sg.Button('salvar senha gerada')],
        [sg.Output(size=(30,10), key='converter')],
        [sg.Button('sair'),sg.Text('feito pro bruno dos santos')]
    ]
    janela = sg.Window('-GERADOR DE SENHA-').layout(estilo)
    while True:
        evento, valores = janela.read()
        site = valores['sp']
        a = ['a','B','b','A','C','c','d','D','#','@','#','$','%','¨','&','*','(','1','2','3','4','5','6','7','8','9','e','f','E','F','G','H','I','g','h','i']
        computador = random.choices(a, k=int(valores['caracteres']))
        novo = ' '.join(computador)
        if evento == sg.WINDOW_CLOSED or evento == 'sair':
            break
        if evento == 'gerar senha':
            janela['converter'].update(f'senha para {site} = {novo}')
        if evento == 'salvar senha gerada':
            with open('senha.txt', 'a', newline='') as arquivo:
                arquivo.write(f'site/software é {site} nova senha = {novo}')
            print('arquivo salvo')

principal()