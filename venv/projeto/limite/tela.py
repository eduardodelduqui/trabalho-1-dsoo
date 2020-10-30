from abc import ABC, abstractmethod

class Tela(ABC):
    pass


@abstractmethod
def mostra_tela_opcoes(self):
    pass

