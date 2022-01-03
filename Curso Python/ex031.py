dis = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {dis:.2f}Km.')
preco = dis * 0.50 if dis <= 200 else dis * 0.45
print(f'E o preço da sua viagem será de R${preco:.2f}')
