from entidade.categoria import Categoria
from entidade.prato import Prato
from entidade.cliente import Cliente
from entidade.produto import Produto
from datetime import datetime, date
import shortuuid


class Pedido:

    def __init__(self, cliente: Cliente):
        self.__codigo = shortuuid.uuid()
        self.__produtos = []
        self.__cliente = cliente
        self.__valor_total = None
        self.__data = date.today()
        self.__horario = datetime.now().strftime("%H:%M:%S")
        self.__pago = False
        self.__valor_inicial = 0

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def produtos(self):
        return self.__produtos

    @property
    def data(self):
        return self.__data

    @property
    def horario(self):
        return self.__horario

    @property
    def pago(self):
        return self.__pago

    @property
    def valor_total(self):
        return self.__valor_total

    def adiciona_produto(self, produto: Prato, qtd: int = 1):
        compra = {"item": produto, "qtd": qtd}
        self.__produtos.append(compra)
        self.calcula_preco_total()

    def calcula_preco_total(self):
        valor = self.__valor_inicial
        for produto in self.produtos:
            valor += produto["item"].preco_unitario*produto["qtd"]
        self.__valor_total = valor

    def efetua_pagamento(self):
        self.__pago = True