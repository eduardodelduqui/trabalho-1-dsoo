from entidade.categoria import Categoria

class Produto:
    _contador = 0
    def __init__(self, nome: str, preco_unitario: float, categoria: str):
        self.__nome = nome
        self.__preco_unitario = preco_unitario
        self.__quantidade = None
        self.__categoria = Categoria(categoria)
        # Produto._contador += 1
        # self.__codigo = Produto._contador


    @property
    def nome(self):
        return self.__nome

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def categoria(self):
        return self.__categoria

    # @property
    # def codigo(self):
    #     return self.__codigo

    @property
    def preco_total(self):
        return self.__quantidade*self.__preco_unitario

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria


