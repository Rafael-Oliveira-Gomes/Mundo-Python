from datetime import date
ano =  date.today().year
t = 0
t1 = 0
for n in range(1, 8):
    niver = int(input('Qual é o ano em que a {}  nasceu? '.format(n)))
    s = ano - niver
    if s >= 21:
        t = t + 1
    else:
        t1 = t1 + 1
print('Ao todo tivemos {} pessoas maiores.'.format(t))
print('E também tivemos {} pessoas menores'.format(t1))
