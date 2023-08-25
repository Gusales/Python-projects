# Escreva um programa que leia três segmentos de reta, e demonstre se eles formam um triângulo  # noqa: E501
# Se eles formarem, mostre o tipo desse triângulo
a = float(input('Usuário, digite o tamanho de uma reta: ').strip())
b = float(input('Usuário, digite mais uma: ').strip())
c = float(input('Usuário, digite o último tamanho da reta: ').strip())

if (b + c > a) and (a + c > b) and (b + a > c):
    print('\033[1;32mÉ possível formar um triângulo com essas retas!\033[m')
    if (a == b and a != c and b != c) or (a != b and b == c and a != c) or (a != b and b != c and a == c):  # noqa: E501
        print('Esse é um triãngulo \033[1;32mIsósceles!')
    elif a != b and b != c and a != c:
        print('Esse é um triãngulo \033[1;32mEscaleno!')
    elif a == b and b == c and c == a:
        print('Esse é um triãngulo \033[1;32mEquilátero!')
else:
    print('\033[1;31mNão é possível formar um triângulo com essas retas!')
