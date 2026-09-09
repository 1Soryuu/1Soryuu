import random

numero = random.randint(1, 100)

print("Jogo de adivinhação")
print("Tente adivinhar o número que estou pensando entre 1 a 100")
print("Você tem 8 tentativas")

numero_secreto = numero
contador = 8
acertou = False

while contador > 0:

    print("Você ainda tem", contador, "tentativas.")

    tentativa = int(input("Digite o seu número: "))

    if tentativa == numero_secreto:
        acertou = True
        tentativas_usadas = 8 - contador + 1

        print("Parabéns! Você acertou!")
        print("Você acertou o número secreto em", tentativas_usadas, "tentativas!")

        break

    elif tentativa < numero_secreto:
        print("O número secreto é maior do que o seu palpite.")

    else:
        print("O número secreto é menor do que o seu palpite.")

    contador -= 1

if not acertou:
    print("Que pena, você errou todas as tentativas!")
    print("O número secreto era:", numero_secreto)
