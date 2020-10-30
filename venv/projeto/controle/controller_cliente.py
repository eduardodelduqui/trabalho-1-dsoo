from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente


class ControllerCliente:
    def __init__(self):
        self.__tela_cliente = TelaCliente()
        self.__clientes = []


    def inicializa(self):
        self.abre_tela_inicial()

    def adiciona_cliente(self):
        print('abrindo tela adicionar')
        cliente = self.__tela_cliente.opcoes_adicionar()
        self.__clientes.append(Cliente(cliente["nome"], cliente["cpf"]))
        print(cliente)

    def remove_cliente(self):
        print('removendo cliente')
        # self.__clientes.remove(cliente)

    def lista_cliente(self):
        print('Clientes')
        for cliente in self.__clientes:
            print(f'Nome: {cliente.nome}    cpf: {cliente.cpf}')

    def finalizar(self):
        exit(0)


    def abre_tela_inicial(self):
        switcher = {0: self.finalizar,
                    1: self.adiciona_cliente,
                    2: self.remove_cliente,
                    3: self.lista_cliente}

        while True:
            opcao = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
