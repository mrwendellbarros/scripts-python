listagem = []
mai = 0
men = 0
for c in range(0, 5):
    listagem.append(int(input(f'digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men =listagem[c]
    else:
        if listagem[c] > mai:
            mai = listagem[c]
        if listagem[c] < men:
            men = listagem[c]
print('=-'*30)
for i, v in enumerate(listagem):
    if v == mai:
        pmai = i
for i, v in enumerate(listagem):
    if v == men:
        pmen = i
print(f'Você digitou os valores {listagem}\n'
      f'O maior valor digitado foi {mai} nas posições {pmai}\n'
      f'O menor valor digitado foi {men} nas posições {pmen}')