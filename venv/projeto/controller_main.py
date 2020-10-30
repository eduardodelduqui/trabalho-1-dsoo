from tela_main import TelaMain
from controle.controller_cliente import ControllerCliente
from controle.controller_loja import ControllerLoja

class ControllerMain:
    def __init__(self):
        self.__tela_main = TelaMain()
        self.__controller_cliente = ControllerCliente()
        self.__controller_loja = ControllerLoja()

    def inicializa_sistema(self):
        self.abre_tela_inicial()

    def finalizar(self):
        exit(0)

    def cliente(self):
        self.__controller_cliente.inicializa()

    def loja(self):
        self.__controller_loja.inicializa()
        
    def abre_tela_inicial(self):
        switcher = {0: self.finalizar,
                    1: self.cliente,
                    2: self.loja}

        while True:
            opcao = self.__tela_main.mostra_tela_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()