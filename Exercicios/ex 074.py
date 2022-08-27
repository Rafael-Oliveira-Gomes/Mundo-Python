from random import choice
maior = 0
menor = 0
while True:
    for p in range(1,6):
        
        n1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        n2 = choice(n1)
        if p == 1:
            maior = n2
            menor = n2
        print(n2, end=' ')
        if n2 > maior:
            maior = n2
        if n2 < menor:
            menor = n2        
    break        

print('\nO maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
