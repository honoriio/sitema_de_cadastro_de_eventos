# Este e um local especifico para a criação de validações para o cadastramento dos eventos.

# Este local e destinado as importações necessarias.
import charset_normalizer
import unidecode

# Criamos essa função para a validação do campo titulo ou algum campo que necessite dessa validação em espesifico.
def validar_titulo(titulo):
    titulo_sem_acentos = unidecode.unidecode(titulo)

    # Não esquecer de deixar o espaço para que não tenha problema com a validação do nome completo
    caracteres_permitidos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ^~´áéíóúÁÉÍÓÚ1234567890 ")
    return set(titulo_sem_acentos).issubset(caracteres_permitidos)


def validar_estado(estado):
    titulo_sem_acentos = unidecode.unidecode(estado)

    # Não esquecer de deixar o espaço para que não tenha problema com a validação do nome completo
    caracteres_permitidos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ^~´áéíóúÁÉÍÓÚ ")
    return set(titulo_sem_acentos).issubset(caracteres_permitidos)


# Função criada para validar cep e garantir que o usuario informe a quantia correta de digitos, que nesse caso são 8 digitos numericos.
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


# Função criada para a validação da hora para que o usuario não informe um horario incorreto. 
def validar_hora(hora_evento):
    caracteres_permitidos = set("1234567890:")
    if all(char in caracteres_permitidos for char in hora_evento):
        tam_hora = 5
        tam_hora_evento = len(hora_evento)
        if tam_hora_evento == tam_hora:
            return True
        else:
            print('A hora informada e invalida. Por favor, insira um horario vãlido.')
    else:
        print('A hora informada contem caracteres não permitidos. Por favor, insíra apenas o formato permitido (HH:MM)')
    return False


# Função criada para a validaçao do número de telefone, o mesmo verifica a quantia de numeros ddd e sulfixo do pais. 
def validar_telefone(celular):
    caracteres_permitidos = set("1234567890")
    if all(char in caracteres_permitidos for char in celular):
        tam_celular = 11
        tam_celular_usuario = len(celular)
        if tam_celular_usuario == tam_celular:
            return True
        else:
            print('O número informado é inválido. Por favor, insira um número válido.')
    else:
        print('O número informada contém caracteres não permitidos. Por favor, insira apenas números, sem barra, aspas ou ponto de separação.')
    return False


# Função criada pra verificar e validar valores monetarios inseridos pelo usuario.
def validar_valores_monetarios(custo):
    caracteres_permitidos = set("1234567890.,")
    if all(char in caracteres_permitidos for char in custo):
        tam_custo = 15
        tam_custo_evento = len(custo)
        if tam_custo_evento <= tam_custo:
            return True
        else: 
            print('O valor informado excede o tamanho maximo permitido.')
    else:
        print('O valor informado contem caracteres não permitidos, por favor, insira valores validos.')
    return False
