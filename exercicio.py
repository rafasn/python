soma=0
for i in range(1,4):
    nota = float(input(f'Informe a sua nota{i}:'))
    soma= soma+nota
media=soma/i
print(round(media))