from tela_main import TelaMain
from controle.controller_cliente import ControllerCliente
from controle.controller_prato import ControllerPrato

class ControllerMain:
    def __init__(self):
        self.__tela_main = TelaMain()
        self.__controller_cliente = ControllerCliente(self)
        self.__controller_prato = ControllerPrato()

    @property
    def controller_prato(self):
        return self.__controller_prato

    def inicializa_sistema(self):
        self.abre_tela_inicial()

    def finalizar(self):
        exit(0)

    def cliente(self):
        self.__controller_cliente.inicializa()

    def prato(self):
        self.__controller_prato.inicializa()
        
    def abre_tela_inicial(self):
        switcher = {0: self.finalizar,
                    1: self.cliente,
                    2: self.prato}

        while True:
            opcao = self.__tela_main.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()