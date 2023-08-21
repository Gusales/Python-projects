# Condicionais usando if e else
time = int(input('Usuário, digite quantos anos tem seu carro: '))

# Outra maneira de fazer 
# print('carro novo' if time <= 3 else 'carro velho')
if time <= 3:
    print('Seu carro está novinho!')
else:
    print('Seu carro ja ta veinho')