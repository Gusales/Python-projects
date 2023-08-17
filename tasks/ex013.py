# Crie um programa que receba um salário de um funcionário e retorne um novo salário, com aumento de 15%   # noqa: E501
wage = float(input('Usuário, digite o valor do seu salário: '))
increase = (15 / 100) * wage
newWage = wage + increase

print(f'Com aumento de 15% (R${increase:.2f}), seu novo salário ficaria com R${newWage:.2f}')  # noqa: E501
