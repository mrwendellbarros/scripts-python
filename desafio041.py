from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: mirim')
elif idade <= 14:
    print('Classificação: infantil')
elif idade <= 19:
    print('Classificação: junior')
elif idade <= 25:
    print('Classificação: sênior')
else:
    print('Classificação: master')