from entidade.prato import Prato
from limite.tela_prato import TelaPrato
from entidade.categoria import Categoria
from controle.controller import Controller
from persistencia.prato_dao import PratoDAO

class ControllerPrato(Controller):
    def __init__(self, controle):
        self.__tela_prato = TelaPrato()
        self.__prato_dao = PratoDAO()
        self.__controle_principal = controle

    @property
    def pratos(self):
        return self.__prato_dao.get_all()

    @property
    def tela_prato(self):
        return self.__tela_prato
    @property
    def controle_principal(self):
        return self.__controle_principal

    def adiciona_prato(self):
        prato = self.__tela_prato.abre_tela_adicionar()
        opcao = self.__controle_principal.controller_categoria.tela_categoria.mostra_tela_opcoes(self.pratos)
        if opcao == 1: categoria_prato = self.adiciona_categoria()
        else: categoria_prato = self.escolhe_categoria()
        self.__prato_dao.add(Prato(prato["nome"], categoria_prato, prato["preco"]))

    def escolhe_categoria(self):
        categoria_prato = self.__controle_principal.controller_categoria.escolhe_categoria()
        return categoria_prato

    def adiciona_categoria(self):
        categoria_prato = self.__controle_principal.controller_categoria.adiciona_categoria()
        return categoria_prato

    def remove_prato(self):
        self.lista_prato()
        if self.pratos:
            id = self.__tela_prato.remove_prato()
            self.__prato_dao.remove(id)

    def altera_nome(self, id):
        valor = self.tela_prato.altera_nome()
        for prato in self.pratos:
            if (prato.id == id):
                prato.nome = valor

    def altera_tipo(self, id):
        opcao = self.tela_prato.tela_altera_categoria()
        if opcao == 1:
            categoria = self.controle_principal.controller_categoria.escolhe_categoria()
        if opcao == 2:
            categoria = self.controle_principal.controller_categoria.adiciona_categoria()
        else:
            self.abre_tela_altera
        for prato in self.pratos:
            if (prato.id == id):
                prato.tipo = categoria

    def altera_preco(self, id):
        valor = self.tela_prato.altera_preco()
        for prato in self.pratos:
            if (prato.id == id):
                prato.preco_unitario = valor

    def imprime_lista_prato(self):
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
                    4: self.imprime_lista_prato}

        while self.mantem_tela_aberta:
            opcao = self.__tela_prato.mostra_tela_opcoes(self.pratos)
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()


    def abre_tela_altera(self):
            self.imprime_lista_prato()
            id_prato = self.__tela_prato.escolhe_prato(self.pratos)
            if id_prato != 0:
                if self.pratos:
                    switcher = {0: self.abre_tela_inicial,
                                1: self.altera_nome,
                                2: self.altera_tipo,
                                3: self.altera_preco}
                while True:
                    opcao = self.__tela_prato.tela_alterar()
                    if opcao != 0:
                        switcher[opcao](id_prato)
                    else:
                        switcher[opcao]()

            else:
                self.abre_tela_inicial()
