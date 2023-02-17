def area(larg, comp):
    a = larg * comp
    print(f'A largura e um terreno {larg} x {comp} é de {a}m2.')


print('  Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
