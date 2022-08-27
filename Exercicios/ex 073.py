from gettext import find


times = ('Palmeiras', 'Flamengo', 'Corinthians', 'Fluminense', 'Athetico-PR', 'Internacional', 'Atlético-Mg', 'América-MG'
'Bragantino', 'Santos', 'São Paulo', 'Botafogo', 'Goiás', 'Ceará SC', 'Fortaleza', 'Cuiabá','Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print('-'*30)

#'[ A ] Apenas os 5 primeiros colocados do brasileirão.'
#'[ B ] Os últimos 4 colocados da tabela'
#'[ C } Uma lista com os times em ordem alfabética'
#'[ D ] Em que posição na tabela está o Avaí.'
print('Apenas os 5 primeiros colocados do brasileirão: {}'.format(times[:5]))
print('=-'* 50)
print('Os últimos 4 colocados da tabela {}'.format(times[15:]))
print('=-'* 50)
print('Uma lista com os times em ordem alfabética: {}'.format(sorted(times)))
print('=-'* 50)
avai = (times.index('Avaí'))
print('O Avaí está na posição {}'.format(avai + 1))
