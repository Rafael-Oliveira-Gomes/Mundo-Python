lugar = float(input('Qual a distância em km dessa viagem: '))
if lugar <= 200:
    valor = (lugar * 0.50)
    print('O valor da viagem fica: {:.2f} R$'.format(valor))
else:
    valor2 = (lugar * 0.45)
    print('O valor será: {:.2} R$'.format(valor2))
print('Boa viagem!')
