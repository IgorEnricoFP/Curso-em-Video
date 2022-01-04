cores = {"azul": '\033[36m',
         "vermelho": '\033[31m',
         "normal": '\033[m'}
sal1 = float(input('Qual é o salário do funcionário? R$'))
sal2 = sal1 * (10 / 100)
if sal1 <= 1250:
    sal2 = sal1 + (sal1 * 15 / 100)
else:
    sal2 = sal1 + (sal1 * 10 / 100)
print(f'Quem ganhava {cores["vermelho"]}R${sal1:.2f} {cores["normal"]}passa a ganhar {cores["azul"]}R${sal2:.2f}')
