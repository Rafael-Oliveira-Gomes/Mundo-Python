frase = str(input('Digite uma frase para saber se é um polindromo ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):      # inverso = junto[::-1]
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
    print(inverso)
else:
    print('Não é um palíndromo.')
