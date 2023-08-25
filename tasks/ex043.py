# Calcular o IMC do usuário e mostrar seu status
kg = float(input('Usuário, digite sua massa corporal (em kg): '))
height = float(input('Agora, digite sua altura (em m): '))

imc = kg / (height ** 2)
print(f'Seu imc é {imc:.1f}kg/m²')

if imc < 18.5:
    print('Você está \033[1;31mabaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está \033[1;33mno peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com \033[1;33msobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está com \033[1;31mobesidade!')
elif imc >= 40:
    print('Você está com \033[1;31mobesidade mórbida!')
