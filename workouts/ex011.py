# Faça um programa que, leia a altura e largura de uma parede, calcule sua área e a quantidade de tinta necessária para pintá-la  # noqa: E501

height = float(input('Digite a altura da parede: '))
width = float(input('Digite a largura dessa parede: '))

field = width * height

# 1l de tinta -> 2m²

liter = field / 2

print(f'A área dessa parede é {field}m², e gastará {liter}L de tinta para pintá-la')
