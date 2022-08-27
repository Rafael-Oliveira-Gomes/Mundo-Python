from random import choice
print('=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 10)
lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
computador = 0
valorinput = 0
parimpar = ''
soma = 0
contador = 0
while True:
    computador = choice(lista)
    parimpar = str(input('Você quer par ou ímpar? [P/I]: ')).upper()
    valorinput = int(input('Digite um número: '))
    soma = computador + valorinput
    contador += 1
    if (soma % 2 == 0) and (parimpar in 'P'):
        print('Você jogou {} e o computador {}. Total de {} é par.'.format(valorinput, computador, soma))
        print('VOCÊ VENCEU!')
    if (soma % 2 == 1) and (parimpar in 'I'):
        print('Você jogou {} e o computador {}. Total de {} é ímpar.'.format(valorinput, computador, soma))
        print('VOCÊ VENCEU!')
    if (parimpar in 'I') and (soma % 2 ==0):
        break
    if (parimpar in 'P') and (soma % 2 ==1):
        break
    
    print('Vamos jogar novamente...')
print('O computador jogou {} e você {}, o total é {}.'.format(computador, valorinput, soma))
print('GAMER OVER! Você venceu {} vezes.'.format(contador))
