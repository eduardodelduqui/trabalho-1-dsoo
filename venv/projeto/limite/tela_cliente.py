from prettytable import PrettyTable
from verifica_valores import VerificaValores


class TelaCliente:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    def cria_lista_id(self, clientes: list):
        lista_id = []
        for cliente in clientes:
            lista_id.append(cliente.id)
        return lista_id

    def mostra_tela_opcoes(self, clientes):
        print("-------------- Cliente --------------")
        print('\033[1;36m1\033[0m - Adicionar cliente')
        if clientes:
            print('\033[1;36m2\033[0m - Remover cliente')
            print('\033[1;36m3\033[0m - Alterar cliente')
            print('\033[1;36m4\033[0m - Listar clientes')
            print('\033[1;36m0\033[0m - Voltar')
            opcao = self.__verifica_valores.inteiros('Escolha a opção: ', list(range(5)))
        else:
            print('\033[1;36m0\033[0m - Voltar')
            opcao = self.__verifica_valores.inteiros('Escolha a opção: ', list(range(2)))
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
        nome = self.__verifica_valores.texto('Digite o nome do cliente: ')
        cpf = self.__verifica_valores.cpf('Alterar CPF para: ')
        endereco = self.__verifica_valores.texto('Digite o endereço: ')

        cliente = {
            "nome": nome,
            "cpf": cpf,
            "endereco": endereco
        }
        return cliente

    def tela_remover(self):
        return self.__verifica_valores.cpf('Digite o cpf do cliente a ser removido [0 para voltar]: ')

    def tela_alterar_opcoes(self):
        print('------ Alterar ------')
        print('1 - Nome')
        print('2 - CPF')
        print('3 - Endereço')
        print('0 - Voltar')
        opcao = self.__verifica_valores.inteiros('Digite a opção que deseja alterar: ', list(range(4)))
        return opcao

    def tela_alterar_para(self, nome: bool = False, cpf: bool = False):
        if(nome):
            return self.__verifica_valores.texto('Alterar nome para: ')
        if(cpf):
            return self.__verifica_valores.cpf('Alterar CPF para: ')

    def escolhe_cliente(self, clientes):
        id_clientes = self.cria_lista_id(clientes)
        return self.__verifica_valoress.inteiros("Insira o ID do cliente [0 para voltar]: ", id_clientes, "Valor inválido, insira um ID válido")






