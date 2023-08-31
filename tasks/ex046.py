# Faça um programa que mostre na tela uma contagem regressiva de 10 a 0 para o estouro de fogos de artifício, com uma pausa de 1 segundo entre elas.  # noqa: E501
from time import sleep

print(' ')
for count in range(10, -1, -1):
    print(count)
    sleep(1)
print('🎆 FELIZ ANO NOVO! 🎆')
