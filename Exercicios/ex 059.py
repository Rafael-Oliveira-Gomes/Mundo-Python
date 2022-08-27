n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = 0
escolha = 0
while escolha != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    escolha = int(input('Qual operação você quer fazer: '))
    if escolha == 1:
        n3 = n1 +n2
        print('A soma desses 2 números é {}'.format(n3))
    elif escolha == 2:
        n3 = (n1 * n2)
        print('A multiplicação desses números é {}'.format(n3))
    elif escolha == 3:
        if n1 > n2:
            print('O {} é maior que o {}.'.format(n1, n2))
        else:
            print('O número {} é maior que o {}'.format(n2, n1))
    elif escolha == 4:
        n1 = int(input('Digite outro valor: '))
        n2 = int(input('Digite outro valor:'))
        
print('Você escolheu sair.')
