from verifica_valores import VerificaValores
from prettytable import PrettyTable

class TelaCategoria:
    def __init__(self):
        self.__verifica_valores = VerificaValores()

    def cria_lista_id(self, categorias: list):
        lista_id = []
        for categoria in categorias:
            lista_id.append(categoria.id)
        return lista_id

    def mostra_tela_opcoes(self):
        print("------ Categorias ------")
        print("1 - Escolher categoria")
        print("2 - Criar nova categoria")
        print("0 - Voltar")
        opcao = self.__verifica_valores.inteiros("Escolha a opção: ", list(range(3)))
        return opcao

    def imprime_lista(self, categorias):
        print("------ Categorias ------")
        t = PrettyTable(['ID', 'Nome'])
        for categoria in categorias:
            t.add_row([categoria.id, categoria.nome])
        print(t)

    def escolhe_categoria(self, categorias):
        lista_id = self.cria_lista_id(categorias)
        id = self.__verifica_valores.inteiros("Digite o id da categoria: ", lista_id, "Valor inválido, insira um ID válido")
        return id

    def adiciona_categoria(self):
        return self.__verifica_valores.texto("Insira o nome da categoria: ")
