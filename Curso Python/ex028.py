import random

n = random.randint(0, 5)
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Vou pensar em número entre 0 e 5. Tente advinhar...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
u = int(input('Em que número eu pensei? '))
print('Processando...')
if u < 0 or u > 5:
    print('NÚMERO INVÁLIDO! Escolha um número de 0 a 5')
else:
    if n == u:
        print(f'PARABÉNS! Você conseguiu me vencer!')
    else:
        print(f'GANHEI! Eu pensei no número {n} e não no {u}')
