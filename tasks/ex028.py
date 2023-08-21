# Escreva um programa que faça o computador pensar em um número de 0 a 5 e peça para que o usuário tente adivinhar o número.  # noqa: E501
from random import randint

print('-=-' * 10)
pc = randint(0, 5)
print('Acabei de pensar em um número de 0 a 5... Tenta adivinhar qual!')
print('-=-' * 10) 

player = int(input('Qual número você acha que é? ').strip())
if player == pc:
    print('Parabéns! Você conseguiu adivinhar o número!')
else:
    print(f'Infelizmente, você não conseguiu adivinhar :( O número que pensei foi {pc} e não {player}')  # noqa: E501
