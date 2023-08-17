# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.  # noqa: E501
num = int(input('Usuário, digite um número de 0 a 9999: '))
print(f'Analisando o número {num}:')

unid = num // 1    % 10 # Unidade
deze = num // 10   % 10 # Dezena
cent = num // 100  % 10 # Centena
mil  = num // 1000 % 10 # Unidade de Milhar

print(f'Unidade: {unid}, Dezena: {deze}, Centena: {cent}, Unid. de Milhar: {mil}')
