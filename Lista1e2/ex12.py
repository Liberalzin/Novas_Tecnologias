# Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def n_primos(n):
    primos_encontrados = 0
    num = 2
    while primos_encontrados < n:
        if eh_primo(num):
            print(num, end=" ")
            primos_encontrados += 1
        num += 1

n = int(input("Digite a quantidade de números primos que deseja encontrar: "))
print(f"Os primeiros {n} números primos são:")
n_primos(n)