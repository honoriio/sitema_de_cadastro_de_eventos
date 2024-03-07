# Local reservado para fazer importações 
import requests

# Função criada para a consulta de cep usando a api viacep
def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
# Função criada para a impreção das informações obtidas pela api viacep
def imprimir_informacoes_cep(cep):
    cep_info = consulta_cep(cep)
    if cep_info:
        print("CEP encontrado:")
        for key, value in cep_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("CEP não encontrado.")
