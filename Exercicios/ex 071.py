print('-=' * 30)
print('{:^30}'.format('BANCO RABANK'))
print('-=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
totalcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print('O total de {} cédulas de R$'.format(totalcedula, cedula))
        if cedula == 50:
            cedula == 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break
print('-=' * 30)
print('Volte sempre ao nosso banco! Tenha um bom dia!')
print('-=' * 30)
