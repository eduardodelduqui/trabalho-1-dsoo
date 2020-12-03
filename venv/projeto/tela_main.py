from limite.tela import Tela
from verifica_valores import VerificaValores
import PySimpleGUI as sg

class TelaMain(Tela):
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    @property
    def verifica_valores(self):
        return self.__verifica_valores

    # def mostra_tela_opcoes(self):
    #     print("-------------- Aplicativo --------------")
    #     print('Entrar como:')
    #     print('\033[1;36m1\033[0m - Cliente')
    #     print('\033[1;36m2\033[0m - Loja')
    #     print('\033[1;36m3\033[0m - Pedido')
    #     print('\033[1;91m0\033[0m - Encerrar')
    #     opcao = self.verifica_valores.inteiros('Escolha a opção: ', list(range(4)))
    #     return opcao

    def mostra_tela_opcoes(self):

        layout = [
            [sg.Button('Cliente', size=(25, 1), pad=(10, 10), font='Helvetica')],
            [sg.Button('Loja', size=(25, 1),pad=(10, 10), font='Helvetica')],
            [sg.Button('Pedido', size=(25, 1),pad=(10, 10), font='Helvetica')],
            [sg.Button('Encerrar', size=(25, 1),pad=(10, 10), font='Helvetica')],
        ]
        sg.theme('LightBlue6')

        window = sg.Window('Aplicativo', element_justification='center',
                           margins=(50, 50)).Layout(layout)

        button, values = window.Read()
        if button == 'Encerrar' or button == None:
            return 0
        if button == 'Cliente':
            window.Close()
            return 1
        if button == 'Loja':
            window.Close()
            return 2
        if button == 'Pedido':
            window.Close()
            return 3
