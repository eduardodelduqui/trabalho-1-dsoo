from prettytable import PrettyTable
from verifica_valores import VerificaValores


class TelaCliente:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    @property
    def verifica_valores(self):
        return self.__verifica_valores

    def cria_lista_id(self, clientes: list):
        lista_id = [0]
        for cliente in clientes:
            lista_id.append(cliente.id)
        return lista_id

    def mostra_tela_opcoes(self, clientes):
        print("-------------- Cliente --------------")
        print('\033[1;36m1\033[0m - Adicionar cliente')
        if clientes:
            print('\033[1;36m2\033[0m - Remover cliente')
            print('\033[1;36m3\033[0m - Alterar cliente')
            print('\033[1;36m4\033[0m - Buscar cliente')
            print('\033[1;36m5\033[0m - Listar clientes')
            print('\033[1;36m0\033[0m - Voltar')
            opcao = self.verifica_valores.inteiros('Escolha a opção: ', list(range(6)))
        else:
            print('\033[1;36m0\033[0m - Voltar')
            opcao = self.verifica_valores.inteiros('Escolha a opção: ', list(range(2)))
        return opcao

    def imprime_lista_cliente(self, clientes):
        if clientes:
            print('----------- Clientes -----------')
            t = PrettyTable(['ID', 'Nome', 'CPF'])
            for cliente in clientes:
                cliente_cpf = self.verifica_valores.cpf_tratado(cliente.cpf)
                t.add_row([cliente.id, cliente.nome, cliente_cpf])
            print(t)
        else:
            print('\033[1;31m!!! Lista de clientes vazia !!!\033[0m')

    def imprime_cliente(self, cliente):
        print('----------- Clientes -----------')
        t = PrettyTable(['ID', 'Nome', 'CPF', 'Telefone', 'Endereço'])
        cliente_cpf = self.verifica_valores.cpf_tratado(cliente.cpf)
        t.add_row([cliente.id, cliente.nome, cliente_cpf, cliente.telefone, cliente.endereco])
        print(t)

    def opcoes_adicionar(self, clientes):
        nome = self.verifica_valores.texto('Digite o nome do cliente: ')
        cpf = self.verifica_valores.cpf('Alterar CPF para: ', clientes)
        endereco = self.verifica_valores.texto('Digite o endereço: ')
        telefone = self.verifica_valores.inteiros('Digite o telefone: ')

        cliente = {
            "nome": nome,
            "cpf": cpf,
            "endereco": endereco,
            "telefone": telefone
        }
        return cliente

    def tela_remover(self):
        return self.verifica_valores.altera_cpf('Digite o cpf do cliente a ser removido [0 para voltar]: ')

    def tela_alterar_opcoes(self):
        print('------ Alterar ------')
        print('1 - Nome')
        print('2 - CPF')
        print('3 - Endereço')
        print('4 - Telefone')
        print('0 - Voltar')
        opcao = self.verifica_valores.inteiros('Digite a opção que deseja alterar: ', list(range(5)))
        return opcao

    def tela_alterar_para(self, nome: bool = False, cpf: bool = False, endereco: bool = False, telefone: bool = False):
        if(nome):
            return self.verifica_valores.texto('Alterar nome para: ')
        if(cpf):
            return self.verifica_valores.altera_cpf('Alterar CPF para: ')
        if(endereco):
            return self.verifica_valores.texto('Alterar endereço para: ')
        if(telefone):
            return self.verifica_valores.inteiros('Alterar telefone para: ')

    def tela_confirma(self):
        print('------ Confirmar ------')
        opcao = self.verifica_valores.sim_ou_nao('Confirmar operação? [S/N]')
        if opcao == 's':
            return True
        else:
            return False

    def escolhe_cliente(self, clientes):
        id_clientes = self.cria_lista_id(clientes)
        return self.verifica_valores.inteiros("Insira o ID do cliente [0 para voltar]: ", id_clientes, "Valor inválido, insira um ID válido")


    def adicionado_com_sucesso(self):
        print('\033[1;36mCLIENTE ADICIONADO COM SUCESSO\033[0m')





