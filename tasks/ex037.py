# Escreva um programa que leia um número inteiro e peça para que o usuário escolha a base de conversão.  # noqa: E501
num = int(input('Usuário, digite um número: '))
print(''' Escolha uma base de converção
      [ 1 ] converter em BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL
       ''')
base = int(input('Agora, digite a base de conversão (Binário, Octal ou Hexadecimal): '))

if base == 1:
    print(f'\033[1;32m{num}\033[m em binário: \033[1;32m{bin(num)[2:]}')
elif base == 2:
    print(f'\033[1;32m{num}\033[m em Octal: \033[1;32m{oct(num)[2:]}')
elif base == 3:
    print(f'\033[1;32m{num}\033[m em Hexadecimal: \033[1;32m{hex(num)[2:]}')
else:
    print('Nenhuma base decimal foi escolhida :/')
    print(f'Mas aqui está a conversão desse número:\nBinário: \033[1;32m{bin(num)}\033[m')  # noqa: E501
    print(f'Octal: \033[1;32m{oct(num)}\033[m \nHexadecimal: \033[1;32m{hex(num)}')