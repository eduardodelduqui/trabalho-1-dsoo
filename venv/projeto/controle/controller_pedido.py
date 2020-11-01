from entidade.pedido import Pedido
from limite.tela_pedido import TelaPedido


class ControllerPedido:
    def __init__(self, controle):
        self.__pedidos = []
        self.__controle_principal = controle
        self.__tela_pedido = TelaPedido()
        self.__mantem_tela_aberta = bool

    @property
    def pedidos(self):
        return self.__pedidos

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

    def imprime_pedido(self, pedido):
        self.__tela_pedido.imprime_pedido(pedido)

    def imprime_lista_pedidos(self):
        for pedido in self.__pedidos:
            self.imprime_pedido(pedido)

    def escolhe_cliente(self):
        self.lista_cliente()
        id_cliente = self.__tela_pedido.escolhe_cliente(self.__controle_principal.controller_cliente.clientes)
        cliente = self.__controle_principal.controller_cliente.cliente(id_cliente)
        pedido = Pedido(cliente)

    def escolhe_pedido(self):
        self.lista_cliente()
        id_cliente = self.__tela_pedido.escolhe_cliente(self.__controle_principal.controller_cliente.clientes)
        cliente = self.__controle_principal.controller_cliente.cliente(id_cliente)
        pedido = Pedido(cliente)
        self.lista_prato()
        lista_compras = self.__tela_pedido.escolhe_prato(self.__controle_principal.controller_prato.pratos)
        for item in lista_compras:
            produto = self.__controle_principal.controller_prato.prato(item["id"])
            quantidade = item["qtd"]
            pedido.adiciona_produto(produto, quantidade)
        self.adiciona_pedido(pedido)
        self.imprime_pedido(pedido)



    def abre_tela_inicial(self):
        switcher = {
            0: self.finaliza,
            1: self.escolhe_pedido,
            2: self.imprime_lista_pedidos
        }

        opcao = self.__tela_pedido.mostra_tela_opcoes()
        switcher[opcao]()


