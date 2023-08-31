# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.  # noqa: E501
# Considere a maioridade como 21 anos
from datetime import date

yearNow = date.today().year

major = []
minor = []
invalid = []

for count in range(0, 4):
    name = str(input(f'Digite o nome da {count + 1}ª pessoa: '))
    year = int(input('Em que ano ela nasceu? '))
    if len(str(year)) != 4:
        print('Ano inválido')
        invalid.append(name)
    elif year > yearNow:
        print('Ano inválido')
        invalid.append(name)
    elif (yearNow - year) >= 18:
        major.append(name)
    elif (yearNow - year) < 18:
        minor.append(name)

if len(major) > 0:
    print(f'Essas são as pessoas que são maiores de idade: {major}')
else:
    print('Não possuem maiores de idade')

if len(minor) > 0:
    print(f'Essas são as pessoas que são menores de idade: {minor}')
else:
    print('Não possuem menores de idade')

if len(invalid) > 0:
    print(f'Essas pessoas estão com os nomes inválidos: {invalid}')
