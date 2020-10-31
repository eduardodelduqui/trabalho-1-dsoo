from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente


class ControllerCliente:
    def __init__(self, controlador):
        self.__tela_cliente = TelaCliente()
        self.__clientes = [Cliente('Eduardo', '100.100.100-10', 'Rua Douglas Seabra Levier')]
        self.__controle_principal = controlador
        self.__mantem_tela_aberta = True


    def inicializa(self):
        self.abre_tela_inicial()

    def adiciona_cliente(self):
        print('abrindo tela adicionar')
        cliente = self.__tela_cliente.opcoes_adicionar()
        self.__clientes.append(Cliente(cliente["nome"], cliente["cpf"], cliente["endereco"]))
        print(cliente)

    def remove_cliente(self):
        self.lista_cliente()
        if self.__clientes:
            cpfCliente = self.__tela_cliente.tela_remover()
            for index, cliente in enumerate(self.__clientes):
                if(cliente.cpf == cpfCliente):
                    self.__clientes.pop(index)

    def altera_nome(self, id, valor):
        print(id)
        print(valor)
        for index, cliente in enumerate(self.__clientes):
            print(cliente.id)
            if (cliente.id == id):
                print("match")
                cliente.nome = valor

    def altera_cpf(self):
        for index, cliente in enumerate(self.__clientes):
            if cliente.id == id:
                cliente.cpf = valor

    def altera_endereco(self):
        for index, cliente in enumerate(self.__clientes):
            if cliente.id == id:
                cliente.endereco = valor

    def lista_cliente(self):
        self.__tela_cliente.imprime_lista_cliente(self.__clientes)

    def lista_loja(self):
        self.__controle_principal.controller_prato.lista_prato()

    def finalizar(self):
        self.__mantem_tela_aberta = False

    def abre_tela_inicial(self):
        self.__mantem_tela_aberta = True
        switcher = {0: self.finalizar,
                    1: self.adiciona_cliente,
                    2: self.remove_cliente,
                    3: self.abre_tela_altera,
                    4: self.lista_cliente,
                    5: self.lista_loja}

        while self.__mantem_tela_aberta:
            opcao = self.__tela_cliente.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]()


    def abre_tela_altera(self):
        self.lista_cliente()
        if self.__clientes:
            switcher = {0: self.abre_tela_inicial,
                        1: self.altera_nome,
                        2: self.altera_cpf,
                        3: self.altera_endereco}

            input_usuario = self.__tela_cliente.tela_alterar()
            funcao_escolhida = switcher[input_usuario["opcao"]](input_usuario["id"], input_usuario["valor"])
