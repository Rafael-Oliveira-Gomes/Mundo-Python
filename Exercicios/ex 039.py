from datetime import date
idade = int(input('Qual a sua idade?'))
ano = date.today().year
if idade < 18:
    resto = (ano - idade) - 2000
    print('O seu momento está chegando, você deverá se alistar em breve. Falta {} anos para você se alistar.'.format(resto))
elif idade == 18:
    print('Está na hora de se alistar.')
else:
    resto = (ano - idade) - 2000
    print('Seu tempo de se alistar já passou {} do prazo'.format(resto))

    