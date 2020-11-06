from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria
from controle.controller import Controller

class ControllerCategoria(Controller):
    def __init__(self):
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()
        self.__tela_escolhe_categoria_aberta = True

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
        while self.__tela_escolhe_categoria_aberta:
            self.imprime_lista()
            id_categoria = self.__tela_categoria.escolhe_categoria(self.categorias)
            if id_categoria == 0:
                self.__tela_escolhe_categoria_aberta == False
                print('voltar')
                break
            else:
                categoria = self.categoria(id_categoria)
                print(categoria)
                return categoria

    def categoria(self, id):
        for categoria in self.__categorias:
            return categoria

    def abre_tela_inicial(self):
        switcher = {1: self.adiciona_categoria,
                    2: self.escolhe_categoria}
        opcao = self.__tela_categoria.mostra_tela_opcoes(self.categorias)
        funcao_escolhida = switcher[opcao]
        funcao_escolhida()

