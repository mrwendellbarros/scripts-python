n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}\n'
      f'Seu último nome é {nome[len(nome)-1]}')