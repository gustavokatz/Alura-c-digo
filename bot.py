from googlesearch import search
print ('\tOlá, bem vindo ao Bot Vtex\n')

nome = input('Como você gostaria de ser chamado?\n')
preparo = input(f'Muito bem {nome}, já decidiu o que vai querer pedir?\n')
while preparo.lower() == 'sim':
    lista2 = input('Quais itens gostaria de colocar no carrinho?\n')
    lista2 = lista2.split(',')
    preparo = input(f'muito bem, essa é sua lista até o momento: {lista2}, gostaria de pedir algo a mais?\n')
    while preparo.lower() == 'sim':
        lista2 = input(f'Quais outros itens gostaria alem de {lista2}\n').split(',') + lista2 
        preparo = input('quer continuar sua compra?\n')
    
print(f'Muito bem, vou finalizar sua compra, sua lista é {lista2}')


i=0
while i < len(lista2):
    lista2[i]= 'comprar ' + lista2[i] + 'Vtex ' 
    i+=1

i=0
while i < len(lista2):
    query = lista2[i]
    i+=1
    for j in search(query, tld="co.in", num=4, stop=4, pause=2, lang = 'pt'):
        print(j)






