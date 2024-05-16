def jogo_da_forca():
    palavra = list("palavra")
    forca = ["_"] * len(palavra)
    tentativas = 6

    print("Jogo da Forca!")
    print(' '.join(forca))

    while tentativas > 0 and "_" in forca:
        letra = input("\nDigite uma letra: ")

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    forca[i] = letra
            print(' '.join(forca))
        else:
            tentativas -= 1
            print(f"Letra não encontrada. Você tem {tentativas} tentativas restantes.")

    if "_" not in forca:
        print("\nParabéns, você ganhou!")
    else:
        print("\nVocê perdeu. A palavra era " + ''.join(palavra))

jogo_da_forca()
