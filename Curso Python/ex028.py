from random import randint
from time import sleep
c = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
u = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if u < 0 or u > 5:
    print('NÚMERO INVÁLIDO! Escolha um número de 0 a 5')
else:
    if c == u:
        print(f'PARABÉNS! Você conseguiu me vencer!')
    else:
        print(f'GANHEI! Eu pensei no número {c} e não no {u}')
