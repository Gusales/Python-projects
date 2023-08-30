# Faça um programa que leia o ano de nascimento de um atleta de natação e mostre sua categoria  # noqa: E501
from datetime import date
yearNow = date.today().year
print('  ')

birth = int(input('Usuário, digite o ano que você nasceu: '))
cat = yearNow - birth

print('  ')
if cat <= 9:
    print('Sua categoria é \033[1;36mMirim')
elif cat <= 14:
    print('Sua categoria é \033[1;36mInfantil')
elif cat < 19:
    print('Sua categoria é \033[1;36mJunior')
elif cat >= 19 and cat < 20:
    print('Sua categoria é \033[1;36mSênior')
else:
    print('Sua categoria é \033[1;36mMaster')
