num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}\n'
      f'Unidade: {u}\n'
      f'Dezena: {d}\n'
      f'Centena: {c}\n'
      f'Milhar: {m}\n')