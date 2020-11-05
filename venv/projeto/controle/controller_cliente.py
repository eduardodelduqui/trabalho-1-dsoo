from entidade.cliente import Cliente
from limite.tela_cliente import TelaCliente
from controle.controller import Controller


class ControllerCliente(Controller):
    def __init__(self):
        self.__tela_cliente = TelaCliente()
        self.__clientes = []
        self.__cliente_em_andamento = None

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tela_cliente(self):
        return self.__tela_cliente

    def adiciona_cliente(self):
        cliente = self.tela_cliente.opcoes_adicionar(self.clientes)
        self.__cliente_em_andamento = Cliente(cliente["nome"], cliente["cpf"], cliente["endereco"], cliente["telefone"])
        self.imprime_cliente(self.__cliente_em_andamento)
        if self.confirma():
            self.__clientes.append(self.__cliente_em_andamento)
            self.tela_cliente.adicionado_com_sucesso()
        else:
            self.__cliente_em_andamento = None

    def remove_cliente(self):
        self.imprime_lista_cliente()
        if self.clientes:
            cpf_cliente = self.tela_cliente.tela_remover()
            if cpf_cliente == 0:
                self.finaliza()
            for index, cliente in enumerate(self.clientes):
                if(cliente.cpf == cpf_cliente):
                    self.__clientes.pop(index)

    def altera_nome(self, id):
        valor = self.tela_cliente.tela_alterar_para(nome=True)
        for index, cliente in enumerate(self.clientes):
            if (cliente.id == id):
                cliente.nome = valor

    def altera_cpf(self, id):
        valor = self.tela_cliente.tela_alterar_para(cpf=True)
        for index, cliente in enumerate(self.clientes):
            if cliente.id == id:
                cliente.cpf = valor

    def altera_endereco(self, id):
        valor = self.tela_cliente.tela_alterar_para(endereco=True)
        for index, cliente in enumerate(self.clientes):
            if cliente.id == id:
                cliente.endereco = valor

    def altera_telefone(self, id):
        valor = self.tela_cliente.tela_alterar_para(telefone=True)
        for index, cliente in enumerate(self.clientes):
            if cliente.id == id:
                cliente.telefone = valor

    def imprime_lista_cliente(self):
        self.tela_cliente.imprime_lista_cliente(self.clientes)

    def imprime_cliente(self, cliente):
        self.tela_cliente.imprime_cliente(cliente)

    def cliente(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente

    def ultimo_cliente(self):
        return self.__clientes[-1]

    def busca_cliente(self):
        while True:
            id_cliente = self.tela_cliente.escolhe_cliente(self.clientes)
            if id_cliente == 0:
                break
            self.imprime_cliente(self.cliente(id_cliente))

    def escolhe_cliente_cpf(self):
        while True:
            cpf_cliente = self.tela_cliente.escolhe_cliente_cpf(self.clientes)
            if cpf_cliente == 0:
                break
            self.imprime_cliente(self.cliente(cpf_cliente))

    def confirma(self):
        return self.tela_cliente.tela_confirma()

    def abre_tela_inicial(self):
        switcher = {0: self.finaliza,
                    1: self.adiciona_cliente,
                    2: self.remove_cliente,
                    3: self.abre_tela_altera,
                    4: self.busca_cliente,
                    5: self.imprime_lista_cliente}

        while self.mantem_tela_aberta:
            opcao = self.tela_cliente.mostra_tela_opcoes(self.clientes)
            funcao_escolhida = switcher[opcao]()


    def abre_tela_altera(self):
        self.imprime_lista_cliente()
        id = self.tela_cliente.escolhe_cliente(self.clientes)
        switcher = {0: self.abre_tela_inicial,
                        1: self.altera_nome,
                        2: self.altera_cpf,
                        3: self.altera_endereco,
                        4: self.altera_telefone}

        opcao = self.tela_cliente.tela_alterar_opcoes()
        funcao_escolhida = switcher[opcao]
        funcao_escolhida(id)