dias = int(input('Quantod dias alugados? '))
km = float(input('quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')