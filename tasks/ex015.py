# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.  # noqa: E501
# Calcule o preço final, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

days = int(input('Usuário, digite o número de dias que esse carro foi alugado: '))
daysPrice = days * 60

km = float(input('Agora, digite a quilometragem rodada durante esses dias: '))
kmPrice = km * 0.15

total = daysPrice + kmPrice

print(f'Preço por dia alugado: R${daysPrice:.2f}\nPreço por km rodado: R${kmPrice:.2f}\nTotal: R${total:.2f}')  # noqa: E501
