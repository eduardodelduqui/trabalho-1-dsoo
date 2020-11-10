from entidade.categoria import Categoria
from entidade.prato import Prato
from entidade.cliente import Cliente
from datetime import datetime, date
import shortuuid


class Pedido:
    def __init__(self, prato: Prato, qtd: int):
        self.__codigo = shortuuid.uuid()
        self.__produtos = [{"item": produto, "qtd": qtd}]
        self.__cliente = None
        self.__valor_total = produto.preco_unitario*qtd
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

    def adiciona_cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    def adiciona_produto(self, produto: Prato, qtd: int = 1):
        compra = {"item": produto, "qtd": qtd}
        self.__produtos.append(compra)
        self.calcula_preco_total()

    def calcula_preco_total(self):
        for produto in self.produtos:
            self.__valor_total += produto["item"].preco_unitario*produto["qtd"]

    def efetua_pagamento(self):
        self.__pago = True