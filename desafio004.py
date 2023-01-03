algo = input('Digite algo: ')
print(f'Tipo: {type(algo)}\n'
      f'Número: {algo.isnumeric()}\n'
      f'Alphanúmrico: {algo.isalnum()}\n'
      f'Alphabetico: {algo.isalpha()}\n'
      f'Decimal: {algo.isdecimal()}\n'
      f'Maiusculo: {algo.isupper()}\n'
      f'Minusculo: {algo.islower()}\n'
      f'Tem espaço: {algo.isspace()}\n')
