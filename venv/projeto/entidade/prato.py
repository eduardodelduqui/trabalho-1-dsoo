from entidade.produto import Produto


class Prato:
    __global_id = 0
    def __init__(self, nome: str, tipo: str, preco_unitario: float):
        Prato.__global_id += 1
        self.__nome = nome
        self.__tipo = tipo
        self.__id = Prato.__global_id
        self.__preco_unitario = preco_unitario

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @property
    def id(self):
        return self.__id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario