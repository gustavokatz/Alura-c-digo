#from googlesearch import search
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



#list_of_queries = lista2
#results = []
#
#for query in list_of_queries:
#    results.append(search(query, tld="co.in", num=10, stop=1, pause=2))

#
#print(results)






