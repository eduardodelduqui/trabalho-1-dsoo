from verifica_valores import VerificaValores
from prettytable import PrettyTable

class TelaCategoria:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    @property
    def verifica_valores(self):
        return self.__verifica_valores

    def cria_lista_id(self, categorias: list):
        lista_id = [0]
        for categoria in categorias:
            lista_id.append(categoria.id)
        return lista_id

    def mostra_tela_opcoes(self, categorias):
        print("------ Categorias ------")
        print("1 - Criar nova categoria")
        if categorias:
            print("2 - Escolher categoria")
            opcao = self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))
        else:
            opcao = self.verifica_valores.inteiros("Escolha a opção: ", list(range(2)))
        return opcao

    def imprime_lista(self, categorias):
        if categorias:
            print("------ Categorias ------")
            t = PrettyTable(['ID', 'Nome'])
            for categoria in categorias:
                t.add_row([categoria.id, categoria.nome])
            print(t)
        else:
            print('\033[1;31m!!! Lista de categorias vazia !!!\033[0m')


    def escolhe_categoria(self, categorias):
        lista_id = self.cria_lista_id(categorias)
        id = self.__verifica_valores.inteiros("Digite o id da categoria: ", lista_id, "Valor inválido, insira um ID válido")
        return id

    def adiciona_categoria(self):
        return self.__verifica_valores.texto("Insira o nome da categoria: ")
