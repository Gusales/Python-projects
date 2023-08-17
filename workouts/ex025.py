# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
name = str(input('Usuário, digite seu nome completo: ')).lower()
nameHaveSilva = name.find('silva')
print(f'Seu nome possui Silva? {nameHaveSilva != -1}')
