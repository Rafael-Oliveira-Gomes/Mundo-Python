km = float(input('Quantos km você percorreu com o carro?'))
a = int(input('Por quantos dias você alugou o carro?'))
p = (a * 60) + (km * 0.15)
print ('O total a se pagar é: {:.2f}'.format(p))
