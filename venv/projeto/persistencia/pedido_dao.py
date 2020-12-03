from persistencia.abstract_dao import AbstractDAO
from entidade.pedido import Pedido

class PedidoDAO(AbstractDAO):
    def __init__(self):
        super().__init__('pedidos.pkl')

    def add(self, pedido: Pedido):
        if ((pedido is not None) and (isinstance(pedido, Pedido)) and (isinstance(pedido.id, str))):
            print('adicionando')
            super().add(pedido.id, pedido)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)