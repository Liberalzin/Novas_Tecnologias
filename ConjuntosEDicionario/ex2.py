L1 = [1, 2, 6, 8]
L2 = [3, 6, 8, 9]

conjunto_1 = set(L1)
conjunto_2 = set(L2)

valores_comuns = conjunto_1 & conjunto_2
print(f"Valores comuns às duas listas: {valores_comuns}")

valores_somente_primeira = conjunto_1 - conjunto_2
print(f"Valores que só existem na primeira: {valores_somente_primeira}")

valores_somente_segunda = conjunto_2 - conjunto_1
print(f"Valores que só existem na segunda: {valores_somente_segunda}")

elementos_nao_repetidos = conjunto_1 ^ conjunto_2
print(f"Elementos não repetidos nas duas listas: {elementos_nao_repetidos}")

primeira_sem_repetidos_segunda = conjunto_1 - conjunto_2
print(f"Primeira lista, sem os elementos repetidos na segunda: {primeira_sem_repetidos_segunda}")