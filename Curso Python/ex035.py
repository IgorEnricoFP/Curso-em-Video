cores = {"normal": '\033[m',
         "amarelo": '\033[33m',
         "roxo": '\033[35m'}
print(f'{cores["amarelo"]}-=-' * 20)
print(f'{cores["roxo"]}Analisador de Triângulos')
print(f'{cores["amarelo"]}-=-' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo')
