maior = 0
menor =0

valores = []
for p in range(0,5):
    valores.append(int(input('Digite um valor para a posição {}: '.format(p))))

print('Você digitou os valores {}'.format(valores))
maior = (max(valores))
menor = (min(valores))
print('=-'* 40)
print('O maior número digitado foi {} na posição {}'.format(maior, valores.index(maior)), end='')
for i, v in enumerate(valores):
    if maior == v:
        print(f'{i}...', end='')
print()
print('O menor número digitado foi {} na posição {}'.format(menor, valores .index(menor)), end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')
print()
