from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente


class ControllerCliente:
    def __init__(self, controlador):
        self.__tela_cliente = TelaCliente()
        self.__clientes = []
        self.__controle_principal = controlador
        self.__mantem_tela_aberta = True


    def inicializa(self):
        self.abre_tela_inicial()

    def adiciona_cliente(self):
        print('abrindo tela adicionar')
        cliente = self.__tela_cliente.opcoes_adicionar()
        self.__clientes.append(Cliente(cliente["nome"], cliente["cpf"]))
        print(cliente)

    def remove_cliente(self):
        print('Remover cliente')
        self.lista_cliente()
        cpfLoja = self.__tela_cliente.tela_remover()
        for index, cliente in enumerate(self.__clientes):
            if(cliente.cpf == cpfLoja):
                self.__clientes.pop(index)
        print('Cliente removido')

    def lista_cliente(self):
        print('Clientes')
        for cliente in self.__clientes:
            print(f'Nome: {cliente.nome}    cpf: {cliente.cpf}')

    def lista_loja(self):
        pass



    def finalizar(self):
        self.__mantem_tela_aberta = False


    def abre_tela_inicial(self):

        switcher = {0: self.finalizar,
                    1: self.adiciona_cliente,
                    2: self.remove_cliente,
                    3: self.lista_cliente,
                    4: self.lista_loja}

        while self.__mantem_tela_aberta:
            opcao = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
