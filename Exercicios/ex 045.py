from random import choice
from time import sleep

jogue = int(input('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Qual é a sua jogada?'''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
papel = 'papel'
pedra = 'pedra'
tesoura = 'tesoura'
lista = ('pedra', 'papel', 'tesoura')
lista2 = choice(lista)

print('-=' * 20)

if jogue == 1 and lista2 == 'papel':
    print('\033[1;31mVocê jogou {} e eu {}, então você perdeu!\033[m'.format(pedra, lista2))
elif jogue == 2 and lista2 == 'pedra':
    print('\033[1;34mVocê jogou {} e eu {}, então você ganhou!\033[m'.format(papel, lista2))
elif jogue == 1 and lista2 == 'tesoura':
    print('\033[1;34mVocê jogou {} e eu {}, então você ganhou!\033[m'.format(pedra, lista2))
elif jogue == 3 and lista2 == 'pedra':
    print('\033[1;31mVocê jogou {} e eu {}, então você perdeu!\033[m'.format(tesoura, lista2))


elif jogue == 2 and lista2 == 'tesoura':
    print('\033[1;31mVocê jogou {} e eu {}, então você perdeu!\033[m'.format(papel, lista2 ))
elif jogue == 3 and lista2 == 'papel':
    print('\033[1;34mVocê jogou {} e eu {}, então você ganhou!\033[m'.format(tesoura, lista2))
else:
    print('INVÁLIDO')
  