from prettytable import PrettyTable
from verifica_valores import VerificaValores
import PySimpleGUI as sg

class TelaPedido:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    @property
    def verifica_valores(self):
        return self.__verifica_valores

    def confirma_pedido(self, pedido):
        pratos = pedido. pratos
        layout = [
            [sg.Text('Pedido', size= (43, 1), pad=(4, 4), font='Helvetica', justification='center')],
            [sg.Text(f'COD. {pedido.id}')],
            [sg.Text(f'DATA: {str(pedido.data)}'), sg.Text(f'HORARIO: {pedido.horario}')]
        ]

        if pedido.cliente:
            layout.append([sg.Text(f'Cliente: {pedido.cliente.nome}', justification='center')])
            layout.append([sg.Text(f'{pedido.cliente.cpf}')])
        else:
            layout.append([sg.Text(f'Cliente não cadastrado', justification='center')])

        layout.append([sg.Text(f"{30*'-'} Itens {30*'-'}", size=(40, 1), justification='center')])

        header = [sg.Text('Prato', size=(15, 1), pad=(1, 1), justification='center'),
                  sg.Text('Qtd.', size=(10, 1), pad=(1, 1), justification='center'),
                  sg.Text('Valor UN.', size=(8, 1), pad=(1, 1), justification='center'),
                  sg.Text('Total item', size=(10, 1), pad=(1, 1), justification='center'),
                  ]
        layout.append(header)

        for prato in pratos:
            qtd = prato["qtd"]
            item = prato["item"]
            if qtd != 0:
                prato_row = [
                    sg.Text(f'{item.nome}', size=(15, 1), pad=(1, 1), justification='center'),
                    sg.Text(f'{qtd}', size=(10, 1), pad=(1, 1), justification='center'),
                    sg.Text(f'{item.preco_unitario:.2f}', size=(8, 1), pad=(1, 1), justification='center'),
                    sg.Text(f'{item.preco_unitario*qtd:.2f}', size=(10, 1), pad=(1, 1), justification='center')
                ]
                layout.append(prato_row)
        layout.append([sg.Text(f'Valor total: R$ {pedido.valor_total:.2f}')])
        layout.append([sg.Submit('Confirmar'), sg.Cancel('Cancelar'), sg.Button('Alterar pedido')])


        window = sg.Window('Clientes', element_justification='center',
                           margins=(50, 50)).Layout(layout)
        button, values = window.Read()

        if button == 'Confirmar':
            window.close()
            return 1
        if button == 'Alterar pedido':
            window.close()
            return 2
        if button == 'Cancelar':
            window.close()
            return 3
        if button == None:
            window.close()
            return 0

    def mostra_tela_opcoes(self):
        layout = [
            [sg.Button('Efetuar pedido', size=(25, 1), pad=(10, 10), font='Helvetica')],
            [sg.Button('Histórico de pedidos',size=(25, 1), pad=(10, 10), font='Helvetica')],
            [sg.Button('Voltar',size=(25, 1), pad=(10, 10), font='Helvetica')],
        ]

        sg.theme('LightBlue6')

        window = sg.Window('Clientes', size=(400, 400), element_justification='center',
                           margins=(50, 50)).Layout(layout)

        button, values = window.Read()
        if button == 'Voltar' or button == None:
            window.close()
            return 0
        if button == 'Efetuar pedido':
            window.close()
            return 1
        if button == 'Histórico de pedidos':
            window.close()
            return 2

    def lista_historico_pedido(self, pedidos):
        header = [
            sg.Text('ID', size=(6, 1), pad=(1, 1)), sg.Text('Nome', size=(30, 1), pad=(1, 1)),
            sg.Text('Data', size=(8, 1), pad=(1, 1)), sg.Text('Horário', size=(8, 1), pad=(1, 1)),
            sg.Text('Valor (R$)', size=(8, 1), pad=(1, 1))
        ]
        layout = []
        layout.append(header)
        for pedido in pedidos:
            if pedido.cliente:
                row = [sg.Text(f'{pedido.id}', background_color='white', size=(6, 1),
                                 pad=(1, 1)),
                       sg.Button(pedido.cliente.nome, size=(30, 1), button_color=('black', 'white'), border_width=0, pad=(1, 1), key=f'{pedido.id}'),
                       sg.Text(pedido.data, size=(8, 1), background_color='white', pad=(1, 1)),
                       sg.Text(pedido.horario, size=(8, 1), background_color='white', pad=(1, 1)),
                       sg.Text(f'{pedido.valor_total:.2f}', size=(8, 1), background_color='white', pad=(1, 1), justification='center')
                       ]
            else:
                row = [sg.Text(f'{pedido.id}', background_color='white', size=(6, 1),
                                 pad=(1, 1)),
                       sg.Button('Cliente não cadastrado', size=(30, 1), button_color=('black', 'white'), border_width=0, pad=(1, 1), key=f'{pedido.id}'),
                       sg.Text(pedido.data, size=(8, 1), background_color='white', pad=(1, 1)),
                       sg.Text(pedido.horario, size=(8, 1), background_color='white', pad=(1, 1)),
                       sg.Text(f'{pedido.valor_total:.2f}', size=(8, 1), background_color='white', pad=(1, 1), justification='center')
                       ]
            layout.append(row)

        window = sg.Window('Clientes', size=(640, 600), element_justification='center',
                           margins=(50, 50)).Layout([[sg.Column(layout, size=(610, 400), scrollable=True)],[sg.Button('Voltar')]])
        button, values = window.Read()

        if button == 'Voltar' or button == None:
            window.close()
            return 0
        else:
            window.close()
            return str(button)

    def imprime_pedido(self, pedido):
        pratos = pedido.pratos
        layout = [
            [sg.Text('Pedido', size=(43, 1), pad=(4, 4), font='Helvetica', justification='center')],
            [sg.Text(f'COD. {pedido.id}')],
            [sg.Text(f'DATA: {str(pedido.data)}'), sg.Text(f'HORARIO: {pedido.horario}')]
        ]

        if pedido.cliente:
            layout.append([sg.Text(f'Cliente: {pedido.cliente.nome}', justification='center')])
            layout.append([sg.Text(f'{pedido.cliente.cpf}')])
        else:
            layout.append([sg.Text(f'Cliente não cadastrado', justification='center')])

        layout.append([sg.Text(f"{40*'-'} Itens {40*'-'}", size=(40, 1), justification='center')])

        header = [sg.Text('Prato', size=(15, 1), pad=(1, 1), justification='center'),
                  sg.Text('Qtd.', size=(10, 1), pad=(1, 1), justification='center'),
                  sg.Text('Valor UN.', size=(8, 1), pad=(1, 1), justification='center'),
                  sg.Text('Total item', size=(10, 1), pad=(1, 1), justification='center'),
                  ]
        layout.append(header)

        for prato in pratos:
            qtd = prato["qtd"]
            item = prato["item"]
            if qtd != 0:
                prato_row = [
                    sg.Text(f'{item.nome}', size=(15, 1), pad=(1, 1), justification='center'),
                    sg.Text(f'{qtd}', size=(10, 1), pad=(1, 1), justification='center'),
                    sg.Text(f'{item.preco_unitario:.2f}', size=(8, 1), pad=(1, 1), justification='center'),
                    sg.Text(f'{item.preco_unitario * qtd:.2f}', size=(10, 1), pad=(1, 1), justification='center')
                ]
                layout.append(prato_row)
        layout.append([sg.Text(f'Valor total: R$ {pedido.valor_total:.2f}')])
        layout.append([sg.Button('Voltar')])

        window = sg.Window('Clientes', element_justification='center',
                           margins=(50, 50)).Layout(layout)
        button, values = window.Read()

        if button == 'Voltar' or button == None:
            window.close()
            return 0

    def mostra_tela_opcoes_cliente(self, clientes):
        layout = [
            [sg.Button('Não adicionar cliente', size=(25, 1), pad=(10, 10), font='Helvetica')],
            [sg.Button('Cliente não cadastrado', size=(25, 1), pad=(10, 10), font='Helvetica')],
        ]
        if clientes:
            layout.append([sg.Button('Cliente cadastrado', size=(25, 1), pad=(10, 10), font='Helvetica')])

        layout.append([sg.Button('Revisar compra', size=(25, 1), pad=(10, 10), font='Helvetica')])
        layout.append([sg.Button('Cancelar compra', size=(25, 1), pad=(10, 10), font='Helvetica')])

        window = sg.Window('Clientes', size=(400, 400), element_justification='center',
                           margins=(50, 50)).Layout(layout)

        button, values = window.Read()

        if button == 'Não adicionar cliente':
            window.close()
            return 1
        if button == 'Cliente não cadastrado':
            window.close()
            return 2
        if button == 'Cliente cadastrado':
            window.close()
            return 3
        if button == 'Revisar compra':
            window.close()
            return 4
        if button == 'Cancelar compra' or button == None:
            window.close()
            return 0

    def escolhe_prato(self, pratos, lista_compras):
        total_compra = 0
        layout = [[sg.Text('Escolha o Prato', size=(30, 1), justification='center')]]

        header = [sg.Text('Nome', size=(15, 1), pad=(1, 1)),
                  sg.Text('Categoria', size=(10, 1), pad=(1, 1)),
                  sg.Text('Preço', size=(5, 1), pad=(1, 1)),
                  ]

        layout.append(header)

        for prato in pratos:
            row = [sg.Button(f'{prato.nome}', button_color=('black', 'white'), border_width=0, size=(15, 1),
                             pad=(1, 1), key=f'{prato.id}'),
                   sg.Text(prato.tipo.nome, size=(10, 1), background_color='white', pad=(1, 1)),
                   sg.Text(prato.preco_unitario, size=(5, 1), background_color='white', pad=(1, 1)),
                   ]
            layout.append(row)

        for index, prato in enumerate(lista_compras):
            if prato["qtd"] != 0:
                total_compra += prato['valor_total']
                row = [
                       sg.Text(prato["nome"], size=(15, 1), background_color='lightblue', pad=(1, 1)),
                       sg.Text(prato["qtd"], size=(5, 1), background_color='lightblue', pad=(1, 1)),
                        sg.Text(f"R$ {prato['valor_total']:.2f}", size=(10, 1), background_color='lightblue', pad=(1, 1)),
                       ]
                layout.append(row)

        if lista_compras:
            window = sg.Window('Lista Pratos', size=(320, 400)).Layout(
                [[sg.Column(layout, size=(300, 300), scrollable=True)],
                 [sg.Text('Total compra:'), sg.Text(f'R$ {total_compra:.2f}')],
                 [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]])
        else:
            window = sg.Window('Lista Pratos', size=(320, 400)).Layout(
                [[sg.Column(layout, size=(300, 300), scrollable=True)],
                 [sg.Submit('Confirmar', disabled=True), sg.Cancel('Cancelar')]])

        button, values = window.Read()
        if button is None or button == 'Cancelar':
            window.close()
            return 0
        if button == 'Confirmar':
            window.close()
            return 1
        else:
            quantidade = self.escolhe_quantidade()
            window.close()
            if quantidade != 0:
                return {
                    'id': button,
                    'qtd': quantidade
                }
            else:
                return {
                    'id': button,
                    'qtd': 0
                }

    def escolhe_quantidade(self):
        layout = [
            [sg.Text('Escolha a quantidade')],
            [sg.Text('Quantidade:', size=(10, 1)), sg.Input(key='quantidade' ,size=(3,1), enable_events=True)],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('').Layout(layout)
        while True:
            event, values = window.Read()
            if event == 'quantidade' and values['quantidade'] and values['quantidade'][-1] not in ('0123456789'):
                window['quantidade'].update(values['quantidade'][:-1])
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return 0
            if event in ('Confirmar'):
                window.close()
                return int(values['quantidade'])




