# Escreva um programa que leia três números, e demonstre qual é o maior e qual é o menor
num1 = int(input('Usuário, digite um número: ').strip())
num2 = int(input('Usuário, digite um segundo número: ').strip())
num3 = int(input('Usuário, digite o último número: ').strip())

minor = num1
major = num1

if num2 < num1 and num2 < num3:
    minor = num2
if num3 < num1 and num3 < num2:
    minor = num3

if num2 > num1 and num2 > num3:
    major = num2
if num3 > num1 and num3 > num2:
    major = num3

print(f'O maior valor digitado foi: {major}')
print(f'O menor valor digitado foi: {minor}')
