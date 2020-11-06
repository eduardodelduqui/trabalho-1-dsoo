
class VerificaValores:
    def __init__(self):
        pass

    def texto(self, mensagem: str = "", mensagem_erro: str = "", especiais: bool = False, numeros: bool = False):
        invalidos = ''
        if especiais == False:
            invalidos += "@#$%¨&*()_-+={[}]?/:;><,.|¹²³£¢¬`´~^°ºª"
        if numeros == False:
            invalidos += '0123456789'
        while True:
            texto = input(mensagem)
            if not self.verifica_caracteres(texto, invalidos):
                texto = texto.split()
                texto_tratado = []
                for trecho in texto:
                    texto_tratado.append(trecho.capitalize())
                return ' '.join(texto_tratado)
            else:
                print(mensagem_erro)

    def verifica_caracteres(self, texto, caracteres):
        for caracter in caracteres:
            if caracter in texto:
                return True
            else: return False

    def sim_ou_nao(self, mensagem: str = ""):
        valores_validos = ['s', 'n']
        while True:
            opcao = input(mensagem).lower()
            if opcao in valores_validos:
                return opcao
            else:
                print('Valor inválido, insira S ou N')

    def inteiros(self, mensagem: str = "", valores_validos: list = None, mensagem_erro: str = "Valor inválido, insira o número ao lado da opção desejada"):
        while True:
            try:
                opcao = int(input(mensagem))
                if(valores_validos):
                    if isinstance(valores_validos, list):
                        if (opcao in valores_validos):
                            return opcao
                        else:
                            print(mensagem_erro)
                    else:
                        raise TypeError('valores_validos precisa ser do tipo List')
                else:
                    return opcao
            except ValueError:
                print('Valor inválido, insira apenas número')

    def float(self, mensagem: str = ""):
        while True:
            try:
                return float(input(mensagem))
            except ValueError:
                print('Valor inválido, valor não pode ser um texto')

    def cpf(self, mensagem: str = "", lista: list = []):
        while True:
            cpf = input(mensagem)
            if cpf.isdigit():
                if len(cpf) == 11 and cpf.isdigit():
                    if self.verifica_cpf(cpf, lista):
                        return cpf
                else: print('CPF inválido, insira um valor válido')
            else:
                print('Valor inválido, insira apenas números')

    def cpf_tratado(self, cpf: str):
        cpf_tratado = ''
        for index, digito in enumerate(cpf):
            cpf_tratado += digito
            if index == 2 or index == 5:
                cpf_tratado += '.'
            if index == 8:
                cpf_tratado += '-'
        return cpf_tratado

    def verifica_cpf(self, cpf, lista):
        for item in lista:
            if cpf == item.cpf:
                print('CPF já cadastrado, insira outro CPF')
                return False
        return True

    def telefone(self, mensagem: str = ""):
        while True:
            try:
                telefone = int(input(mensagem))
                if len(str(telefone)) == 10 or len(str(telefone)) == 11:
                    return telefone
                else:
                    print('Valor inválido, insira um número de telefone válido')
            except ValueError:
                print('Valor inválido, insira apenas números')

    def telefone_tratado(self, telefone: int):
        telefone_tratado = '('
        telefone = str(telefone)
        for index, digito in enumerate(telefone):
            telefone_tratado += digito
            if index == 1:
                telefone_tratado += ')'
            if index == 6:
                telefone_tratado += '-'
        return telefone_tratado




