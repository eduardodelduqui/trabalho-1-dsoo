from prettytable import PrettyTable
import os


class TelaCliente:
    def __init__(self):
        pass

    def verifica_numero_inteiro(self, mensagem: str = "", valores_validos: [] = None):
        while True:
            try:
                opcao = int(input('Escolha a Opção: '))
                if (opcao in valores_validos):
                    return opcao
                else:
                    print('Valor inválido, insira o número ao lado da opção desejada')
            except ValueError:
                print('Valor inválido, valor precisa ser inteiro')

    def mostra_tela_opcoes(self):
        print("-------------- Cliente --------------")
        print('\033[1;36m1\033[0m - Adicionar cliente')
        print('\033[1;36m2\033[0m - Remover cliente')
        print('\033[1;36m3\033[0m - Alterar cliente')
        print('\033[1;36m4\033[0m - Listar clientes')
        print('\033[1;36m0\033[0m - Voltar')
        opcao = self.verifica_numero_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4])
        return opcao

    def imprime_lista_cliente(self, clientes):
        if clientes:
            print('----------- Clientes -----------')
            t = PrettyTable(['ID', 'Nome', 'CPF'])
            for cliente in clientes:
                t.add_row([cliente.id, cliente.nome, cliente.cpf])
            print(t)
        else:
            print('\033[1;31m!!! Lista de clientes vazia !!!\033[0m')


    def opcoes_adicionar(self):
        nome = input('Digite o nome do cliente: ')
        cpf = input('Digite o cpf do cliente: ')
        endereco = input('Digite o endereço: ')

        cliente = {
            "nome": nome,
            "cpf": cpf,
            "endereco": endereco
        }
        return cliente

    def tela_remover(self):
        return input('Digite o cpf do cliente a ser removido: ')

    def tela_alterar(self):
        id = int(input('Digite o ID do cliente a ser alterado: '))
        print('------ Alterar ------')
        print('1 - Nome')
        print('2 - CPF')
        print('3 - Endereço')
        print('0 - Voltar')
        opcao = int(input('Digite a opção que deseja alterar: '))
        valor = input('Alterar para: ')
        return {
            "id": id,
            "opcao": opcao,
            "valor": valor
        }

    def escolhe_cliente(self, clientes):
        id_clientes = self.pega_id_lista(clientes)
        return self.verifica_numero_inteiro("Escolha o cliente: ", id_clientes)






