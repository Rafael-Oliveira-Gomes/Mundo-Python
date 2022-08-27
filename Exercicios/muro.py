p = float(input('Qual a largura da parede?'))
a = float(input('Qual é a altura da parede?'))
area = a * p
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2'.format(p, a, area))
t = area / 2
print('Para pintar, você usará {} litros de tinta.'.format(t))

