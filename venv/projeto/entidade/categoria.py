
class Categoria:
    __global_id = 0
    def __init__(self, nome: str):
        Categoria.__global_id += 1
        self.__id = Categoria.__global_id
        self.__nome = nome


    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id

    @nome.setter
    def nome(self, nome):
        self.__nome = nome