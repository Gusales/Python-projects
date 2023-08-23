# Escreva um programa que compare dois valores, diga qual dos dois é maior ou se eles são iguais.  # noqa: E501

num1 = int(input('Usuário, digite um número: '))
num2 = int(input('Agora, digite mais um: '))

if num1 == num2:
    print('Esses números são iguais!')
elif num1 > num2:
    print(f'{num1} é maior que {num2}')
else:
    print(f'{num2} é maior que {num1}')
