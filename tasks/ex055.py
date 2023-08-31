# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.  # noqa: E501

majorWeight = 0
minorWeight = 1000

for count in range(0, 5):
    weight = float(input(f'Peso da {count + 1}ª pessoa: '))
    if majorWeight < weight:
        majorWeight = weight
    
    if minorWeight > weight:
        minorWeight = weight

print(f'O maior peso digitado foi: {majorWeight}Kg')
print(f'O menor peso digitado foi: {minorWeight}Kg')
