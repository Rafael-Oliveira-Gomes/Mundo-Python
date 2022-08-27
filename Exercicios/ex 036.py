
print('- -' * 25)
valor = float(input('Qual o valor da casa?'))
print('- -' * 25)
salario = float(input('Quanto é o seu salário?'))
print('- -' * 25)
anos = int(input('Em quantos anos você quer pagar?'))
print('- -' * 25)
prestação = valor / (anos * 12)
    
resto = salario * 0.30 / 100
    
if prestação <= resto :
    print('Empréstimo pode ser CONCEDIDO!')

else:
    print('Empréstimo NEGADO!')
    