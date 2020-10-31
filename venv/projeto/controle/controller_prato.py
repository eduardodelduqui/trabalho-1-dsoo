from entidade.prato import Prato
from limite.tela_prato import TelaPrato


class ControllerPrato:
    def __init__(self):
        self.__tela_prato = TelaPrato()
        self.__pratos = [Prato("Habib's", "Lanches"), Prato("Pizza Hut", "Pizza")]



    def inicializa(self):
        self.abre_tela_inicial()
        pass

    def adiciona_prato(self):
        prato = self.__tela_prato.abre_tela_adicionar()
        self.__pratos.append(Prato(prato["nome"], prato["tipo"]))
        print(len(self.__pratos))

    def remove_prato(self):
        pass

    def lista_prato(self):
        print('Pratos')
        for prato in self.__pratos:
            print(f'Nome: {prato.nome}    Categoria: {prato.tipo}')

    def finalizar(self):
        exit(0)

    def abre_tela_inicial(self):
        switcher = {0: self.finalizar,
                    1: self.adiciona_prato,
                    2: self.remove_prato,
                    3: self.lista_prato}

        while True:
            opcao = self.__tela_prato.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()
