nome = str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome...\n'
      f'Seu nome em maiúscula é {nome.upper()}\n'
      f'Seu nome em minúsculo é {nome.lower()}\n'
      f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras\n'
      f'Seu primeiro nome tem {nome.find(" ")} letras')
