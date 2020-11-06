
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

    def cpf(self, mensagem: str = "", lista: list = None):
        while True:
            cpf = input(mensagem)
            soma = 0
            multiplicador = 10
            if cpf.isdigit():
                
                #Validando digito verificador
                valido = False
                
                if len(cpf) == 11:
                
                    for i in range(9):
                        soma += multiplicador*int(cpf[i])
                        multiplicador -=1
                    if soma%11 == 0 or soma%11 == 1:
                        digito1 = 0
                    else:
                        digito1 = 11 - (soma%11)
                    
                    multiplicador = 11
                    soma = 0
                    for i in range(10):
                        if multiplicador == 2:
                            soma += 2*digito1
                        else:
                            soma += multiplicador*int(cpf[i])
                            multiplicador -= 1
                    if soma%11 == 0 or soma%11 == 1:
                        digito2 = 0
                    else:
                        digito2 = 11 - (soma%11)
                    
                    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
                        valido = True
                    #fim vallidação digito verificador
                    
                if cpf.isdigit() and valido:
                    if len(lista) != 0:
                        for cliente in lista:
                            if cpf == cliente.cpf:
                                print('CPF já cadastrado, insira outro CPF')
                                break
                            else:
                                print(lista)
                                return cpf
                    else:
                        return cpf
                    
                else: print('CPF inválido, insira um valor válido')
            
            else:
                print('Valor inválido, insira apenas números')
    
    def altera_cpf(self, mensagem: str = ""):
        while True:
            cpf = input(mensagem)
            soma = 0
            multiplicador = 10
            if cpf.isdigit():
                
                #Validando digito verificador
                valido = False
                
                if len(cpf) == 11:
                
                    for i in range(9):
                        soma += multiplicador*int(cpf[i])
                        multiplicador -=1
                    if soma%11 == 0 or soma%11 == 1:
                        digito1 = 0
                    else:
                        digito1 = 11 - (soma%11)
                    
                    multiplicador = 11
                    soma = 0
                    for i in range(10):
                        if multiplicador == 2:
                            soma += 2*digito1
                        else:
                            soma += multiplicador*int(cpf[i])
                            multiplicador -= 1
                    if soma%11 == 0 or soma%11 == 1:
                        digito2 = 0
                    else:
                        digito2 = 11 - (soma%11)
                    
                    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
                        valido = True
                    #fim vallidação digito verificador
                    
                if cpf.isdigit() and valido:
                    return cpf
                else:
                    print('CPF inválido, insira um valor válido')
            
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


