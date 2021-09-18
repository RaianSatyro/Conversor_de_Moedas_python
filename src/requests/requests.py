import requests
requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()
dolar_in_real = float(cotacao['USD']['bid'])

