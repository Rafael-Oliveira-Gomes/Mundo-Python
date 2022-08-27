inputUsuario = int(input('Digite um número para saber o seu fatorial: '))

numeroParaMultiplicar = inputUsuario
resultado = numeroParaMultiplicar
txtMultiplicacao = '' + str(numeroParaMultiplicar )

while numeroParaMultiplicar - 1!=0:
    numeroParaMultiplicar -= 1
    resultado = resultado * numeroParaMultiplicar
    txtMultiplicacao = txtMultiplicacao + ' x ' + str(numeroParaMultiplicar)

print(txtMultiplicacao + ' = ' + str(resultado))

