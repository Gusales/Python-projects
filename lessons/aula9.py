text = 'hello world'
texto = ' Olá mundo! '

print(text)
# Resultado: hello world

print(text[0]) 
# Resultado: h

print(text[0:6])
# Resultado: hello

print(text[0:6:2])
# Resultado: hlo

print(text[:6])
# Resultado: hello

print(text[7:])
# Resultado: world

print(text[0::2])
# Resultado: hlowrd

# Para obter o comprimento(tamanho) da string, é utilizado len, que vem de lenght
print(len(text))
# Resultado: 11

# Para obter uma contagem de caracteres repetidos, podemos utilizar o método count,
# Ele também pode ser utilizado com fatiamento.
print(text.count('l'))
# Resultado: 3

# Para encontrar um certo conjunto de caracteres, podemos utilizar o find()
# Ele nos retorna a posição em que o termo se inicia
print(text.find('ello'))
# Resultado: 1

# Também pode ser escrito assim: (mas retornando apenas true ou false)
print('hello' in text)
# Resultado: True

# Para alterar algum termo dentro da string, usamos replace('o que vai trocar', 'o que vai entrar no lugar')  # noqa: E501
print(text.replace('Hello', 'Olá'))
# Resultado: Olá world

# Exibir a string com caracteres em maiúsculos
print(text.upper())
# Resultado: HELLO WORLD

# Exibir a string com caracteres em minúsculos
print(text.lower())
# Resultado: hello world

# Para exibir a string toda em minúscula, mas com o primeiro caractere em maiúsculo, usamos capitalize()  # noqa: E501
print(text.capitalize())
# Resultado: Hello world

# Para por todas as palavras com a primeira letra em maiúscula, se usa title()
print(text.title())
# Resultado:  Olá Mundo

# A partir daqui, usaremos texto

# Para remover espaços em branco inúteis
print(texto.strip())
# Resultado: Olá mundo!

# Para remover apenas os espaços em branco da direta, usamos uma variação do strip
print(texto.rstrip())
# Caso texto = 'Olá mundo! ', ficaria 'Olá mundo!'
# Resultado: Olá mundo!

# Assim como o r, podemos usar l
print(texto.lstrip())
# Resultado: Olá mundo!

splitedText = text.split()
print(splitedText)
# Resultado: ['hello', 'world']

joinedText = '-'.join(splitedText)
print(joinedText)
# Resultado: hello-world
