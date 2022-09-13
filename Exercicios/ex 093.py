dicionario = {}
lista = []
tol = 0
dicionario['nome'] = str(input('Nome do jogador? '))
jogos = int(input('Quantos jogos {} jogou? '.format(dicionario['nome'])))
for i in range(0, jogos):
    gol = int(input('Quantos gols na partida {}? '.format(i)))
    tol = (tol + gol)
    lista.append(gol)

dicionario['gols'] = lista
dicionario['total'] = tol
print('-=' * 20)
print(dicionario)
print('-=' * 20)
for k, v in dicionario.items():
    print('O campo {} tem o valor {}'.format(k, v))
print('-=' * 20)

#    print('Na partida {}, fez {}'.format(p, dicionario['gols']))
print('Foi um total de {} gols.'.format(dicionario['total']))

