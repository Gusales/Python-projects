# Crie um programa que leia o nome completo de uma pessoa e mostre
# 1 - O nome com todas as letras maiúsculas e minúsculas. 
# 2 - Quantas letras ao todo (sem considerar espaços). 
# 3 - Quantas letras tem o primeiro nome

# Lendo o nome do usuário
name = str(input('Usuário, digite seu nome completo: ')).strip()

# Exibindo seu nome em caps lock e minúsculas
print(f'Este é o seu nome com todas as letras em maiúsculas: {name.upper()}\nEste é o seu nome com todas as letras em minúsculas: {name.lower()}')  # noqa: E501

#  Exibindo a quantidade de letras no nome (sem os espaços)
nameLenghtWithSpaces = len(name)
countSpaces = name.count(' ')

nameLenghtWithoutSpaces = nameLenghtWithSpaces - countSpaces
print(f'Seu nome inteiro possui {nameLenghtWithoutSpaces} letras')

# Lendo a quantidade de letras no primeiro nome
nameList = name.split()
print(f'Seu primeiro nome, {nameList[0]}, possui {len(nameList[0])} letras')
