from prettytable import PrettyTable
from verifica_valores import VerificaValores
import PySimpleGUI as sg


class TelaCliente:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    @property
    def verifica_valores(self):
        return self.__verifica_valores

    def mostra_tela_opcoes(self, clientes):
        if clientes:
            layout = [
                [sg.Button('Adicionar cliente', size=(25, 1), pad=(10, 10), font='Helvetica')],
                [sg.Button('Remover cliente',size=(25, 1), pad=(10, 10), font='Helvetica')],
                [sg.Button('Alterar cliente',size=(25, 1), pad=(10, 10), font='Helvetica')],
                [sg.Button('Listar cliente',size=(25, 1), pad=(10, 10), font='Helvetica')],
                [sg.Button('Voltar',size=(25, 1), pad=(10, 10), font='Helvetica')],
            ]
        else:
            layout = [
                [sg.Button('Adicionar cliente', pad=(10, 10), font='Helvetica')],
                [sg.Button('Voltar', pad=(10, 10), font='Helvetica')],
            ]
        sg.theme('LightBlue6')

        window = sg.Window('Clientes', size=(400, 400), element_justification='center',
                           margins=(50, 50)).Layout(layout)

        button, values = window.Read()
        if button == 'Voltar' or button == None:
            window.close()
            return 0
        if button == 'Adicionar cliente':
            window.close()
            return 1
        if button == 'Remover cliente':
            window.close()
            return 2
        if button == 'Alterar cliente':
            window.close()
            return 3
        if button == 'Listar cliente':
            window.close()
            return 4

    def imprime_lista_cliente(self, clientes):
        if clientes:
            layout = [[sg.Text('Lista de Clientes', size=(70, 1), justification='center')]]

            header = [sg.Text('Nome', size=(30, 1), pad=(1, 1)),
                      sg.Text('CPF', size=(10, 1), pad=(1, 1)),
                      sg.Text('Endereço', size=(25, 1), pad=(1, 1)),
                      sg.Text('Telefone', size=(10, 1), pad=(1, 1))
                      ]

            layout.append(header)

            for cliente in clientes:
                row = [sg.Text(f'{cliente.nome}',background_color='white', size=(30, 1), pad=(1, 1)),
                       sg.Text(cliente.cpf, size=(10, 1), background_color='white', pad=(1, 1)),
                       sg.Text(cliente.endereco, size=(25, 1), background_color='white', pad=(1, 1)),
                       sg.Text(cliente.telefone, size=(10, 1), background_color='white', pad=(1, 1))
                       ]
                layout.append(row)

            window = sg.Window('Lista Clientes').Layout(layout)
            button, values = window.Read()
            window.close()

    def escolhe_cliente(self, clientes):
        if clientes:
            layout = [[sg.Text('Lista de Clientes', size=(70, 1), justification='center')]]

            header = [sg.Text('Nome', size=(30, 1), pad=(1, 1)),
                      sg.Text('CPF', size=(10, 1), pad=(1, 1)),
                      sg.Text('Endereço', size=(25, 1), pad=(1, 1)),
                      sg.Text('Telefone', size=(10, 1), pad=(1, 1))
                      ]

            layout.append(header)

            for cliente in clientes:
                row = [sg.Button(f'{cliente.nome}', button_color=('black', 'white'), border_width=0, size=(30, 1),
                                 pad=(1, 1), key=f'{cliente.cpf}'),
                       sg.Text(cliente.cpf, size=(10, 1), background_color='white', pad=(1, 1)),
                       sg.Text(cliente.endereco, size=(25, 1), background_color='white', pad=(1, 1)),
                       sg.Text(cliente.telefone, size=(10, 1), background_color='white', pad=(1, 1))
                       ]
                layout.append(row)

            window = sg.Window('Lista Clientes').Layout(layout)
            button, values = window.Read()
            window.close()
            if button is None:
                return 0
            return int(str(button))

    def opcoes_adicionar(self, clientes):
        layout = [
            [sg.Text('Adicionar Cliente')],
            [sg.Text('Nome:', size=(8, 1), pad=(5, 5)), sg.InputText(key='nome')],
            [sg.Text('CPF:', size=(8, 1), pad=(5, 5)), sg.InputText(key='cpf', enable_events=True)],
            [sg.Text('CPF inválido, insira um valor válido', pad=(5, 1), text_color='red', visible=False,
                     key='cpf_validation_1')],
            [sg.Text('CPF já existente, insira outro CPF', pad=(5, 1), text_color='red', visible=False,
                     key='cpf_validation_2')],
            [sg.Text('Endereço:', size=(8, 1), pad=(5, 5)), sg.InputText(key='endereco')],
            [sg.Text('Telefone:', size=(8, 1), pad=(5, 5)), sg.InputText(key='telefone', enable_events=True)],
            [sg.Text('Telefone inválido, insira um valor válido', pad=(5, 1), text_color='red', visible=False,
                     key='telefone_validation_1')],
            [sg.Text('Telefone já existente, insira outro telefone', pad=(5, 1), text_color='red', visible=False,
                     key='telefone_validation_2')],
            [sg.Submit('Adicionar'), sg.Cancel('Voltar')]
        ]

        sg.theme('LightBlue6')
        window = sg.Window('Adicionar Cliente').Layout(layout)
        while True:
            form_valido = []
            event, values = window.Read()
            if event == 'cpf' and values['cpf'] and values['cpf'][-1] not in ('0123456789'):
                window['cpf'].update(values['cpf'][:-1])
            if event == 'telefone' and values['telefone'] and values['telefone'][-1] not in ('0123456789'):
                window['telefone'].update(values['telefone'][:-1])
            if event in (sg.WIN_CLOSED, 'Voltar'):
                window.close()
                return 0
            if event in ('Adicionar'):
                if not self.verifica_valores.telefone(values['telefone']):
                    window['telefone_validation_1'].update(visible=True)
                    form_valido.append(False)
                else: window['telefone_validation_1'].update(visible=False)
                if not self.verifica_valores.verifica_telefone(int(values['telefone']), clientes):
                    window['telefone_validation_2'].update(visible=True)
                    form_valido.append(False)
                else: window['telefone_validation_2'].update(visible=False)
                if not self.verifica_valores.cpf(values['cpf']):
                    window['cpf_validation_1'].update(visible=True)
                    form_valido.append(False)
                else: window['cpf_validation_1'].update(visible=False)
                if not self.verifica_valores.verifica_cpf(int(values['cpf']), clientes):
                    window['cpf_validation_2'].update(visible=True)
                    form_valido.append(False)
                else: window['cpf_validation_2'].update(visible=False)
                if not form_valido:
                    window.close()
                    return {
                        'nome': str(values['nome']),
                        'cpf': int(values['cpf']),
                        'endereco': str(values['endereco']),
                        'telefone': int(values['telefone'])
                    }


    def tela_alterar_opcoes(self, cliente, clientes):
        layout = [
            [sg.Text('Alterar Cliente')],
            [sg.Text('Nome:', size=(8, 1), pad=(5, 5)), sg.InputText(cliente.nome, key='nome')],
            [sg.Text('CPF:', size=(8, 1), pad=(5, 5)), sg.InputText(cliente.cpf, key='cpf', enable_events=True)],
            [sg.Text('CPF inválido, insira um valor válido', pad=(5, 1), text_color='red', visible=False,
                     key='cpf_validation_1')],
            [sg.Text('CPF já existente, insira outro CPF', pad=(5, 1), text_color='red', visible=False,
                     key='cpf_validation_2')],
            [sg.Text('Endereço:', size=(8, 1), pad=(5, 5)), sg.InputText(cliente.endereco, key='endereco')],
            [sg.Text('Telefone:', size=(8, 1), pad=(5, 5)), sg.InputText(cliente.telefone, key='telefone', enable_events=True)],
            [sg.Text('Telefone inválido, insira um valor válido', pad=(5, 1), text_color='red', visible=False,
                     key='telefone_validation_1')],
            [sg.Text('Telefone já existente, insira outro telefone', pad=(5, 1), text_color='red', visible=False,
                     key='telefone_validation_2')],
            [sg.Submit('Alterar'), sg.Cancel('Voltar')]
        ]

        window = sg.Window('Alterar Cliente').Layout(layout)
        while True:
            form_valido = []
            event, values = window.Read()
            if event == 'cpf' and values['cpf'] and values['cpf'][-1] not in ('0123456789'):
                window['cpf'].update(values['cpf'][:-1])
            if event == 'telefone' and values['telefone'] and values['telefone'][-1] not in ('0123456789'):
                window['telefone'].update(values['telefone'][:-1])
            if event in (sg.WIN_CLOSED, 'Voltar'):
                window.close()
                return 0
            if event in ('Alterar'):
                if not self.verifica_valores.telefone(values['telefone']):
                    window['telefone_validation_1'].update(visible=True)
                    form_valido.append(False)
                else:
                    window['telefone_validation_1'].update(visible=False)
                if not self.verifica_valores.verifica_telefone(int(values['telefone']), clientes, cliente.telefone):
                    window['telefone_validation_2'].update(visible=True)
                    form_valido.append(False)
                else:
                    window['telefone_validation_2'].update(visible=False)
                if not self.verifica_valores.cpf(values['cpf']):
                    window['cpf_validation_1'].update(visible=True)
                    form_valido.append(False)
                else:
                    window['cpf_validation_1'].update(visible=False)
                if not self.verifica_valores.verifica_cpf(int(values['cpf']), clientes, cliente.cpf):
                    window['cpf_validation_2'].update(visible=True)
                    form_valido.append(False)
                else:
                    window['cpf_validation_2'].update(visible=False)
                if not form_valido:
                    window.close()
                    return {
                        'nome': str(values['nome']),
                        'cpf': int(values['cpf']),
                        'endereco': str(values['endereco']),
                        'telefone': int(values['telefone'])
                    }

    def tela_confirma(self):
        layout = [
            [sg.Text('Confirmar Operação?')],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('').Layout(layout)
        button, values = window.Read()
        if button == 'Confirmar':
            window.close()
            return True
        else:
            window.close()
            return False