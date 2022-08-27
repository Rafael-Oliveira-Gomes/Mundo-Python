media = 0
somaIdade = 0

nomeHomemVelho = ''
idadeHomemVelho = 0

qtdMulherNova = 0

for p in range(1,5):
    print('---- {} Pessoa ----'.format(p))
    nomeInput = str(input('Nome: '))
    idadeInput = int(input('Idade: '))
    sexoInput = str(input('Sexo [M/F] ')).upper()
    somaIdade = somaIdade + idadeInput    
    if ((idadeInput > idadeHomemVelho) and (sexoInput in 'Mm')):
        idadeHomemVelho = idadeInput
        nomeHomemVelho = nomeInput

    if (idadeInput < 20) and (sexoInput in 'F'):
        qtdMulherNova += 1

    
    	    	
media = somaIdade / 4

print('A media de idade é {}'.format(media))
print('O homem mais velho é: {} com {} anos'.format(nomeHomemVelho, idadeHomemVelho))
print('O total de mulheres menores de 20 anos é {}'.format(qtdMulherNova))