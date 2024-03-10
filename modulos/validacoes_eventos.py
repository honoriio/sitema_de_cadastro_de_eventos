# Este e um local especifico para a criação de validações para o cadastramento dos eventos.

# Este local e destinado as importações necessarias.
import unidecode

# Criamos essa função para a validação do campo titulo ou algum campo que necessite dessa validação em espesifico.
def validar_titulo(titulo):
    titulo_sem_acentos = unidecode.unidecode(titulo)

    # Não esquecer de deixar o espaço para que não tenha problema com a validação do nome completo
    caracteres_permitidos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ^~´áéíóúÁÉÍÓÚ1234567890 ")
    return set(titulo_sem_acentos).issubset(caracteres_permitidos)


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
