##########################################################################
dicionario = {}
def ehPrimo(numero):
    primo = 0
    cont = 2
    if numero > 1:
        for p in range(2, numero):
            
            if (numero % p == 0):
                return False
            else:
                cont +=1
    if (cont == numero):
        return True
##########################################################################

for i in range (1, 501):
    if(ehPrimo(i)):
        dicionario[i] = ehPrimo(i)
print(dicionario)
