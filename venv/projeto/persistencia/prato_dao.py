from persistencia.abstract_dao import AbstractDAO
from entidade.prato import Prato

class PratoDAO(AbstractDAO):
    def __init__(self):
        super().__init__('pratos.pkl')

    def add(self, prato: Prato):
        print(prato)
        if ((prato is not None) and (isinstance(prato, Prato)) and (isinstance(prato.id, str))):
            print('adicionando')
            super().add(prato.id, prato)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            super().remove(key)