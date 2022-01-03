import random

n = random.randint(0, 5)
print('-------Jogo de Advinhação-------')
print("""Nesse jogo, você ganha se escolher o mesmo número que o computador \nVamos Começar!""")
u = int(input('Escolha um número de 0 a 5: '))
if u < 0 or u > 5:
    print('NÚMERO INVÁLIDO! Escolha um número de 0 a 5')
else:
    print(f'O computador escolheu: {n}')
    if n == u:
        print('Você Venceu!')
    else:
        print('Você Perdeu!')
