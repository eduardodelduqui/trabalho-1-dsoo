from limite.tela import Tela
from verifica_valores import VerificaValores

class TelaMain(Tela):
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    @property
    def verifica_valores(self):
        return self.__verifica_valores

    def mostra_tela_opcoes(self):
        print("-------------- Aplicativo --------------")
        print('Entrar como:')
        print('\033[1;36m1\033[0m - Cliente')
        print('\033[1;36m2\033[0m - Loja')
        print('\033[1;36m3\033[0m - Pedido')
        print('\033[1;91m0\033[0m - Encerrar')
        opcao = self.verifica_valores.inteiros('Escolha a opção: ', list(range(4)))
        return opcao