
def leiaInt(msg):
    while True:
        try:
            n  = int(input(msg))
        except (ValueError, TypeError):
            print('por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu nãodigitar esse número.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')