salario =float(input('Qual o seu salário:'))
if salario >= 1250:
    aumento = salario * 1.10
    print('O seu salário com 10% de aumento fica: {}'.format(aumento))
else:
    aumento2 = salario * 1.15
    print('O seu salário com 15% de aumento fica: {}'.format(aumento2))
