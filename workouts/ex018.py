# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, Cosseno e Tangente desse ângulo.  # noqa: E501
import math

num = float(input('Usuário, digite algum ângulo: '))

# Convertendo num para ângulo
value = math.radians(num)
seno = math.sin(value)
cosseno = math.cos(value)
tangente = math.tan(value)

print(f'Seno de {num} = {seno:.2f},\nCosseno de {num} = {cosseno:.2f},\nTangente de {num} = {tangente:.2f}')  # noqa: E501
