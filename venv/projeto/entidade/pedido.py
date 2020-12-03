from entidade.categoria import Categoria
from entidade.prato import Prato
from entidade.cliente import Cliente
from datetime import datetime, date
import shortuuid


class Pedido:
    def __init__(self, prato: Prato, qtd: int):
        self.__id = shortuuid.uuid()
        self.__pratos = [{"item": prato, "qtd": qtd}]
        self.__cliente = None
        self.__valor_total = prato.preco_unitario*qtd
        self.__data = date.today()
        self.__horario = datetime.now().strftime("%H:%M:%S")
        self.__pago = False
        self.__valor_inicial = 0

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
    def pago(self):
        return self.__pago

    @property
    def valor_total(self):
        return self.__valor_total

    def adiciona_cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    def adiciona_prato(self, prato: Prato, qtd: int = 1):
        compra = {"item": prato, "qtd": qtd}
        self.__pratos.append(compra)
        self.calcula_preco_total()

    def calcula_preco_total(self):
        for prato in self.pratos:
            self.__valor_total += prato["item"].preco_unitario*prato["qtd"]

    def efetua_pagamento(self):
        self.__pago = True