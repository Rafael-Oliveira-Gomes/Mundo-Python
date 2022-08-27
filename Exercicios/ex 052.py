tot = 0
n1 = int(input('Qual número você deseja saber se é primo? '))
for p in range(1, n1 + 1):
    if n1 % p == 0:
        print('\033[33m', end=' ')
        tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(p), end=' ')
print('O número {} foi divisível {} vezes.'.format(n1, tot))
if tot == 2:
    print('Por isso ele é primo.')
else:
    ('Ele não é primo.')

