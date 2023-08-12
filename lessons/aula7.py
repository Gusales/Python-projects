num1 = int(input('Digite um número '))
num2 = int(input('Digite outro número '))

sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

divInt = num1 // num2
expo = num1 ** num2

print('Resultados: \n Soma {},\n Subtração {},\n Multiplicação {} e\n Divisão {} (Apenas 3 casas {:.3f})'.format(sum, sub, mult, div, div))  # noqa: E501
print('Divisão inteira {} e Potencialização {}'.format(divInt, expo))

print('\nNova sintaxe!!! 2020')
print(f'Resultados: \n Soma {sum},\n Subtração {sub},\n Multiplicação {mult} e\n Divisão {div} (Apenas 3 casas {div:.3f})')  # noqa: E501
