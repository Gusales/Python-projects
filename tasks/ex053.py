# crie um programa que leia uma frase e diga se ela é palíndroma ou não.
phrase = str(input('Usuário, digite uma frase: ')).strip().upper()
keywords = phrase.split()
oneWord = ''.join(keywords)

reverse = ''
for letter in range(len(oneWord) - 1, -1, -1):
    reverse += oneWord[letter]

print(f'o inverso de {oneWord} é {reverse}, logo:')
if oneWord == reverse:
    print('Essa frase é uma palíndroma')
else:
    print('Essa frase não é uma palíndroma')