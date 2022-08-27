while True:
    valor = int(input('Qual número você quer saber a tabuada: '))
    if valor < 0:
        break
    for p in range(1, 11):
        print('{} x {} = {}'.format(valor, p, valor * p))
print('\033[1;31mPROGRAMA ENCERRADO.\033[m')
