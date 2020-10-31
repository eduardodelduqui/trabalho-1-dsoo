
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


    def pega_id_pratos(self, pratos: list):
        lista = []
        for prato in pratos:
            lista.append(prato.id)
        return lista




    def mostra_tela_opcoes(self):
        print("------- Pedido -------")
        print("1 - Escolher prato: ")
        print("0 - Voltar")
        return self.verifica_numero_inteiro("Escolha a opção: ", [0, 1])

    def escolhe_pedido(self, pratos):
        idPratos = self.pega_id_pratos(pratos)
        return self.verifica_numero_inteiro("Escolha a opção: ", idPratos)

