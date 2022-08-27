palavras = ('garrafa', 'carne', 'rafa', 'dozape', 'desenvolvedor', 'aviao', 'sonhos', 'carro', 'snow')
for lista in palavras:
    print('\nNa palavra {} temos '.format((lista).upper(), end=''))
    for letra in lista:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
