from entidade.categoria import Categoria
from entidade.prato import Prato
from entidade.cliente import Cliente
from datetime import datetime, date
import shortuuid


class Pedido:
    def __init__(self, prato: Prato, qtd: int):
        if isinstance(prato, Prato) and isinstance(qtd, int):
            self.__id = shortuuid.uuid()[:5]
            self.__pratos = [{"item": prato, "qtd": qtd}]
            self.__cliente = None
            self.__data = date.today()
            self.__horario = datetime.now().strftime("%H:%M:%S")

    @property
    def id(self):
        return self.__id

    @property
    def cliente(self):
        return self.__cliente

    @property
    def pratos(self):
        return self.__pratos

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def valor_total(self):
        valor_total = 0
        for prato in self.pratos:
            valor_total += prato["item"].preco_unitario * prato["qtd"]
        return valor_total

    def adiciona_cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    def adiciona_prato(self, prato: Prato, qtd: int = 1):
        compra = {"item": prato, "qtd": qtd}
        self.__pratos.append(compra)