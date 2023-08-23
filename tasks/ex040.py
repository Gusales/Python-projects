# Desenvolva um programa que leia duas notas de um aluno, calcule e motre a sua média

# Caso a média seja inferior a 5, ele estará REPROVADO
# Caso a média esteja entre 5 e 6.9, ele estará de RECUPERAÇÃO
# Caso a média seja superior a 7, ele estará APROVADO

note1 = float(input('Digite a primeira nota: '))
note2 = float(input('Digite a segunda nota: '))

media = (note1 + note2) / 2
print(f'\nA média desse aluno é {media}')

if media >= 7:
    print('Aluno \033[1;32mAprovado!\033[m')
elif media >= 5 and media < 7:
    print('Aluno está em \033[1;33mRecuperação!\033[m')
else:
    print('Aluno \033[1;31mReprovado!\033[m')