# Crie um programa que receba um salário de um funcionário e retorne um novo salário
# Caso ele receba menos que R$1.250,00, o salário aumentará em 15%
# Caso ele receba mais que R$1.250,00, o salário aumentará em 10%

wage = float(input('Usuário, digite o valor do seu salário: '))

increasePercent = 15 if wage <= 1250 else 10

increase = (increasePercent / 100) * wage
newWage = wage + increase

print(f'Com aumento de {increasePercent}% (R${increase:.2f}), seu novo salário ficaria com R${newWage:.2f}')  # noqa: E501
