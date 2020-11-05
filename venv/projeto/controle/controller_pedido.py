from entidade.pedido import Pedido
from limite.tela_pedido import TelaPedido
from datetime import datetime, date
from controle.controller import Controller


class ControllerPedido(Controller):
    def __init__(self, controle):
        self.__pedidos = []
        self.__controle_principal = controle
        self.__tela_pedido = TelaPedido()
        self.__pedido_em_andamento = ''

    @property
    def pedidos(self):
        return self.__pedidos

    @property
    def ultimo_pedido(self):
        return self.__pedidos[-1]

    @property
    def pedido_em_andamento(self):
        return self.__pedido_em_andamento

    @pedido_em_andamento.setter
    def pedido_em_andamento(self, pedido):
        self.__pedido_em_andamento = pedido

    def adiciona_pedido(self, pedido: Pedido):
        self.__pedidos.append(pedido)

    def remove_pedido(self, pedido: Pedido):
        self.__pedidos.remove(pedido)

    def imprime_lista_cliente(self):
        self.__controle_principal.controller_cliente.imprime_lista_cliente()

    def lista_prato(self):
        self.__controle_principal.controller_prato.lista_prato()

    def imprime_pedido(self, pedido: Pedido = None):
        self.__tela_pedido.imprime_pedido(pedido)

    def imprime_lista_pedidos(self):
        if(self.__pedidos):
            for pedido in self.__pedidos:
                self.imprime_pedido(pedido)
        else:
            self.imprime_pedido()

    def historico_pedidos(self):
        lista = []
        for pedido in self.__pedidos:
            if pedido.data == data_escolhida:
                lista.append(pedido)
        if lista:
            for item in lista: self.imprime_pedido(item)
        else:
            self.imprime_pedido(lista)

    def cadastra_cliente(self):
        self.__controle_principal.controller_cliente.adiciona_cliente()
        cliente = self.__controle_principal.controller_cliente.ultimo_cliente()
        self.pedido_em_andamento.adiciona_cliente(cliente)
        self.abre_tela_cofirma()

    def escolhe_cliente(self):
        self.imprime_lista_cliente()
        id_cliente = self.__tela_pedido.escolhe_cliente(self.__controle_principal.controller_cliente.clientes)
        cliente = self.__controle_principal.controller_cliente.cliente(id_cliente)
        self.pedido_em_andamento.adiciona_cliente(cliente)
        self.abre_tela_cofirma()

    def escolhe_pedido(self):
        self.lista_prato()
        lista_compras = self.__tela_pedido.escolhe_prato(self.__controle_principal.controller_prato.pratos)
        for index, item in enumerate(lista_compras):
            produto = self.__controle_principal.controller_prato.prato(item["id"])
            quantidade = item["qtd"]
            if index == 0:
                pedido = Pedido(produto, quantidade)
                continue
            pedido.adiciona_produto(produto, quantidade)
        self.pedido_em_andamento = pedido
        self.abre_tela_escolhe_cliente()

    def confirma_pedido(self):
        pedido = self.pedido_em_andamento
        pedido.efetua_pagamento()
        self.adiciona_pedido(pedido)
        self.imprime_pedido(pedido)

    def refaz_pedido(self):
        self.escolhe_pedido()

    def cancela_pedido(self):
        self.pedido_em_andamento = None

    def abre_tela_inicial(self):
        switcher = {
            0: self.finaliza,
            1: self.escolhe_pedido,
            2: self.abre_tela_historico}
        opcao = self.__tela_pedido.mostra_tela_opcoes()
        switcher[opcao]()

    def abre_tela_escolhe_cliente(self):
        switcher = {
            0: self.finaliza,
            1: self.abre_tela_cofirma,
            2: self.cadastra_cliente,
            3: self.escolhe_cliente,}
        opcao = self.__tela_pedido.mostra_tela_opcoes_cliente()
        switcher[opcao]()

    def abre_tela_historico(self):
        switcher = {0: self.abre_tela_inicial,
                    1: self.imprime_lista_pedidos,
                    2: self.historico_pedidos}
        opcao = self.__tela_pedido.mostra_tela_historico()
        switcher[opcao]()

    def abre_tela_cofirma(self):
        self.imprime_pedido(self.pedido_em_andamento)
        switcher = {0: self.abre_tela_escolhe_cliente,
                    1: self.confirma_pedido,
                    2: self.refaz_pedido,
                    3: self.cancela_pedido}
        opcao = self.__tela_pedido.confirma_pedido()
        switcher[opcao]()




