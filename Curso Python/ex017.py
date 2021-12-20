import math
co = float(input("Qual o comprimento do Cateto Oposto em cm? "))
ca = float(input("Qual o compriemento do Cateto Adjascente em cm? "))
print(f"O comprimento da hipotenusa é de {math.hypot(co, ca):.2f}cm")
