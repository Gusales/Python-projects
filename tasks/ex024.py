# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"  # noqa: E501
city = str(input('Digite o nome de uma cidade: ').strip())
city = city.lower()

cityHaveSanto = (city[:5] == 'santo')
print(f'Essa cidade começa com Santo? {cityHaveSanto}')
