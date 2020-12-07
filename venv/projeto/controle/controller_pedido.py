from entidade.pedido import Pedido
from limite.tela_pedido import TelaPedido
from datetime import datetime, date
from controle.controller import Controller
from persistencia.pedido_dao import PedidoDAO


class ControllerPedido(Controller):
    def __init__(self, controle):
        self.__pedido_dao = PedidoDAO()
        self.__controle_principal = controle
        self.__tela_pedido = TelaPedido()
        self.__pedido_em_andamento = None

    @property
    def pedidos(self):
        return self.__pedido_dao.get_all()

    @property
    def ultimo_pedido(self):
        return self.pedidos[-1]

    @property
    def pedido_em_andamento(self):
        return self.__pedido_em_andamento

    @property
    def controle_principal(self):
        return self.__controle_principal

    @pedido_em_andamento.setter
    def pedido_em_andamento(self, pedido):
        self.__pedido_em_andamento = pedido

    def adiciona_pedido(self, pedido: Pedido):
        self.__pedido_dao.add(pedido)

    def remove_pedido(self, pedido: Pedido):
        self.__pedidos_dao.remove(pedido)

    def imprime_lista_cliente(self):
        self.__controle_principal.controller_cliente.imprime_lista_cliente()

    def lista_prato(self):
        self.__controle_principal.controller_prato.imprime_lista_prato()

    def imprime_pedido(self, pedido: Pedido = None):
        if self.__tela_pedido.imprime_pedido(pedido) == 0:
            self.lista_historico_pedidos()

    def lista_historico_pedidos(self):
        id_pedido = self.__tela_pedido.lista_historico_pedido(self.pedidos)
        if id_pedido != 0:
            self.imprime_pedido(self.__pedido_dao.get(id_pedido))
        else:
            self.abre_tela_inicial()

    def cadastra_cliente(self):
        cliente = self.__controle_principal.controller_cliente.adiciona_cliente(retorna=True)
        self.pedido_em_andamento.adiciona_cliente(cliente)
        self.abre_tela_confirma()

    def escolhe_cliente(self):
        cpf_cliente = self.__controle_principal.controller_cliente.escolhe_cliente()
        cliente = self.__controle_principal.controller_cliente.cliente(cpf_cliente)
        self.pedido_em_andamento.adiciona_cliente(cliente)
        self.abre_tela_confirma()

    def escolhe_pedido(self):
        lista_compras = []
        while True:
            valores = self.__tela_pedido.escolhe_prato(self.__controle_principal.controller_prato.pratos, lista_compras)
            if valores == 0:
                self.cancela_pedido()
                self.abre_tela_inicial()
            if valores == 1:
                for index, item in enumerate(lista_compras):
                    produto = self.__controle_principal.controller_prato.prato(item["id"])
                    quantidade = item["qtd"]
                    if index == 0:
                        pedido = Pedido(produto, quantidade)
                        continue
                    pedido.adiciona_prato(produto, quantidade)
                self.pedido_em_andamento = pedido
                self.abre_tela_escolhe_cliente()
            else:
                produto = self.__controle_principal.controller_prato.prato(valores['id'])
                lista_compras.append({
                    "id": valores["id"],
                    "nome": produto.nome,
                    "qtd": valores["qtd"],
                    "valor_total": valores["qtd"]*produto.preco_unitario
                })

    def confirma_pedido(self):
        pedido = self.pedido_em_andamento
        self.adiciona_pedido(pedido)
        self.abre_tela_inicial()

    def refaz_pedido(self):
        self.escolhe_pedido()

    def cancela_pedido(self):
        self.pedido_em_andamento = None
        self.abre_tela_inicial()


    def abre_tela_inicial(self):
        switcher = {
            0: self.__controle_principal.abre_tela_inicial,
            1: self.escolhe_pedido,
            2: self.lista_historico_pedidos}
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        switcher[opcao]()

    def abre_tela_escolhe_cliente(self):
        switcher = {
            0: self.cancela_pedido,
            1: self.abre_tela_confirma,
            2: self.cadastra_cliente,
            3: self.escolhe_cliente,
            4: self.finaliza}
        opcao = self.__tela_pedido.mostra_tela_opcoes_cliente(self.controle_principal.controller_cliente.clientes)
        switcher[opcao]()

    def abre_tela_confirma(self):
        switcher = {0: self.abre_tela_escolhe_cliente,
                    1: self.confirma_pedido,
                    2: self.refaz_pedido,
                    3: self.cancela_pedido}
        opcao = self.__tela_pedido.confirma_pedido(self.pedido_em_andamento)
        switcher[opcao]()




