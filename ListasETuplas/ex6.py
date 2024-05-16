lugares_vagos = [10, 2, 1, 3, 0]

while True:
    num_sala = int(input("Digite o número da sala (0 para sair): "))
    if num_sala == 0:
        break
    if num_sala < 1 or num_sala > 5:
        print("Número de sala inválido.")
        continue
    lugares_solicitados = int(input("Digite a quantidade de lugares solicitados: "))
    if lugares_solicitados > lugares_vagos[num_sala - 1]:
        print("Não é possível vender o número de lugares solicitados.")
    else:
        lugares_vagos[num_sala - 1] -= lugares_solicitados
        print(f"Venda realizada. Agora restam {lugares_vagos[num_sala - 1]} lugares na sala {num_sala}.")