import emoji # Importação da biblioteca Emoji
from math import sqrt, floor

print(emoji.emojize("Olá Mundo, :globo_mostrando_as_américas: ", language='pt'))
num = int(input('Digite um número: '))
root = floor(sqrt(num))

print(f'Esse é o resultado da Raiz quadrada de {num}: {root}')
