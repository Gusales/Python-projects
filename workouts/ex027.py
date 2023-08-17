# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.  # noqa: E501
name = str(input('Usuário, digite o seu nome completo: ')).strip()
name = name.split()
firstName = name[0]
lastName = name[(len(name) - 1)]
print(f'Usuário, seu primeiro nome é {firstName} e seu último nome é {lastName}.')
