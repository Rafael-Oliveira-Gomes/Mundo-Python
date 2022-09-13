import random


def megasena():
    escolhidos = []
    lista = []

    # Constroi lista de 1 a 60
    contadorLista = 1
    while(contadorLista <= 60):
        lista.append(contadorLista)
        contadorLista += 1

    possibilidades = lista
    # Escolhe 6 numeros aleatórios
    contadorEscolhidos = 1
    while(contadorEscolhidos <= 6):
        escolhido = random.choice(possibilidades)
        possibilidades.remove(escolhido)
        escolhidos.append(escolhido)
        contadorEscolhidos += 1

    print("possibilidades:")
    print(lista)
    print("\nescolhidos:")
    print(sorted(escolhidos))

    return sorted(escolhidos)


def criarJogo():
    def inputNumero(jogo):
        numero = int(input("Escreva o numero " + str(i+1) + ": "))
        if numero > 60 or numero < 1:
            print("Número inválido. Tente de novo")
            inputNumero(jogo)
        if numero in jogo:
            print("Nao pode escrever um numero repetido no mesmo jogo.")
            inputNumero(jogo)
        else:
            jogo.append(numero)

    jogo = []

    for i in range(0, 6):
        inputNumero(jogo)
    return sorted(jogo)


print('MEGA SENA')
print('=-' * 30)
qtd = int(input('Quantos jogos você quer fazer? '))

jogos = []

for i in range(0, qtd):
    print('-' * 60)
    print("jogo " + str(i+1) + ":")
    jogos.append(criarJogo())
print('-' * 60)

resultado = megasena()

print("seus jogos:")
print(jogos)

for jogoAtual in jogos:
    if jogoAtual == resultado:
        print("VOCE GANHOU!")
        break

print("Você errou")
