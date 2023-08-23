# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
# Pergunte o salário do comprador, o valor da casa e em quantos anos ele pretende pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.   # noqa: E501

house = float(input('Comprador, digite o valor da casa que queira comprar: R$'))
wage = float(input('Agora, digite o seu salário: R$'))
years = int(input('Em quantos anos deseja pagar? '))

months = years * 12 # Cálculo de quantos meses o usuário irá pagar o empréstimo

percent = (30 / 100) * wage

installment = house / months
print(f'Serão {months} parcelas de R${installment:.2f} por mês')

if installment <= percent:
    print('Você \033[1;32mpode\033[m realizar o financiamento dessa casa!')
else:
    print('Você \033[1;31mnão pode\033[m realizar o financiamento dessa casa!')
