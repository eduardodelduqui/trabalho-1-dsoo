from entidade.produto import Produto


class Prato:
    def __init__(self, nome: str, tipo: str):
        self.__nome = nome
        self.__tipo = tipo
        self.__telefone = None
        self.__cnpj = None
        self.__id = None
        self.__produtos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def tipo(self):
        return self.__tipo

    @property
    def telefone(self):
        return self.__telefone

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def id(self):
        return self.__id

    @property
    def produtos(self):
        return self.__produtos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    def adicionaProduto(self, produto):
        if isinstance(produto, Produto):
            if produto not in self.__produtos:
                self.__produtos.append(produto)
            else:
                print("Produto duplicado")
        else:
            print(f'{produto} não é um produto')

