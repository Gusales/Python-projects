# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar  # noqa: E501
value = float(input('Vamos fazer a conversão das moedas que você tem na carteira. Digite o valor: '))  # noqa: E501

# Com US$1,00 = R$3,27 
quotation = 3.27
convertion = value / quotation
print(f'Em jun de 2017, você estaria com US${convertion:.2f}')

# Com US$1,00 = R$4,91
quotation = 4.91
convertion = value / quotation
print(f'Em Ago de 2023, você estaria com US${convertion:.2f}')
