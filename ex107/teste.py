from ex107 import moeda

p = float(input('Digite o  preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
