# Escreva um programa que leia um valor em metros e faça a conversão para centímetros e milímetros # noqa: E501
meter = int(input('Digite a metragem que deseja calcular: '))
cent = meter * 100
mili = meter * 1000

print(f'Valor em centímetros: {cent}cm\n Valor em milímetros: {mili}mm')