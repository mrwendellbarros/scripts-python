c = ('\033[m',
     '\033[0;30;41m');


def ajuda(com):
    título(f'Acessando o manual do comando {com}', 1)
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')

comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
