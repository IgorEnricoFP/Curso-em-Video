cores = {"amarelo": '\033[33m',
         "vermelho": '\033[31m'}
velo = float(input('Qual é a velocidade atual do carro? '))
if velo > 80:
    print(f'{cores["vermelho"]}MULTADO! Você excedeu o limite permitido que é de: 80Km/h')
    multa = (velo - 80) * 7
    print(f'{cores["vermelho"]}Você deve pagar uma multa de R${multa:.2f}')
print(f'{cores["amarelo"]}Tenha um bom dia! Dirija com segurança!')
