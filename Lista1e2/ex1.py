# Escreva um aplicativo que solicita ao usuário inserir dois inteiros, obtém do usuário esses números e imprime sua soma, produto, diferença e divisão.

def calcular_operacoes(num1, num2):
    soma = num1 + num2
    produto = num1 * num2
    diferenca = num1 - num2
    divisao = num1 / num2 if num2 != 0 else "indefinida (divisão por zero)"
    return soma, produto, diferenca, divisao

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
soma, produto, diferenca, divisao = calcular_operacoes(num1, num2)
print("Soma:", soma)
print("Produto:", produto)
print("Diferença:", diferenca)
print("Divisão:", divisao)
