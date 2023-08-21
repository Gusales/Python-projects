# Faça um programa que leia um número e verifique se ele é ímpar ou par.
num = int(input('Usuário, digite um número: ').strip())
if (num % 2) == 0:
    print('O número digitado é par')
else:
    print('O número digitado é ímpar')