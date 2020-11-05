from entidade.pedido import Pedido
from limite.tela_pedido import TelaPedido
from datetime import datetime, date


class ControllerPedido:
    def __init__(self, controle):
        self.__pedidos = []
        self.__controle_principal = controle
        self.__tela_pedido = TelaPedido()
        self.__mantem_tela_aberta = bool

    @property
    def pedidos(self):
        return self.__pedidos

    @property
    def ultimo_pedido(self):
        return self.__pedidos[-1]

    def inicializa(self):
        self.__mantem_tela_aberta = True
        self.abre_tela_inicial()

    def finaliza(self):
        self.__mantem_tela_aberta = False

    def adiciona_pedido(self, pedido: Pedido):
        self.__pedidos.append(pedido)

    def remove_pedido(self, pedido: Pedido):
        self.__pedidos.remove(pedido)

    def lista_cliente(self):
        self.__controle_principal.controller_cliente.lista_cliente()

    def lista_prato(self):
        self.__controle_principal.controller_prato.lista_prato()

    def imprime_pedido(self, pedido: Pedido = None):
        self.__tela_pedido.imprime_pedido(pedido)

    def imprime_lista_pedidos(self):
        if(self.__pedidos):
            for pedido in self.__pedidos:
                self.imprime_pedido(pedido)
        else:
            self.imprime_pedido()

    def historico_pedidos(self):
        lista = []
        for pedido in self.__pedidos:
            if pedido.data == date.today():
                lista.append(pedido)
        if lista:
            for item in lista: self.imprime_pedido(item)
        else:
            self.imprime_pedido()

    def cadastra_cliente(self):
        self.__controle_principal.controller_cliente.adiciona_cliente()
        cliente = self.__controle_principal.controller_cliente.ultimo_cliente()
        print(cliente)
        pedido = self.ultimo_pedido
        pedido.adiciona_cliente(cliente)
        self.imprime_pedido(pedido)

    def escolhe_cliente(self):
        pedido = self.ultimo_pedido
        self.lista_cliente()
        id_cliente = self.__tela_pedido.escolhe_cliente(self.__controle_principal.controller_cliente.clientes)
        cliente = self.__controle_principal.controller_cliente.cliente(id_cliente)
        pedido.adiciona_cliente(cliente)
        self.imprime_pedido(pedido)

    def escolhe_pedido(self):
        self.lista_prato()
        lista_compras = self.__tela_pedido.escolhe_prato(self.__controle_principal.controller_prato.pratos)
        for index, item in enumerate(lista_compras):
            produto = self.__controle_principal.controller_prato.prato(item["id"])
            quantidade = item["qtd"]
            if index == 0:
                pedido = Pedido(produto, quantidade)
                continue
            pedido.adiciona_produto(produto, quantidade)
        self.adiciona_pedido(pedido)
        self.abre_tela_escolhe_cliente()

    def abre_tela_escolhe_cliente(self):
        switcher = {
            0: self.finaliza,
            1: self.imprime_pedido,
            2: self.cadastra_cliente,
            3: self.escolhe_cliente,}
        opcao = self.__tela_pedido.mostra_tela_opcoes_cliente()
        if opcao == 1:
            switcher[opcao](self.ultimo_pedido)
        else:
            switcher[opcao]()

    def abre_tela_inicial(self):
        switcher = {
            0: self.finaliza,
            1: self.escolhe_pedido,
            2: self.imprime_lista_pedidos,
            3: self.historico_pedidos}
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        switcher[opcao]()



