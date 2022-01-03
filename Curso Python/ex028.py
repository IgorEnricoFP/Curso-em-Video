from random import randint
from time import sleep
c = randint(0, 5)
print("\033[33m-=-\033[m" * 20)
print('\033[mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print("\033[33m-=-\033[m" * 20)
u = int(input('Em que número eu pensei? '))
print('\033[mPROCESSANDO...')
sleep(2)
if u < 0 or u > 5:
    print('\033[31mNÚMERO INVÁLIDO!\033[m Escolha um número de 0 a 5')
else:
    if c == u:
        print(f'\033[32mPARABÉNS! Você conseguiu me vencer!')
    else:
        print(f'GANHEI! Eu pensei no número {c} e não no {u}')
