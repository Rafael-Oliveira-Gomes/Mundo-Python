n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1 > n2:
    print('O número {} é maior que o {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que o {}'.format(n2, n1))
    print('2 opção')
else:
    print('\033[1;31mNãõ existe valor maior, os dois são iguais.\033[m')
