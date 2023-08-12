# Faça um algorítmo que receba um preço de um produto e calcule seu preço com desconto de 5%  # noqa: E501

value = int(input('Digite o valor do produto: '))
discount = ((5 / 100) * value)
newValue = value - discount

print(f'Valor do desconto(5%): R${discount:.2f}\nValor final: R${newValue:.2f}')
