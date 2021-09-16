from src.functions.funciton import *

def menu():
    print('''
    #### Conversor de moedas ####

    1 - Dólar americano para Real
    2 - Real para Dólar americano
    3 - Dólar americano para Euro
    4 - Euro para Dólar americano
    
    0 - Sair
    
    #############################
    ''')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        valor1 = float(input('Digite um valor em Dólar: '))
        dolar_to_real(valor1)
        menu()

    elif escolha == '2':
        valor2 = float(input('Digite um valor em Real: '))
        real_to_dolar(valor2)
        menu()

    elif escolha == '3':
        valor3 = float(input('Digite um valor em Dólar: '))
        dolar_to_euro(valor3)
        menu()
    
    elif escolha == '4':
        valor4 = float(input('Digite um valor em Euro: '))
        euro_to_dolar(valor4)
        menu()

    elif escolha == '0':
        print('Saindo...')

    else:
        print('Digite uma opção valida')
        menu()
