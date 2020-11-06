from prettytable import PrettyTable
from verifica_valores import VerificaValores

class TelaPedido:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    @property
    def verifica_valores(self):
        return self.__verifica_valores

    def pega_id_lista(self, pratos: list):
        lista = []
        for prato in pratos:
            lista.append(prato.id)
        return lista

    def imprime_pedido(self, pedido):
        if pedido:
            produtos = pedido.produtos
            t_produtos = PrettyTable(['ID', 'Produto', 'Qtd.', 'Preço unitário' ], border=False)
            for produto in produtos:
                qtd = produto["qtd"]
                produto = produto["item"]
                t_produtos.add_row([produto.id, produto.nome, qtd, f'{produto.preco_unitario:.2f}'])
            tabela = PrettyTable(['NOTA FISCAL'])
            t_cod = PrettyTable(['COD. '], border=False, header=False)
            t_cod.add_row(['COD. '+pedido.codigo])
            t_header = PrettyTable(['DATA', 'HORARIO'], border=False, header=False)
            t_header.add_row(['DATA: '+str(pedido.data), 'HORARIO: '+pedido.horario])
            tabela.add_row([t_cod])
            tabela.add_row([t_header])
            if pedido.cliente:
                cliente = pedido.cliente
                t_cliente = PrettyTable(['ID', 'Nome', 'CPF'], border=False)
                cliente_cpf = self.verifica_valores.cpf_tratado(cliente.cpf)
                t_cliente.add_row([cliente.id, cliente.nome, cliente_cpf])
                tabela.add_row(['----------- Cliente -----------'])
                tabela.add_row([t_cliente])
            else:
                tabela.add_row(['Cliente não cadastrado'])
            tabela.add_row(['------------ Itens ------------'])
            tabela.add_row([t_produtos])
            tabela.add_row(['-------------------------------'])
            t_footer = PrettyTable(['VALOR TOTAL', 'PAGO'], header=False, border=False)
            if pedido.pago:
                pago = 'PAGO'
            else: pago = 'A PAGAR'
            t_footer.add_row(['Valor total: R$ '+f'{pedido.valor_total:.2f}', pago])
            tabela.add_row([t_footer])
            print(tabela)
        else:
            print('LISTA VAZIA')

    def mostra_tela_opcoes(self):
        print("------- Pedido -------")
        print("\033[1;36m1\033[0m - Efetuar pedido")
        print("\033[1;36m2\033[0m - Histórico de pedidos")
        print("\033[1;91m0\033[0m - Voltar")
        return self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))

    def mostra_tela_historico(self):
        print("------ Histórico ------")
        print("\033[1;36m1\033[0m - Desde o início")
        print("\033[1;36m2\033[0m - Últimos")
        print("\033[1;91m0\033[0m - Voltar")
        return self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))

    def mostra_tela_opcoes_cliente(self, clientes):
        print("------ Adicionar Cliente ------")
        print("\033[1;36m1\033[0m - Não adicionar cliente")
        print("\033[1;36m2\033[0m - Cliente não cadastrado")
        if clientes:
            print("\033[1;36m3\033[0m - Cliente cadastrado")
        print("\033[1;91m0\033[0m - Cancelar compra")
        if clientes: return self.verifica_valores.inteiros("Escolha a opção: ", list(range(4)))
        else: return self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))

    def confirma_pedido(self):
        print("------ Confirmar Pedido ------")
        print("\033[1;36m1\033[0m - Confirmar")
        print("\033[1;36m2\033[0m - Alterar pedido")
        print("\033[1;36m3\033[0m - Cancelar pedido")
        print("\033[1;91m0\033[0m - Voltar")
        return self.__verifica_valores.inteiros("Escolha a opçao: ", list(range(4)))

    def escolhe_prato(self, pratos):
        lista_compras = []
        id_pratos = self.pega_id_lista(pratos)
        while True:
            id = self.__verifica_valores.inteiros("Escolha o prato: ", id_pratos)
            qtd = self.__verifica_valores.inteiros("Escolha a quantidade: ", list(range(99)), 'Valor inválido, não é possível comprar mais de 100 itens')
            if qtd != 0:
                compra = {"id": id, "qtd": qtd}
                lista_compras.append(compra)
            if self.__verifica_valores.sim_ou_nao("Deseja continuar a compra? [S/N]", ) == "n":
                return lista_compras

    def escolhe_cliente(self, clientes):
        id_clientes = self.pega_id_lista(clientes)
        return self.__verifica_valores.inteiros("Escolha o cliente: ", id_clientes)


