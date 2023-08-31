# Refaça o desafio 009 agora utilizando loop for
value = int(input('Usuário, digite um valor para ver sua tabuada: '))
for count in range(0, 11):
    print(f'{value} x {count:2} = {(value * count):2}')
