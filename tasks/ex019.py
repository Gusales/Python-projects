# Um professor deseja sortear um de seus quatro alunos para apagar o quadro. Crie um programa que o auxilie, escrevendo o nome do escolhido.  # noqa: E501
from random import choice

name1 = str(input('Olá professor, digite o nome de um aluno: '))
name2 = str(input('Agora, digite o nome de mais um: '))
name3 = str(input('Digite o próximo: '))
name4 = str(input('Digite o nome do último: '))

list = [name1, name2, name3, name4]

sorted = choice(list)
print(f'O aluno(a) escolhido foi: {sorted}!')
