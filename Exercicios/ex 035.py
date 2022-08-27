n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento:'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
    if n1 == n2 and n2 == n3:
        print('É um triângulo equilátero')

    elif n1 == n2 or n1 == n3 or n2 ==n3:
        print('É um triângulo isósceles')

    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('É um triângulo Escaleno')

else:
    print('Não pode se formar um triângulo')
