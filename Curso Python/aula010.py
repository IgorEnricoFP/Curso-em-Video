tempo = int(input('Quantos anos tem seu carro? '))
# print('Carro novo' if tempo <= 3 else 'Carro velho')
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
# //////////////////
nome = str(input('Qual é seu nome? ')).title()
if nome == 'Igor':
    print('Que nome familiar!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
# /////////////////
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi: {m:.2f}')
if m >= 6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim, Estude Mais!')
