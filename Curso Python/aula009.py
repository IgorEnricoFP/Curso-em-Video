frase = 'Curso em video Python'
print(frase[9::3])

print(len(frase))

print(frase.upper().count('O'))
print(frase.count('o', 0 , 13))

print(frase.find('deo'))
print(frase.find('Android'))

print('Curso' in frase)

print(frase.replace('Python', 'Android'))

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase1 = '   Aprenda Python   '
print(frase.strip())
print(frase.rstrip())   # ou frase.lstrip() para começar pela esquerda

fraseDiv = frase.split()
print(fraseDiv[0])
print('-'.join(frase))

print("""Olá Mundo! esse texto é muito grande então para poder dar um print de uma vez só Utilizamos 3 Aspas""")

