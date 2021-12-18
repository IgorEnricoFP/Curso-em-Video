preco = float(input("Qual o preço do produto? R$"))
desconto = int(input("Qual a porcentagem de desconto? "))
final = preco - (preco * desconto / 100)
print(f"O produto que custava R${preco:.2f}, na promoção com desconto de {desconto}% vai custar R${final:.2f}")
