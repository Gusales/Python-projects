# Crie um programa que leia um número Real (float) e mostre na tela sua posição inteira.

from math import trunc
num = float(input('Usuário, digite um número real (utilizando ponto como vírgula) '))

print(f'A parte inteira de {num} é: {trunc(num)}')
