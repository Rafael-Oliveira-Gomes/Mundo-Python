from random import choice
from time import sleep
players = {}
dado = (1, 2, 3, 4, 5, 6)
players['jogador1'] = choice(dado)
players['jogador2'] = choice(dado)
players['jogador3'] = choice(dado)
players['jogador4'] = choice(dado)
for nomes in players.keys():
    print('O {} tirou {}'.format(nomes, players[nomes]))
    sleep(1)
