# Faça um programa que leia um número inteito e diga se ele é primo ou não
num = int(input('Digite um número e veja se ele é primo ou não: '))

divider = []

for count in range(1, num + 1):
    if num % count == 0:
        divider.append(count)
        
if len(divider) == 2:
    print(f'{num} é um número primo')
else:
    print(f'{num} não é um número primo')
