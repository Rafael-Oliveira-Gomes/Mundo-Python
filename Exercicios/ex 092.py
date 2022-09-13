dicionario = {}
dicionario['nome'] = str(input('Qual o seu nome? '))
dicionario['idade'] = 2022 - int(input('Em que ano você nasceu? '))
dicionario['ctps'] = int(input('Qual sua carteira de trabalho? 0 se não tiver'))
if dicionario['ctps'] !=0:
    dicionario['anoContrato'] = int(input('Em que ano você foi contratado? '))
    dicionario['salario'] = float(input('Qual o seu salário? '))
    dicionario['aposentadoria'] = (dicionario['idade'] + (2022 - dicionario['anoContrato']))
for k, v in dicionario.items():
        print(' {} tem o valor {}'.format(k, v))
     

