# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A. e mostre os dez primeiros tempos.  # noqa: E501
a1 = int(input('Usuário, digite o primeiro termo de uma P.A.: '))
r = int(input('Agora, digite sua razão: '))

pa = [a1]
term = a1 + r
pa.append(term)
for count in range(1, 9):
    term += r
    pa.append(term)

pa.append('...')
print(f'Essa é a sua progressão aritmética: {pa}')

