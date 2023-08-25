# Escreva um programa que jogue Joquempô com você!
from random import randint
from emoji import emojize

choices = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choices[randint(0, 2)]
print('\033[32m*=*\033[33m*=*' * 10 + '\033[m')
print('Vamos Jogar Pedra, Papel ou Tesoura!')
player = str(input('Faça sua escolha: ')).strip()
playerUp = player.upper()
print('\033[32m*=*\033[33m*=*' * 10 + '\033[m')

if pc == playerUp:
    print(emojize('\033[33mEMPATE! :melting_face:', language="en"))
elif (pc == 'PEDRA' and playerUp == 'PAPEL') or (pc == 'PAPEL' and playerUp == 'TESOURA') or (pc == 'TESOURA' and playerUp == 'PEDRA'):  # noqa: E501
    print(emojize(f'Eu escolhi {pc.capitalize()} :smiling_face_with_tear:', language="en"))  # noqa: E501
    print('\033[32mVOCÊ VENCEU!')
    print(f'{player.capitalize()} vence {pc.capitalize()}')
elif (playerUp == 'PEDRA' and pc == 'PAPEL') or (playerUp == 'PAPEL' and pc == 'TESOURA') or (playerUp == 'TESOURA' and pc == 'PEDRA'):  # noqa: E501
    print(emojize(f'Eu escolhi {pc.capitalize()} :beaming_face_with_smiling_eyes:', language='en'))  # noqa: E501
    print('\033[31mVOCÊ PERDEU!')
    print(f'{pc.capitalize()} vence {player.capitalize()}')
else:
    print(emojize('Não entendi sua escolha :thinking_face:', language="en"))

print('\033[32m*=*\033[33m*=*' * 10 + '\033[m')
