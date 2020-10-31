from entidade.prato import Prato
from limite.tela_prato import TelaPrato


class ControllerPrato:
    def __init__(self):
        self.__tela_prato = TelaPrato()
        self.__pratos = [Prato("Esfiha", "Lanches", "1.45"), Prato("Kibe", "Lanches", "1.35")]
        self.__mantem_tela_aberta = True



    def inicializa(self):
        self.abre_tela_inicial()
        pass

    def adiciona_prato(self):
        prato = self.__tela_prato.abre_tela_adicionar()
        self.__pratos.append(Prato(prato["nome"], prato["tipo"]))

    def remove_prato(self):
        self.lista_prato()
        if self.__pratos:
            id = self.__tela_prato.remove_prato()
            for index, prato in enumerate(self.__pratos):
                if prato.id == id:
                    self.__pratos.pop(index)

    def lista_prato(self):
        self.__tela_prato.imprime_lista_prato(self.__pratos)

    def finalizar(self):
        self.__mantem_tela_aberta = False

    def abre_tela_inicial(self):
        self.__mantem_tela_aberta = True
        switcher = {0: self.finalizar,
                    1: self.adiciona_prato,
                    2: self.remove_prato,
                    3: self.lista_prato}

        while self.__mantem_tela_aberta:
            opcao = self.__tela_prato.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
