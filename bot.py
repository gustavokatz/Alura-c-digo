# Para que o código funcione correntamente, favor instalar as bibliotecas 'beautifulsoup4' e 'google'.
# Para as instalar, basta digitar pip install (biblioteca)


# Adiquirição de informação
from googlesearch import search
print ('Olá, bem vindo ao Bot Vtex\n')
nome = input('Como você gostaria de ser chamado?\n')
residencia = input(f'Certo, {nome}, em que cidade você mora?\n')
preparo = input(f'Muito bem {nome}, já decidiu o que vai querer pedir?\n')

# Criação da lista de compra
while preparo.lower() == 'sim':
    lista2 = input('Quais itens gostaria de colocar no carrinho?\n')
    lista2 = lista2.split(',')
    preparo = input(f'muito bem, essa é sua lista até o momento: {lista2}, gostaria de pedir algo a mais?\n')
    while preparo.lower() == 'sim':
        lista2 = input(f'Quais outros itens gostaria alem de {lista2}\n').split(',') + lista2 
        preparo = input('quer continuar sua compra?\n')
print(f'Muito bem, vou finalizar sua compra, sua lista é {lista2}')

# Correção da lista para obter itens compraveis relacionados a Vtex e a residência
i=0
while i < len(lista2):
    lista2[i]= 'comprar ' + lista2[i] + ' Vtex ' +  residencia
    i+=1

# Pesquisa da lista no Google
i=0
while i < len(lista2):
    query = lista2[i]
    i+=1
    for j in search(query, tld="co.in", num=3, stop=3, pause=2, lang = 'pt'):
        print(j)
