# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.  # noqa: E501
print(' ')

media = 0

major = 0
majorName = ''

twentyYearsLow = []

for count in range(0, 4):
    print(('='*5) + f' {count + 1}ª pessoa ' + ('='*5))
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).upper()

    # calculando a média
    media += age

    # vendo qual o homem mais velho
    if sex == 'M' and major < age:
        majorName = name
        major = age

    # Quais mulheres possuem menos de 20 anos
    if sex == 'F' and age < 20:
        twentyYearsLow.append(name)

print(f'\nA média de idade desse grupo é de {media / 4} anos')
print(f'O homem mais velho desse grupo é {majorName} com {major} anos')

if len(twentyYearsLow) > 0:
    print(f'Essas são as mulheres que possuem menos de 20 anos: {twentyYearsLow}')
else:
    print('Não há mulheres com menos de 20 anos')