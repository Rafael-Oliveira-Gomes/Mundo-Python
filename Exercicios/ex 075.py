numeros = (int(input('Digite um número: ')),
            int(input('Digite um número: ')),
            int(input('Digite um número: ')),
            int(input('Digite um número: ')))
print('O valor 9 apareceu {} vezes'.format(numeros.count(9)))
if 3 in numeros:
    print('O valor 3 apareceu na {} posição.'.format(numeros.index(3)+1))
else:
    print('Não apareceu nenhum 3')
print('Os valores pares digitados foram', end='')
for n in numeros:
    if n %2==0:
        print(n, end=' ')
        