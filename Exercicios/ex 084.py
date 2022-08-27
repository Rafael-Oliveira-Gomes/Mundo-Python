contador = 0
pessoas_peso = []
continuar = ''
maior = []
menor = []
nomeMaior = []
nomeMenor = []
while True:
    pessoas_peso.append(str(input('Nome: ')))
    pessoas_peso.append(float(input('Peso: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    contador += 1
    if continuar == 'N':
        break
    for p in pessoas_peso:
        if p == 0:
            maior = pessoas_peso[1]
            menor = pessoas_peso[1]
        if pessoas_peso[1] > maior:
            maior = pessoas_peso
        if pessoas_peso[1] < menor:
            menor = pessoas_peso[1]
print()
            