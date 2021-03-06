from tela_main import TelaMain
from controle.controller_cliente import ControllerCliente
from controle.controller_prato import ControllerPrato
from controle.controller_pedido import ControllerPedido
from controle.controller_categoria import ControllerCategoria

class ControllerMain:
    def __init__(self):
        self.__tela_main = TelaMain()
        self.__controller_cliente = ControllerCliente(self)
        self.__controller_prato = ControllerPrato(self)
        self.__controller_categoria = ControllerCategoria()
        self.__controller_pedido = ControllerPedido(self)

    @property
    def controller_prato(self):
        return self.__controller_prato

    @property
    def controller_cliente(self):
        return self.__controller_cliente

    @property
    def controller_categoria(self):
        return self.__controller_categoria

    @property
    def controller_pedido(self):
        return self.__controller_pedido

    def inicializa_sistema(self):
        self.abre_tela_inicial()

    def finalizar(self):
        exit('Aplicativo encerrado')

    def cliente(self):
        self.__controller_cliente.inicializa()

    def prato(self):
        self.__controller_prato.inicializa()

    def pedido(self):
        self.__controller_pedido.inicializa()
        
    def abre_tela_inicial(self):
        switcher = {0: self.finalizar,
                    1: self.cliente,
                    2: self.prato,
                    3: self.pedido}

        opcao = self.__tela_main.mostra_tela_opcoes()
        funcao_escolhida = switcher[opcao]
        funcao_escolhida()