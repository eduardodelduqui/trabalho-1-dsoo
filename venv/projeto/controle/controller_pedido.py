from entidade.pedido import Pedido


class ControllerPedido:
    def __init__(self):
        self.__pedidos = []

    @property
    def pedido(self):
        return self.__pedidos

    def adiciona_pedido(self, pedido: Pedido):
        self.__pedidos.append(pedido)

    def remove_pedido(self, pedido: Pedido):
        self.__pedidos.remove(pedido)


