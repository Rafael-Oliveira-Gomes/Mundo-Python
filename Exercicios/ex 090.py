aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média de {}: '.format(aluno['nome'])))
if (aluno['media'] > 7):
    print('Aprovado')
else:
    print('Reprovado')
    