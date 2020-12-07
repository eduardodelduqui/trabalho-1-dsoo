from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from controle.controller import Controller
from persistencia.cliente_dao import ClienteDAO


class ControllerCliente(Controller):
    def __init__(self, controle):
        self.__cliente_dao = ClienteDAO()
        self.__tela_cliente = TelaCliente()
        self.__controle_principal = controle
        self.__cliente_em_andamento = None

    @property
    def clientes(self):
        return self.__cliente_dao.get_all()

    @property
    def tela_cliente(self):
        return self.__tela_cliente

    @property
    def controle_principal(self):
        return self.__controle_principal

    def adiciona_cliente(self, retorna = False):
        cliente = self.tela_cliente.opcoes_adicionar(self.clientes)
        if cliente != 0:
            self.__cliente_em_andamento = Cliente(cliente["nome"], cliente["cpf"], cliente["endereco"], cliente["telefone"])
            self.__cliente_dao.add(self.__cliente_em_andamento)
            if retorna:
                return self.__cliente_em_andamento

    def remove_cliente(self):
        cpf = self.tela_cliente.escolhe_cliente(self.clientes)
        if cpf != 0:
            self.__cliente_dao.remove(cpf)

    def altera_cliente(self, cpf, valores):
        cliente = Cliente(valores["nome"], valores["cpf"], valores["endereco"], valores["telefone"])
        if cliente != 0:
            self.__cliente_dao.remove(cpf)
            self.__cliente_dao.add(cliente)
        else:
            self.abre_tela_inicial()

    def imprime_lista_cliente(self):
        self.tela_cliente.imprime_lista_cliente(self.clientes)

    def imprime_cliente(self, cliente):
        self.tela_cliente.imprime_cliente(cliente)

    def cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente

    def ultimo_cliente(self):
        for index, cliente in enumerate(self.clientes):
            if index == len(self.clientes)-1:
                return cliente

    def busca_cliente(self):
        while True:
            id_cliente = self.tela_cliente.escolhe_cliente(self.clientes)
            if id_cliente == 0:
                break
            self.imprime_cliente(self.cliente(id_cliente))

    def escolhe_cliente(self):
        return self.tela_cliente.escolhe_cliente(self.clientes)

    def confirma(self):
        return self.tela_cliente.tela_confirma()

    def abre_tela_inicial(self):
        switcher = {0: self.controle_principal.abre_tela_inicial,
                    1: self.adiciona_cliente,
                    2: self.remove_cliente,
                    3: self.abre_tela_altera,
                    4: self.imprime_lista_cliente
                    }

        while self.mantem_tela_aberta:
            opcao = self.tela_cliente.mostra_tela_opcoes(self.clientes)
            funcao_escolhida = switcher[opcao]()

    def abre_tela_altera(self):
        while True:
            cpf = self.escolhe_cliente()
            if cpf != 0:
                valores = self.tela_cliente.tela_alterar_opcoes(self.cliente(cpf), self.clientes)
                if valores != 0:
                    self.altera_cliente(cpf, valores)
            else:
                self.abre_tela_inicial()