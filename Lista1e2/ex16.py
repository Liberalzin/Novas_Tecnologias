# A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, … Os dois primeiros termos são iguais a 1, e a partir do terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥ 3, exiba o n-ésimo termo da série de Fibonacci.

print('-'*30)
print('N-ésimo termo da série de Fibonacci')
print('-'*30)

def fibonacci(n):
    if n <= 0:
        return "N deve ser um número inteiro positivo"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        t1 = 1
        t2 = 1
        for _ in range(3, n + 1):
            t3 = t1 + t2
            t1 = t2
            t2 = t3
        return t2

n = int(input('Digite o valor de n (número inteiro positivo): '))
result = fibonacci(n)
print('-'*30)
print(f'O {n}-ésimo termo da série de Fibonacci é: {result}')
print('-'*30)