from src.requests.requests import dolar_in_real


#Função que converte dolar para real
def dolar_to_real(dolar):
    real = dolar * dolar_in_real
    print(f'''
    ${dolar :.2f} = Dólar americano
    R${real :.2f} = Real
    ''')

#Função que converte real para dolar
def real_to_dolar(real):
    dolar = real / dolar_in_real
    print(f'''
    R${real :.2f} = Real
    ${dolar :.2f} = Dólar
    ''')

#Função que converte dolar para euro
def dolar_to_euro(dolar):
    euro = dolar * 0.85
    print(f'''
    ${dolar :.2f} = Dólar americano
    €{euro :.2f} = Euro
    ''')

#Função que converte euro para dolar
def euro_to_dolar(euro):
    dolar = euro * 1.18
    print(f'''
    €{euro :.2f} = Euro
    ${dolar :.2f} = Dólar americano
    ''')