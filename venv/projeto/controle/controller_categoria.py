from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria
from controle.controller import Controller

class ControllerCategoria(Controller):
    def __init__(self):
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()

    @property
    def categorias(self):
        return self.__categorias

    @property
    def tela_categoria(self):
        return self.__tela_categoria


    def imprime_lista(self):
        self.__tela_categoria.imprime_lista(self.categorias)

    def adiciona_categoria(self):
        nome = self.tela_categoria.adiciona_categoria()
        categoria = Categoria(nome)
        self.__categorias.append(categoria)
        return categoria

    def escolhe_categoria(self):
        self.imprime_lista()
        id_categoria = self.__tela_categoria.escolhe_categoria(self.categorias)
        categoria = self.categoria(id_categoria)
        return categoria

    def categoria(self, id):
        for categoria in self.__categorias:
            return categoria

    def abre_tela_inicial(self):
        switcher = {0: self.finaliza,
                    1: self.escolhe_categoria,
                    2: self.adiciona_categoria}
        opcao = self.__tela_categoria.mostra_tela_opcoes()
        funcao_escolhida = switcher[opcao]
        funcao_escolhida()
