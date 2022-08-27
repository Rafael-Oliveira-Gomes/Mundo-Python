n1 = float(input('Qual foi a sua primeira nota?'))
n2 = float(input('Qual foi a segunda nota?'))
media = (n1 + n2) / 2

if media < 5:
    print('\033[0;31mREPROVADO\033[m')
    print('A sua média é {}'.format(media))

elif media > 5 and media < 6.9:
    print('\033[0;33mRECUPERAÇÃO\033[m')
    print('A sua média é {}'.format(media))

else:
    print('\033[0;34mAPROVADO\033[m')
    print('A sua média é {}'.format(media))
