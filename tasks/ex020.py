# O mesmo professor do desafio anterior deseja sortear a ordem de apresentação de um trabalho dos alunos. Crie um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.   # noqa: E501
from random import sample

name1 = str(input('Olá professor, digite o nome de um aluno: '))
name2 = str(input('Agora, digite o nome de mais um: '))
name3 = str(input('Digite o próximo: '))
name4 = str(input('Digite o nome do último: '))

list = [name1, name2, name3, name4]

listOrdened = sample(list, 4)
print(f'A ordem de apresentação ficará assim: \n{listOrdened}')
