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
            t_cliente.add_row([cliente.id, cliente.nome, cliente.cpf])
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

    def mostra_tela_opcoes(self):
        print("------- Pedido -------")
        print("1 - Escolher pedido")
        print("2 - Histórico de pedidos")
        print("0 - Voltar")

        return self.verifica_numero_inteiro("Escolha a opção: ", [0, 1 , 2])

    def mostra_tela_opcoes_cliente(self):
        print("------ Adicionar Cliente ------")
        print("1 - Finalizar")
        print("2 - Cliente não cadastrado")
        print("3 - Cliente cadastrado")

        return self.verifica_numero_inteiro("Escolha a opção: ", [0, 1, 2, 3])

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

