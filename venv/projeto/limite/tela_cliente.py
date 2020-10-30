
class TelaCliente:
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
        print("*-------------- Cliente --------------")
        print('1 - Adicionar')
        print('2 - Remover')
        print('3 - Listar')
        print('0 - Encerrar')
        opcao = self.verifica_numero_inteiro('Escolha a opção: ', [0, 1, 2, 3])
        return opcao

    def opcoes_adicionar(self):
        nome = input('Digite o nome do cliente: ')
        cpf = input('Digite o cpf do cliente: ')
        cliente = {
            "nome": nome,
            "cpf": cpf
        }
        return cliente

    def tela_remover(self):
        return input('Digite o cpf do cliente a ser removido: ')


