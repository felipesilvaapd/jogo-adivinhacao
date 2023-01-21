import random

def jogar():
    print("*************************************")
    print("  Bem vindo ao jogo de Adivinhação!  ")
    print("*************************************")

    numero_secreto = round(random.random() * 100)
    total_de_tentativas = 10
    rodada = 1

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        print("Só tem três níveis de dificuldade")

    while(rodada <= total_de_tentativas):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu numero: ")
        print("você digitou", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if (acertou):
            print("Você acertou o chute")
            break
        else:
            if(maior):
                print("Você errou! o seu chute foi maior que o número secreto")
            elif(menor):
                print("você errou! o seu chute foi menor que o número secreto")

        rodada = rodada + 1

    print("Fim do jogo")



if(__name__ == "__main__"):
    jogar()