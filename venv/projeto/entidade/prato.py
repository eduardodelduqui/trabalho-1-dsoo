from entidade.categoria import Categoria

class Prato:
    __global_id = 0
    def __init__(self, nome: str, categoria: Categoria, preco_unitario: float):
        Prato.__global_id += 1
        self.__nome = nome
        self.__tipo = categoria
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
    def tipo(self, categoria):
        self.__tipo = categoria

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario