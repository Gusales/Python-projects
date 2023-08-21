# Escreva um programa que leia três segmentos de reta, e demonstre se eles formam um triângulo  # noqa: E501
a = float(input('Usuário, digite o tamanho de uma reta: ').strip())
b = float(input('Usuário, digite mais uma: ').strip())
c = float(input('Usuário, digite o último tamanho da reta: ').strip())

if (b + c > a) and (a + c > b) and (b + a > c):
    print('É possível formar um triângulo com essas retas!')       
else:
    print('Não é possível formar um triângulo com essas retas!')
