from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente


class ControllerCliente:
    def __init__(self):
        self.__tela_cliente = TelaCliente()
        self.__clientes = [Cliente('Eduardo', '100.100.100-10', 'Rua Douglas Seabra Levier')]
        self.__mantem_tela_aberta = True

    @property
    def clientes(self):
        return self.__clientes

    def inicializa(self):
        self.__mantem_tela_aberta = True
        self.abre_tela_inicial()

    def finaliza(self):
        self.__mantem_tela_aberta = False

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
        for index, cliente in enumerate(self.__clientes):
            if (cliente.id == id):
                cliente.nome = valor

    def altera_cpf(self, id, valor):
        for index, cliente in enumerate(self.__clientes):
            if cliente.id == id:
                cliente.cpf = valor

    def altera_endereco(self, id, valor):
        for index, cliente in enumerate(self.__clientes):
            if cliente.id == id:
                cliente.endereco = valor

    def lista_cliente(self, busca: bool = False):
        self.__tela_cliente.imprime_lista_cliente(self.__clientes)
        if busca:
            return self.__tela_cliente.escolhe_cliente

    def cliente(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente

    def abre_tela_inicial(self):
        switcher = {0: self.finaliza,
                    1: self.adiciona_cliente,
                    2: self.remove_cliente,
                    3: self.abre_tela_altera,
                    4: self.lista_cliente}

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
