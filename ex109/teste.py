import moeda

p = float(input('Digite o  preço: R$'))

print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')

print(f'O dobro de R${moeda.moeda(p)} é {moeda.dobro(p, True)}')

print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10, True)}')

print(f'Reduzindo o preço em 13%, temos {moeda.diminuir(p, 13, True)}')
