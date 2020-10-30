

class Categoria:
    def __init__(self, codigo: int):
        self.__lista = []
        if (codigo > 0 and codigo <= len(self.__lista)):
            self.__nome = self.__lista[codigo - 1]

    @property
    def categorias(self):
        return self.__lista

    def adiciona(self, categoria):
        self.__lista.append(categoria)
