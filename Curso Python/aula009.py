frase = 'Curso em video Python'
print(f'{frase[9::3]}')

print(f"{len(frase)}")

print(f"{frase.count('o', 0 , 13)}")

print(f"{frase.find('deo')}")
print(f"{frase.find('Android')}")

print(f"{'Curso' in frase}")

print(f"{frase.replace('Python', 'Android')}")

print(f"{frase.upper()}")
print(f"{frase.lower()}")
print(f"{frase.capitalize()}")
print(f"{frase.title()}")

frase1 = '   Aprenda Python   '
print(f"{frase.strip()}")
print(f"{frase.rstrip()}")   # ou frase.lstrip() para começar pela esquerda

print(f"{frase.split()}")
print(f"{'-'.join(frase)}")

print("""Olá Mundo, esse texto é muito grande então para poder dar um print de uma vez só Utilizamos 3 Aspas""")
