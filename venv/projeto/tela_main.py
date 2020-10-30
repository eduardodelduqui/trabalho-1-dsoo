from limite.tela import Tela

class TelaMain(Tela):
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
        print("*-------------- Aplicativo --------------")
        print('Entrar como:')
        print('1 - Cliente')
        print('2 - Loja')
        print('0 - Encerrar')
        opcao = self.verifica_numero_inteiro('Escolha a opção: ', [0, 1, 2])
        return opcao