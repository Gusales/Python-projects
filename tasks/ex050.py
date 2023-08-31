# Desenvolva um programa que leia seis números inteiros e mostre a soma daqueles que apenas sejam pares. Os ímpares, desconsidere-os.  # noqa: E501
sum = 0
print(' ')
for count in range(0, 6):
    num = int(input('Usuário, digite um número: '))

    if num % 2 == 0:
        sum += num
print(f'A soma dos números pares digitados é igual a: {sum}')
