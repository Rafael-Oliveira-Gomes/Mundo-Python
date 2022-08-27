n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi: {}'.format(m))
if m >=6.0:
    print('Parabéns, você passou!')
else:
    print('Que pena')
