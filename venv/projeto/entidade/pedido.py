from entidade.categoria import Categoria
from entidade.prato import Prato
from entidade.cliente import Cliente
from entidade.produto import Produto
from datetime import datetime, date
import uuid


class Pedido:

    def __init__(self, cliente: Cliente, prato: Prato):
        self.__codigo = uuid.uuid4().hex
        self.__prato = prato
        self.__cliente = cliente
        self.__data = date.today
        self.__horario = datetime.now().strftime("%H:%M:%S")

    def imprime(self):
        return dict(pedido=self.__codigo,
                    prato=self.__prato.nome,
                    cliente=self.__cliente.nome,
                    data=self.__data,
                    horario=self.__horario)