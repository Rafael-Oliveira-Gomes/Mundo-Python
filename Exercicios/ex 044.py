from ast import Num


produto = float(input('Qual o valor do produto?'))
metodo = int(input('''Escolha uma das opçoes:
[ 1 ] à vista no dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço normal
[ 4 ] em 3x ou mais no cartão: 20% de juros '''))

vista = produto - (produto * 0.10)
cartao = produto - (produto * 0.05)
acrescimo = produto + (produto * 0.20)

if metodo == 1:
    print('Você escolheu à vista no dinheiro ou cheque, e com 10% de desconto fica {} R$.'.format(vista))
elif metodo == 2:
    print('Você escolheu à vista no cartão com 5% de desconto, e fica R$ {} '.format(cartao))
elif metodo == 3:
    print('Você escolheu em 2x no cartão sem juros, e fica R$ {} por parcela.'.format(produto / 2))
elif metodo == 4:
    print('Você escolheu em 3x no cartão com 20% de juros, então o valor total fica {} R$ e por parcela fica {:.2f} R$'.format(acrescimo, produto / 3))
else:
    total = 0
    print('Opção inválida.')