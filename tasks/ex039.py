# Faça um programa que leia o ano de nascimento de um jovem e informe: 
# Ainda vai se alistar, precisa se alistar ou ja passou o tempo do alistamento
from datetime import date
birth = int(input('Usuário, digite o ano de seu nascimento: '))
yearNow = date.today().year

age = yearNow - birth

if age == 18 and date.today().month <= 6:
    print(f'Você tem até dia 30 de Junho para fazer o alistamento! Ainda faltam {6 - date.today().month} meses para o fim do prazo')  # noqa: E501
elif age == 18 and date.today().month > 6:
    print(f'Já passou o dia do alistamento! Caso não tenha feito, procure uma junta militar mais rápido possível! Se passaram {date.today().month - 6} meses após o fim do prazo')  # noqa: E501
elif age > 18:
    print(f'Já passou a data do alistamento! já se passaram {age - 18} anos da data do alistamento!')  # noqa: E501
elif age < 18 and age > 0:
    print(f'O alistamento é obrigatório no ano em que o jovem completar 18 anos de idade, e deverá ser feito até 30 de Junho. Ainda faltam {18 - age} anos até o ano do alistamento')  # noqa: E501
else:
    print('Não é possível analisar sua idade!')
