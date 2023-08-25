# Elabore um programa que calcule o valor a ser pago em um produto, considerando seu preço normal, e condição de pagamento  # noqa: E501
productPrice = float(input('Digite o valor a ser pago no produto: R$'))

print('FORMAS DE PAGAMENTO:')
print('[ 1 ] à vista com dinheiro/cheque')
print('[ 2 ] á vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

payment = int(input('Qual a forma de pagamento? '))


totalPrice = float(0)
if payment == 1:
    discount = (10 / 100) * productPrice
    totalPrice = productPrice - discount
    print(f'Você recebeu um desconto de 10%! (R${discount:.2f})')
    print(f'Valor da compra final: R${totalPrice:2f}')

elif payment == 2:
    discount = (5 / 100) * productPrice
    totalPrice = productPrice - discount
    print(f'Você recebeu um desconto de 5%! (R${discount:.2f})')
    print(f'Valor da compra final: R${totalPrice:2f}')

elif payment == 3:
    totalPrice = productPrice
    print(f'Você pagará R${totalPrice:2f}, divido em duas parcelas de R${totalPrice / 2} ao mês')  # noqa: E501

elif payment == 4:
    divider = int(input('Quer dividir em quantas parcelas? '))
    juros = (20 / 100) * productPrice
    totalPrice = juros + productPrice
    parcelas = totalPrice / divider
    print(f'Você pagará R${totalPrice:.2f} com 20% de juros (R${juros:.2f}), divido em {divider} parcelas de R${parcelas:.2f} ao mês')  # noqa: E501
else:
    print('Você não selecionou uma forma de pagamento!')
