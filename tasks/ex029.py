# Escreva um programa que leia a velocidade de um carro. Caso ele ultrapasse 80km/h o programa deverá mostrar uma mensagem de multa com o preço da multa.  # noqa: E501
multa = 7 # R$ 7,00 por cada km excedido
km = int(input('Usuário, digite a velocidade do seu carro: ').strip())
if km > 80:
    kmOut = km - 80
    priceMulta = kmOut * multa
    print(f'Usuário, você foi multado em R${priceMulta:.2f} por dirigir a {km}km/h em uma rodovia onde o limite é de 80km/h ({kmOut}km/h a mais do permitido)')  # noqa: E501

print('Tenha uma boa viagem e dirija com seguirança!')
