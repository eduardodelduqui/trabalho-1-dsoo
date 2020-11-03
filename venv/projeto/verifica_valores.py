
class VerificaValores:
    def __init__(self):
        pass

    def texto(self, mensagem: str = ""):
        texto = input(mensagem)
        texto = texto.split()
        texto_tratado = []
        for trecho in texto:
            texto_tratado.append(trecho.capitalize())
        return ' '.join(texto_tratado)

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

    def cpf(self, mensagem: str = ""):
        while True:
            try:
                cpf = int(input(mensagem))
                if len(str(cpf)) == 11:
                    return self.retorna_cpf_tratado(cpf)
                else:
                    print('CPF inválido, insira um valor válido')
            except ValueError:
                print('Valor inválido, insira apenas números')

    def retorna_cpf_tratado(self, cpf: int):
        cpf_tratado = ''
        cpf = list(str(cpf))
        for index, digito in enumerate(cpf):
            cpf_tratado += digito
            if index == 2 or index == 5:
                cpf_tratado += '.'
            if index == 8:
                cpf_tratado += '-'
        return cpf_tratado



