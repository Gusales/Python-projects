# Faça um programa que leia o comprimento do cateto oposto e cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.  # noqa: E501

from emoji import emojize
from math import hypot

print(emojize('Olá usuário! Vamos calcular o Teorema de Pitágoras :triângulo_vermelho_para_cima:', language="pt"))  # noqa: E501
catA = float(input('Usuário, digite o valor do Cateto Oposto: '))
catB = float(input('Agora, digite o valor do Cateto Adjacente: '))

# a² + b² = c² 
hipo = hypot(catA, catB)
print(f'Utilizando a fórmula, temos x² = {catA}² + {catB}²\nPortanto a hipotenusa é igual a: {hipo:.2f}\n{hipo:.2f}² = {catA}² + {catB}²')  # noqa: E501
