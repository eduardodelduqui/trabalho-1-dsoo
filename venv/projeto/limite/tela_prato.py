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
        print("*-------------- Loja --------------")
        print('1 - Adicionar prato')
        print('2 - Remover prato')
        print('3 - Listar pratos')
        print('0 - Voltar')
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

