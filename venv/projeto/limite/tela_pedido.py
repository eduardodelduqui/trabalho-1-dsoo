from prettytable import PrettyTable
from verifica_valores import VerificaValores
import PySimpleGUI as sg

class TelaPedido:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    @property
    def verifica_valores(self):
        return self.__verifica_valores

    def pega_id_lista(self, pratos: list):
        lista = []
        for prato in pratos:
            lista.append(prato.id)
        return lista

    def imprime_pedido(self, pedido):
        if pedido:
            pratos = pedido.pratos
            t_pratos = PrettyTable(['ID', 'prato', 'Qtd.', 'Preço unitário' ], border=False)
            for prato in pratos:
                qtd = prato["qtd"]
                prato = prato["item"]
                t_pratos.add_row([prato.id, prato.nome, qtd, f'{prato.preco_unitario:.2f}'])
            tabela = PrettyTable(['NOTA FISCAL'])
            t_cod = PrettyTable(['COD. '], border=False, header=False)
            t_cod.add_row(['COD. '+pedido.id])
            t_header = PrettyTable(['DATA', 'HORARIO'], border=False, header=False)
            t_header.add_row(['DATA: '+str(pedido.data), 'HORARIO: '+pedido.horario])
            tabela.add_row([t_cod])
            tabela.add_row([t_header])
            if pedido.cliente:
                cliente = pedido.cliente
                t_cliente = PrettyTable(['ID', 'Nome', 'CPF'], border=False)
                cliente_cpf = self.verifica_valores.cpf_tratado(cliente.cpf)
                t_cliente.add_row([cliente.id, cliente.nome, cliente_cpf])
                tabela.add_row(['----------- Cliente -----------'])
                tabela.add_row([t_cliente])
            else:
                tabela.add_row(['Cliente não cadastrado'])
            tabela.add_row(['------------ Itens ------------'])
            tabela.add_row([t_pratos])
            tabela.add_row(['-------------------------------'])
            t_footer = PrettyTable(['VALOR TOTAL', 'PAGO'], header=False, border=False)
            if pedido.pago:
                pago = 'PAGO'
            else: pago = 'A PAGAR'
            t_footer.add_row(['Valor total: R$ '+f'{pedido.valor_total:.2f}', pago])
            tabela.add_row([t_footer])
            print(tabela)
        else:
            print('LISTA VAZIA')

    # def mostra_tela_opcoes(self):
    #     print("------- Pedido -------")
    #     print("\033[1;36m1\033[0m - Efetuar pedido")
    #     print("\033[1;36m2\033[0m - Histórico de pedidos")
    #     print("\033[1;91m0\033[0m - Voltar")
    #     return self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))

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

    def mostra_tela_historico(self):
        print("------ Histórico ------")
        print("\033[1;36m1\033[0m - Desde o início")
        print("\033[1;36m2\033[0m - Últimos")
        print("\033[1;91m0\033[0m - Voltar")
        return self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))

    def mostra_tela_opcoes_cliente(self, clientes):
        print("------ Adicionar Cliente ------")
        print("\033[1;36m1\033[0m - Não adicionar cliente")
        print("\033[1;36m2\033[0m - Cliente não cadastrado")
        if clientes:
            print("\033[1;36m3\033[0m - Cliente cadastrado")
        print("\033[1;91m0\033[0m - Cancelar compra")
        if clientes: return self.verifica_valores.inteiros("Escolha a opção: ", list(range(4)))
        else: return self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))

    def confirma_pedido(self):
        print("------ Confirmar Pedido ------")
        print("\033[1;36m1\033[0m - Confirmar")
        print("\033[1;36m2\033[0m - Alterar pedido")
        print("\033[1;36m3\033[0m - Cancelar pedido")
        print("\033[1;91m0\033[0m - Voltar")
        return self.__verifica_valores.inteiros("Escolha a opçao: ", list(range(4)))

    # def escolhe_prato(self, pratos):
    #     lista_compras = []
    #     id_pratos = self.pega_id_lista(pratos)
    #     while True:
    #         id = input("Escolha o prato: ")
    #         qtd = self.__verifica_valores.inteiros("Escolha a quantidade: ", list(range(99)), 'Valor inválido, não é possível comprar mais de 100 itens')
    #         if qtd != 0:
    #             compra = {"id": id, "qtd": qtd}
    #             lista_compras.append(compra)
    #         if self.__verifica_valores.sim_ou_nao("Deseja continuar a compra? [S/N]", ) == "n":
    #             return lista_compras

    def escolhe_prato(self, pratos):
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

        window = sg.Window('Lista Clientes').Layout(layout)
        button, values = window.Read()
        if button is None:
            window.close()
            return 0
        else:
            quantidade = self.escolhe_quantidade()

        return {
            'item': button,
            'quantidade': quantidade
        }

    def escolhe_quantidade(self):
        layout = [
            [sg.Text('Escolha a quantidade')],
            [sg.Text('Quantidade:', size=(10, 1)), sg.Input(key='quantidade' ,size=(3,1))],
            [sg.Submit('Confirmar'), sg.Cancel('Cancelar')]
        ]

        window = sg.Window('').Layout(layout)
        button, values = window.Read()
        if button == 'Confirmar':
            return int(values['quantidade'])
        else:
            window.close()

    def escolhe_cliente(self, clientes):
        id_clientes = self.pega_id_lista(clientes)
        return self.__verifica_valores.inteiros("Escolha o cliente: ", id_clientes)


