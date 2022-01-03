cores = {"limpa": '\033[m',
         "roxo": '\033[35m',
         "azul": '\033[36m'}
n = int(input(f'{cores["roxo"]}Me diga um número qualquer: '))
if n % 2 == 1:
    print(f'\033[mO número {n} é {cores["azul"]}ÍMPAR')
else:
    print(f'\033[mO número {n} é {cores["azul"]}PAR')
