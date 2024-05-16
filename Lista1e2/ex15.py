# O quadrado de um número natural n é dado pela soma dos n primeiros números ímpares consecutivos. Por exemplo, 1^2 =1, 2^2 = 1+3 etc. Dado um número n, calcule seu quadrado usando a soma de ímpares ao invés de produto.

def quadrado_com_soma_impares(n):
    soma_impares = 0
    ultimo_impar = 1
    for _ in range(n):
        soma_impares += ultimo_impar
        ultimo_impar += 2
    return soma_impares

n = int(input("Digite um número natural: "))
quadrado = quadrado_com_soma_impares(n)
print(f"O quadrado de {n} é {quadrado}.")