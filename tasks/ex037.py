# Escreva um programa que leia um número inteiro e peça para que o usuário escolha a base de conversão.  # noqa: E501
num = int(input('Usuário, digite um número: '))
base = str(input('Agora, digite a base de conversão (Binário, Octal ou Hexadecimal): '))

if base.upper() == 'BINÁRIO' or base.upper() == 'BINARIO' or base.upper() == 'BIN':
    print(f'\033[1;32m{num}\033[m em binário: \033[1;32m{bin(num)}')
elif base.upper() == 'OCTAL' or  base.upper() == 'OCT':
    print(f'\033[1;32m{num}\033[m em Octal: \033[1;32m{oct(num)}')
elif base.upper() == 'HEXADECIMAL' or  base.upper() == 'HEX':
    print(f'\033[1;32m{num}\033[m em Hexadecimal: \033[1;32m{hex(num)}')
else:
    print('Nenhuma base decimal foi escolhida :/')
    print(f'Mas aqui está a conversão desse número:\nBinário: \033[1;32m{bin(num)}\033[m')  # noqa: E501
    print(f'Octal: \033[1;32m{oct(num)}\033[m \nHexadecimal: \033[1;32m{hex(num)}')