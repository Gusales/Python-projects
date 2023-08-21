# Faça um programa que leia um ano e mostre se ele é bissexto.
# (DETALHE, AQUI COMEÇA OS MONTE DE IF E ELSE)

from datetime import date

year = str(input('Usuário, digite um ano: (Caso queira saber do ano atual, digite apenas 1) ')).strip()  # noqa: E501
if year == '1': 
    year = date.today().year

if str(year).isnumeric() is False:
    print('digite um ano válido!')
else:
    year = str(year)
    if (len(year) != 4):
        print('Digite um ano válido!')
    else:
        yearNum = int(year) 
        if yearNum % 4 == 0 and yearNum % 100 != 0 or yearNum % 400 == 0:
            print(f'{yearNum} é um ano bissexto!')
        else: 
            print(f'{yearNum} não é um ano bissexto')
