import random

n = random.randint(0, 5)
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= \n
Vou pensar em número entre 0 e 5. Tente advinhar...\n
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
u = int(input('Em que número eu pensei? '))
u = int(input('Escolha um número de 0 a 5: '))
if u < 0 or u > 5:
    print('NÚMERO INVÁLIDO! Escolha um número de 0 a 5')
else:
    print(f'O computador escolheu: {n}')
    if n == u:
        print('Você Venceu!')
    else:
        print('Você Perdeu!')
