n1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = n1 + (10 - 1) * razao   #conta para aparecer ate os 10 primeiros da lista q eu quero
for pa in range(n1, decimo, razao):
    print('{}'.format(pa), end= '-> ')
