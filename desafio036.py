casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacão = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos\n'
      f'a prestação será de R${prestacão:.2f}')
if prestacão <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')