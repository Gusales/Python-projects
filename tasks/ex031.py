# Faça um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem.  # noqa: E501
# Cobre R$0.50 por Km. Caso a viagem exceda 200Km, cobre R$0,45.
km = int(input('Usuário, digite a distância da viagem em Km: '))

if km <= 200:
    passagem = km * 0.5
    print(f'A passagem custará: R${passagem:.2f}')
else:
    passagem = km * 0.45
    print(f'A passagem custará R${passagem:.2f}')
