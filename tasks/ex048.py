# faça um programa que mostre na tela todos os números pares de 1 a 50

print('Esse é o resultado da soma dos ímpares multiplos de 3 até o número 500: ')
sum = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        sum += count
print(f'{sum}')

