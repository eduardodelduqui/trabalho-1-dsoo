from entidade.prato import Prato
from limite.tela_prato import TelaPrato


class ControllerPrato:
    def __init__(self):
        self.__tela_prato = TelaPrato()
        self.__pratos = [Prato("Esfiha", "Lanches", 1.45), Prato("Kibe", "Lanches", 1.35)]
        self.__mantem_tela_aberta = True

    @property
    def pratos(self):
        return self.__pratos

    def inicializa(self):
        self.__mantem_tela_aberta = True
        self.abre_tela_inicial()

    def finaliza(self):
        self.__mantem_tela_aberta = False

    def adiciona_prato(self):
        prato = self.__tela_prato.abre_tela_adicionar()
        self.__pratos.append(Prato(prato["nome"], prato["tipo"], prato["preco"]))

    def remove_prato(self):
        self.lista_prato()
        if self.pratos:
            id = self.__tela_prato.remove_prato()
            for index, prato in enumerate(self.pratos):
                if prato.id == id:
                    self.__pratos.pop(index)

    def altera_nome(self, id, valor):
        for prato in self.pratos:
            if (prato.id == id):
                prato.nome = valor

    def altera_tipo(self, id, valor):
        for prato in self.pratos:
            if (prato.id == id):
                prato.tipo = valor

    def altera_preco(self, id, valor):
        for prato in self.pratos:
            if (prato.id == id):
                prato.preco_unitario = valor

    def lista_prato(self):
        self.__tela_prato.imprime_lista_prato(self.pratos)

    def prato(self, id):
        for prato in self.pratos:
            if prato.id == id:
                return prato



    def abre_tela_inicial(self):
        switcher = {0: self.finaliza,
                    1: self.adiciona_prato,
                    2: self.remove_prato,
                    3: self.abre_tela_altera,
                    4: self.lista_prato}

        while self.__mantem_tela_aberta:
            opcao = self.__tela_prato.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()


    def abre_tela_altera(self):
        self.lista_prato()
        id_prato = self.__tela_prato.escolhe_prato(self.pratos)
        if self.__pratos:
            switcher = {0: self.abre_tela_inicial,
                        1: self.altera_nome,
                        2: self.altera_tipo,
                        3: self.altera_preco}

            input_usuario = self.__tela_prato.tela_alterar()
            funcao_escolhida = switcher[input_usuario["opcao"]](id_prato, input_usuario["valor"])
