from math import radians, sin, cos, tan
a = float(input("Insira o valor de um ângulo: "))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print(f"O Ângulo de {a}º tem o SENO de {s:.2f}")
print(f"O Ângulo de {a}º tem o COSSENO de {c:.2f}")
print(f"O Ângulo de {a}º tem a TANGENTE de {t:.2f}")
