velocidade = float(input('Qual a velocidade do carro:'))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou 80km de velocidade e sua multa vai ser: {} R$'.format(multa))
else:
    print('Fim')
