from entidade.pedido import Pedido
from limite.tela_pedido import TelaPedido


class ControllerPedido:
    def __init__(self, controle):
        self.__pedidos = []
        self.__controle_principal = controle
        self.__tela_pedido = TelaPedido()
        self.__mantem_tela_aberta = bool

    @property
    def pedido(self):
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

    def escolhe_pedido(self):
        print('Escolhendo pedido')

    def abre_tela_inicial(self):
        switcher = {
            0: self.finaliza,
            1: self.escolhe_pedido
        }

        opcao = self.__tela_pedido.mostra_tela_opcoes()
        switcher[opcao]()


