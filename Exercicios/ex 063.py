#Fibonacci

numero1 = 0
numero2 = 1
resultado = 0
numerosoma = 0

while resultado < 100:
    
    numero1 = numero2
    numero2 = numerosoma
    numerosoma = (numero1 + numero2)
    resultado = numerosoma
    
    print('{}'.format(resultado),end=' => ')
    