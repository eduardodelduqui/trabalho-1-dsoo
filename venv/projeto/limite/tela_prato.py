from prettytable import PrettyTable
from verifica_valores import VerificaValores

class TelaPrato:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    def cria_lista_id(self, pratos: list):
        lista_id = []
        for prato in pratos:
            lista_id.append(prato.id)
        return lista_id

    def mostra_tela_opcoes(self, pratos):
        print("-------------- Loja --------------")
        print('\033[1;36m1\033[0m - Adicionar prato')
        if pratos:
            print('\033[1;36m2\033[0m - Remover prato')
            print('\033[1;36m3\033[0m - Alterar prato')
            print('\033[1;36m4\033[0m - Listar pratos')
        print('\033[1;91m0\033[0m - Voltar')

        opcao = self.__verifica_valores.inteiros('Escolha a opção: ', list(range(5)))
        return opcao

    def abre_tela_adicionar(self):
        nome = self.__verifica_valores.texto('Digite o nome da prato: ')
        preco = self.__verifica_valores.float('Digite o preço do prato: ')
        preco = round(preco, 2)
        prato = {
            "nome": nome,
            "preco": preco
        }
        return prato

    def remove_prato(self):
        return self.__verifica_valores.inteiros('Insira o ID do prato a ser removido: ')

    def imprime_lista_prato(self, pratos):
        if(pratos):
            print('----------- Pratos -----------')
            t = PrettyTable(['ID', 'Nome', 'Tipo', 'Preço'])
            for prato in pratos:
                t.add_row([prato.id, prato.nome, prato.tipo.nome, 'R$ ' + f'{prato.preco_unitario:.2f}'])
            print(t)
        else:
            print('\033[1;31m!!! Lista de pratos vazia!!!\033[0m')

    def tela_alterar(self):
        print('------ Alterar ------')
        print('1 - Nome')
        print('2 - Categoria')
        print('3 - Preço')
        print('0 - Voltar')
        opcao = self.__verifica_valores.inteiros('Digite a opção que deseja alterar: ')
        return opcao

    def altera_nome(self):
        return self.__verifica_valores.texto('Alterar nome para: ')

    def altera_preco(self):
        return self.__verifica_valores.float('Alterar preço para: ')

    def tela_altera_categoria(self):
        print("------ Categorias ------")
        print("1 - Escolher categoria")
        print("2 - Criar nova categoria")
        opcao = self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))
        return opcao

    def escolhe_prato(self, pratos):
        id_pratos = self.cria_lista_id(pratos)
        return self.__verifica_valores.inteiros("Insira o ID do prato: ", id_pratos, "Valor inválido, insira um ID válido")



