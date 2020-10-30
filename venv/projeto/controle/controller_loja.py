from entidade.loja import Loja
from limite.tela_loja import TelaLoja


class ControllerLoja:
    def __init__(self):
        self.__tela_loja = TelaLoja()
        self.__lojas = []


    def inicializa(self):
        self.abre_tela_inicial()
        pass

    def adiciona_loja(self):
        pass
        # if isinstance(loja, Loja) and loja not in self.__lojas:
        #     self.__lojas.append(loja)

    def remove_loja(self):
        pass
        # self.__lojas.remove(loja)

    def lista_loja(self):
        return self.__lojas

    def finalizar(self):
        exit(0)

    def abre_tela_inicial(self):
        switcher = {0: self.finalizar,
                    1: self.adiciona_loja,
                    2: self.remove_loja,
                    3: self.lista_loja}

        while True:
            opcao = self.__tela_loja.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
