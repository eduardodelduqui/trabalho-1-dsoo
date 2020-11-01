from prettytable import PrettyTable

class TelaPedido:
    def __init__(self):
        pass

    def verifica_numero_inteiro(self, mensagem: str, valores):
        while True:
            try:
                opcao = int(input(mensagem))
                if opcao in valores:
                    return opcao
                else:
                    print("Não existe ID, insira um ID existente")
            except:
                print("Insira um valor inteiro")


    def pega_id_lista(self, pratos: list):
        lista = []
        for prato in pratos:
            lista.append(prato.id)
        return lista

    def imprime_pedido(self, pedido):
        cliente = pedido.cliente
        produtos = pedido.produtos
        t_cliente = PrettyTable(['ID', 'Nome', 'CPF'])
        t_cliente.add_row([cliente.id, cliente.nome, cliente.cpf])
        t_cliente.border = False
        t_produtos = PrettyTable(['ID', 'Produto', 'Qtd.', 'Preço unitário' ])
        t_produtos.border = False
        for produto in produtos:
            qtd = produto["qtd"]
            produto = produto["item"]
            t_produtos.add_row([produto.id, produto.nome, qtd, f'{produto.preco_unitario:.2f}'])
        tabela = PrettyTable(['NOTA FISCAL'])
        t_header = PrettyTable(['COD.', 'DATA', 'HORARIO'])
        t_header.header = False
        t_header.border = False
        t_header.add_row(['COD. '+pedido.codigo, 'DATA: '+str(pedido.data), 'HORARIO: '+pedido.horario])
        tabela.add_row([t_header])
        tabela.add_row(['----------- Cliente -----------'])
        tabela.add_row([t_cliente])
        tabela.add_row(['------------ Itens ------------'])
        tabela.add_row([t_produtos])
        tabela.add_row(['-------------------------------'])
        t_footer = PrettyTable(['VALOR TOTAL', 'PAGO'])
        t_footer.header = False
        t_footer.border = False
        if pedido.pago:
            pago = 'PAGO'
        else: pago = 'A PAGAR'
        t_footer.add_row(['Valor total: R$ '+f'{pedido.valor_total:.2f}', pago])
        tabela.add_row([t_footer])
        print(tabela)

    def mostra_tela_opcoes(self):
        print("------- Pedido -------")
        print("1 - Escolher pedido")
        print("2 - Histórico de pedidos")
        print("0 - Voltar")
        return self.verifica_numero_inteiro("Escolha a opção: ", [0, 1 , 2])

    def escolhe_prato(self, pratos):
        lista_compras = []
        id_pratos = self.pega_id_lista(pratos)
        while True:
            id = self.verifica_numero_inteiro("Escolha o prato: ", id_pratos)
            qtd = self.verifica_numero_inteiro("Escolha a quantidade: ", list(range(100)))
            compra = {"id": id, "qtd": qtd}
            lista_compras.append(compra)
            if input("Deseja continuar a compra? [S/N]") == "N":
                return lista_compras

    def escolhe_cliente(self, clientes):
        id_clientes = self.pega_id_lista(clientes)
        return self.verifica_numero_inteiro("Escolha o cliente: ", id_clientes)

