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
                [sg.Button('Buscar cliente',size=(25, 1), pad=(10, 10), font='Helvetica')],
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
        if button == 'Buscar cliente':
            window.close()
            return 4
        if button == 'Listar cliente':
            window.close()
            return 5

    # def mostra_tela_opcoes(self, clientes):
    #     print("-------------- Cliente --------------")
    #     print('\033[1;36m1\033[0m - Adicionar cliente')
    #     if clientes:
    #         print('\033[1;36m2\033[0m - Remover cliente')
    #         print('\033[1;36m3\033[0m - Alterar cliente')
    #         print('\033[1;36m4\033[0m - Buscar cliente')
    #         print('\033[1;36m5\033[0m - Listar clientes')
    #         print('\033[1;36m0\033[0m - Voltar')
    #         opcao = self.verifica_valores.inteiros('Escolha a opção: ', list(range(6)))
    #     else:
    #         print('\033[1;36m0\033[0m - Voltar')
    #         opcao = self.verifica_valores.inteiros('Escolha a opção: ', list(range(2)))
    #     return opcao

    # def imprime_lista_cliente(self, clientes):
    #     if clientes:
    #         print('----------- Clientes -----------')
    #         t = PrettyTable(['ID', 'Nome', 'CPF'])
    #         for cliente in clientes:
    #             cliente_cpf = self.verifica_valores.cpf_tratado(cliente.cpf)
    #             t.add_row([cliente.id, cliente.nome, cliente_cpf])
    #         print(t)
    #     else:
    #         print('\033[1;31m!!! Lista de clientes vazia !!!\033[0m')

    def imprime_lista_cliente(self, clientes):
        if clientes:
            layout = [[sg.Text('Lista de Clientes', size=(70, 1), justification='center')]]

            header = [sg.Text('Nome', size=(25, 1), pad=(1, 1)),
                      sg.Text('CPF', size=(10, 1), pad=(1, 1)),
                      sg.Text('Endereço', size=(25, 1), pad=(1, 1)),
                      sg.Text('Telefone', size=(10, 1), pad=(1, 1))
                      ]

            layout.append(header)

            for cliente in clientes:
                row = [sg.Button(f'{cliente.nome}', button_color=('black', 'white'), border_width=0, size=(30, 1), pad=(1, 1), key=f'{cliente.cpf}'),
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

            header = [sg.Text('Nome', size=(25, 1), pad=(1, 1)),
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


    # def imprime_cliente(self, cliente):
    #     print('----------- Clientes -----------')
    #     t = PrettyTable(['ID', 'Nome', 'CPF', 'Telefone', 'Endereço'])
    #     cliente_cpf = self.verifica_valores.cpf_tratado(cliente.cpf)
    #     cliente_telefone = self.verifica_valores.telefone_tratado(cliente.telefone)
    #     t.add_row([cliente.id, cliente.nome, cliente_cpf, cliente_telefone, cliente.endereco])
    #     print(t)

    # def opcoes_adicionar(self, clientes):
    #     nome = self.verifica_valores.texto('Digite o nome do cliente: ')
    #     cpf = self.verifica_valores.cpf('Alterar CPF para: ', clientes)
    #     endereco = self.verifica_valores.texto('Digite o endereço: ')
    #     telefone = self.verifica_valores.telefone('Digite o telefone (com DDD): ')
    #
    #     cliente = {
    #         "nome": nome,
    #         "cpf": cpf,
    #         "endereco": endereco,
    #         "telefone": telefone
    #     }
    #     return cliente

    def opcoes_adicionar(self, clientes):
        layout = [
            [sg.Text('Adicionar Cliente')],
            [sg.Text('Nome:', size=(8, 1), pad=(5, 5)), sg.InputText(key='nome')],
            [sg.Text('CPF:', size=(8, 1), pad=(5, 5)), sg.InputText(key='cpf')],
            [sg.Text('Endereço:', size=(8, 1), pad=(5, 5)), sg.InputText(key='endereco')],
            [sg.Text('Telefone:', size=(8, 1), pad=(5, 5)), sg.InputText(key='telefone')],
            [sg.Submit('Adicionar'), sg.Cancel('Voltar')]
        ]
        sg.theme('LightBlue6')
        window = sg.Window('Adicionar Cliente').Layout(layout)
        button, values = window.Read()
        if button == 'Voltar' or button is None:
            window.close()
            return 0
        else:
            if self.tela_confirma():
                window.close()
                return {
                    'nome': values['nome'],
                    'cpf': int(values['cpf']),
                    'endereco': values['endereco'],
                    'telefone': values['telefone']
                }

    # def tela_remover(self):
    #     return self.verifica_valores.cpf('Digite o cpf do cliente a ser removido [0 para voltar]: ')

    # def tela_alterar_opcoes(self):
    #     print('------ Alterar ------')
    #     print('1 - Nome')
    #     print('2 - CPF')
    #     print('3 - Endereço')
    #     print('4 - Telefone')
    #     print('0 - Voltar')
    #     opcao = self.verifica_valores.inteiros('Digite a opção que deseja alterar: ', list(range(4)))
    #     return opcao

    def tela_alterar_opcoes(self, cliente):
        layout = [
            [sg.Text('Alterar Cliente')],
            [sg.Text('Nome:', size=(8, 1), pad=(5, 5)), sg.InputText(cliente.nome, key='nome')],
            [sg.Text('CPF:', size=(8, 1), pad=(5, 5)), sg.InputText(cliente.cpf, key='cpf')],
            [sg.Text('Endereço:', size=(8, 1), pad=(5, 5)), sg.InputText(cliente.endereco, key='endereco')],
            [sg.Text('Telefone:', size=(8, 1), pad=(5, 5)), sg.InputText(cliente.telefone, key='telefone')],
            [sg.Submit('Alterar'), sg.Cancel('Voltar')]
        ]

        window = sg.Window('Alterar Cliente').Layout(layout)
        button, values = window.Read()
        return {
            'nome': values['nome'],
            'cpf': int(values['cpf']),
            'endereco': values['endereco'],
            'telefone': values['telefone']
        }


    # def tela_alterar_para(self, nome: bool = False, cpf: bool = False, endereco: bool = False, telefone: bool = False):
    #     if(nome):
    #         return self.verifica_valores.texto('Alterar nome para: ')
    #     if(cpf):
    #         return self.verifica_valores.cpf('Alterar CPF para: ')
    #     if(endereco):
    #         return self.verifica_valores.texto('Alterar endereço para: ')
    #     if(telefone):
    #         return self.verifica_valores.telefone('Alterar telefone para: ')

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

    # def escolhe_cliente(self, clientes):
    #     id_clientes = self.cria_lista_id(clientes)
    #     return self.verifica_valores.inteiros("Insira o ID do cliente [0 para voltar]: ", id_clientes, "Valor inválido, insira um ID válido")


    def adicionado_com_sucesso(self):
        print('\033[1;36mCLIENTE ADICIONADO COM SUCESSO\033[0m')





