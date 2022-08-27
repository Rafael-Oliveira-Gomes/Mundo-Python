from datetime import date
ano = int(input('Em que ano está: '))
if ano == 0: #vai falar do ano em que estamos
    ano = date.today().year
    print(ano)
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')
