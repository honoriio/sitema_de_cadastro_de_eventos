# esté e um local especifico para crir as funcoes de validaçoes

# Importando os modulos necessarios


# Importamos a biblioteca unidecode, que permite a remoção de acentos em strings,
# sendo útil para a função de validação de nomes fornecidos pelos usuários.
import unidecode
import re


# Aqui criamos uma função para validar a entrada de nomes, onde so e permitido a entrada somente de letras e acentos usados na lingua portuguesa.
# Essa função podera ser usada posteriromente em validações de outros campos além de nomes de usuario, como nomes de cidades, nomes de ruas etc.


def validar_nome(nome):
    nome_sem_acentos = unidecode.unidecode(nome)

    # Não esquecer de deixar o espaço para que não tenha problema com a validação do nome completo
    caracteres_permitidos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ^~´áéíóúÁÉÍÓÚ ")
    return set(nome_sem_acentos).issubset(caracteres_permitidos)


# Validação para verificar se o valor inserido e inteiro  de forma correta
def leiaint(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido.\033[0m')
        except KeyboardInterrupt:
            print('O usuário decidiu não informar mais o número.')
            return 0
        else:
            return inteiro


# Função criada para validar a entrada da data, dando a possibilidade do usuário já inserir a data formatada (com a barra separadora)
def validar_data(data):
    caracteres_permitidos = set("1234567890/")
    if all(char in caracteres_permitidos for char in data):
        tam_data = 10
        tam_data_usuario = len(data)
        if tam_data_usuario == tam_data:
            return True
        else:
            print('A data informada é inválida. Por favor, insira um valor válido.')
    else:
        print('A data informada contém caracteres não permitidos. Por favor, insira apenas números e a barra de separação.')
    return False



# Função criada para validar a entrada do campo email.
def validar_email(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    #Verifica se o email corresponde ao padrão 
    if re.match(padrao, email):
        return True
    else:
        return False
    
    
# Validação para verificar se o valor inserido e inteiro  de forma correta
def leiaint(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido.\033[0m')
        except KeyboardInterrupt:
            print('O usuário decidiu não informar mais o número.')
            return None
        else:
            return inteiro


# Função criada para validar cep e garantir que o usuario informe a quantia correta de digitos.
def validar_cep(cep):
    caracteres_permitidos = set("1234567890")
    if all(char in caracteres_permitidos for char in cep):
        tam_cep = 8
        tam_cep_usuario = len(cep)
        if tam_cep_usuario == tam_cep:
            return True
        else:
            print('A CEP informado é inválido. Por favor, insira um valor válido.')
    else:
        print('A CEP informada contém caracteres não permitidos. Por favor, insira apenas números, sem barra ou ponto de separação.')
    return False