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
        print('1 - Cliente')
        print('2 - Loja')
        print('3 - Pedido')
        print('0 - Encerrar')
        opcao = self.verifica_valores.inteiros('Escolha a opção: ', list(range(4)))
        return opcao