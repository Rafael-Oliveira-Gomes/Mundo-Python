total = 0
contador = 0
maior = 0
nome = ''
menor = 0
print('-'*20)
print('LOJA DO RAFAO')
print('-'*20)

while True:
    nomeinput = str(input('Qual é o produto? '))
    preçoinput = float(input('Qual é o valor?R$ '))
    continuar = str(input('Deseja continuar? [S/N]')).upper()
    total += preçoinput
    if (preçoinput > 1000):
        contador += 1
    if (preçoinput > maior):
        maior = preçoinput
    if (preçoinput < menor):
        menor = preçoinput
        nome = nomeinput
    if continuar in 'N':
        break
print('O total gasto foi {}'.format(total))
print('Nessa lista temos {} produtos mais de 1000 R$.'.format(contador))
print('O produto mais barato é {}.'.format(nome))
