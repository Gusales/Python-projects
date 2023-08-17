# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez  # noqa: E501
sentence = str(input('Usuário, digite uma frase: ')).strip().lower()
sentenceA = sentence.count('a')

sentenceAInitial = sentence.find('a') + 1
sentenceAFinal = sentence.rfind('a') + 1

print(f'A frase possui {sentenceA} letras "a" \nA primeira letra "a" apareceu na posição {sentenceAInitial} \nA ultima letra "a" apareceu nessa posição: {sentenceAFinal} ')  # noqa: E501
