import moeda
preco= float(input('Digite o preço:'))
print(f'a metade de {preco} é {moeda.metade(preco)}')
print(f'o dobro de {preco} é {moeda.dobro(preco)}')
print(f'o aumento de 10% de {preco} é {moeda.aumento(preco, 10)}')
print(f'o desconto de 10% de {preco} é {moeda.desconto(preco,10)}')

