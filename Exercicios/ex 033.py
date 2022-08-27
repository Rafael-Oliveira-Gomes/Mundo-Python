n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 > n2 > n3:
    print('O maior número é: {}'.format(n1))
else:
    print('')
if n2 > n1 > n3:
    print('O maior número é: {}'.format(n2))
else:
    print('')
if n3 > n2 > n1:
   print('O maior número é: {}'.format(n3))
else:
    print('')
if n1 < n2 < n3:
    print('O menor número é: {}'.format(n1))
else:
    print('')
if n2 < n1 < n3:
    print('O menor número é: {}'.format(n2))
else:
    print('')
if n3 < n1 < n2:
    print('O menor número é: {}'.format(n3))
else:
    print('')

