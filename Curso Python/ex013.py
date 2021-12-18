salarioI = float(input("Qual o salário do funcionário? R$"))
aumento = int(input("Qual o aumento que o funcionário receberá? "))
salarioF = salarioI + (salarioI * aumento / 100)
print(f"Um funcionário que ganhava R${salarioI:.2f}, com {aumento}% de aumento, passa a receber R${salarioF:.2f} ")
