lista = []
continuar = ''
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('Posiçaõ\t\tNome:  \t\tMedia')
for i, alunos in enumerate(lista):
    print('{}\t\t{}\t\t{}\\'.format(i, alunos[0], alunos[2]))
while True:
    notas1e2 = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if notas1e2 == 999:
        break
    if notas1e2 <= len(lista) - 1:
        print('Notas de {} são: {}'.format(
            lista[notas1e2][0], lista[notas1e2][1]))
