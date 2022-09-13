pares = 0
maior = 0
somaColuna = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input('Digite um valor na posição {}, {}:  '.format(linha, coluna)))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
    print()
print('-=' * 30)
print('A soma de todos os pares {}'.format(pares))
for linha in range(0, 3):
    somaColuna += matriz[linha][2]
print('A soma dos valores da terceira coluna é: {} '.format(somaColuna))
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print('O maior valor da segunda linha é {}'.format(maior))
