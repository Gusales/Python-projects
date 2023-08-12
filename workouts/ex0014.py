# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.  # noqa: E501
grausC = float(input('Digite uma temperatura: ºC'))

# Fórmula!! 
# F = ((9 * ºC) / 5) + 32

grausF = ((9 * grausC) / 5) + 32

print(f'{grausC}ºC equivale a {grausF}ºF')
