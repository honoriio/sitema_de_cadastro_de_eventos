from modulos.interface.elemento import *


linha_dupla()
print('EVENTHUB v-0.1.2'.center(82))
linha_dupla()
print('MENU'.center(82))
linha_dupla()

print('[1]- Cadastrar um novo usuário.')
print('[2]- Cadastrar um novo evento.')
print('[3]- Vizualizar usúarios')
print('[4]- vizualizar eventos')
linha()
resp = input('Opção: ')
linha()

if resp == '1':  # Corrigido: comparando com strings '1' e '2'
    from modulos.database.data_base import BancoDeDados
    bd = BancoDeDados()
elif resp == '2':
    from modulos.funcoes_eventos import *
    from modulos.database.data_base_eventos import BancoDeDadosEventos
    from modulos.funcoes import *
    bd = BancoDeDadosEventos()
    linha()
elif resp == '3':
    from modulos.database.print_data_base_usuarios import PrintBancoDeDadosUsuarios
    PrintBancoDeDadosUsuarios()
    linha()
elif resp == '4':
    from modulos.database.print_data_base_eventos import PrintBancoDeDadosEventos
    PrintBancoDeDadosEventos()
    linha()
    




# Campo de mudanças.

# Preciso melhorar isso, criar alguma apresentação para o programa e melhorar a logica da validação das opções 
# Preciso deixar o mais limpo visualmente possivel sem deixar de ser funcional 


# Preciso criar a funçao de banco de dados para os eventos, acho que vou fazer algo igual no banco de dados dos cadastros dos usuarios.