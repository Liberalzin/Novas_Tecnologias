versao_inicial = [1, 2, 5, 6, 9]
versao_alterada = [1, 2, 8, 10]

conjunto_inicial = set(versao_inicial)
conjunto_alterado = set(versao_alterada)

nao_mudaram = conjunto_inicial & conjunto_alterado
print(f"Elementos que não mudaram: {nao_mudaram}")

novos_elementos = conjunto_alterado - conjunto_inicial
print(f"Novos elementos: {novos_elementos}")

removidos = conjunto_inicial - conjunto_alterado
print(f"Elementos que foram removidos: {removidos}")