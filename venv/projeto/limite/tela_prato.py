from prettytable import PrettyTable


class TelaPrato:
    def __init__(self):
        pass

    def verifica_numero_inteiro(self, mensagem: str = "", valores_validos: [] = None):
        while True:
            try:
                opcao = int(input('Escolha a Opção: '))
                if (opcao in valores_validos):
                    return opcao
                else:
                    print('Valor inválido, insira o número ao lado da opção desejada')
            except ValueError:
                print('Valor inválido, valor precisa ser inteiro')

    def mostra_tela_opcoes(self):
        print("-------------- Loja --------------")
        print('\033[1;36m1\033[0m - Adicionar prato')
        print('\033[1;36m2\033[0m - Remover prato')
        print('\033[1;36m3\033[0m - Listar pratos')
        print('\033[1;91m0\033[0m - Voltar')
        opcao = self.verifica_numero_inteiro('Escolha a opção: ', [0, 1, 2, 3])
        return opcao

    def abre_tela_adicionar(self):
        nome = input('Digite o nome da prato: ')
        tipo = input('Digite a categoria da prato: ')
        prato = {
            "nome": nome,
            "tipo": tipo
        }
        return prato

    def remove_prato(self):
        return int(input('Insira o ID do prato a ser removido: '))

    def imprime_lista_prato(self, pratos):
        if(pratos):
            print('----------- Pratos -----------')
            t = PrettyTable(['ID', 'Nome', 'Tipo', 'Preço'])
            for prato in pratos:
                t.add_row([prato.id, prato.nome, prato.tipo, 'R$ ' + prato.preco_unitario])
            print(t)
        else:
            print('\033[1;31m!!! Lista de pratos vazia!!!\033[0m')



