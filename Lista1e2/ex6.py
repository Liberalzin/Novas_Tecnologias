# Escreva um aplicativo que receba a, b e c, coeficientes de uma equação do segundo grau, e calcule as raízes x’ e x” através da fórmula de Báskara.

import cmath

def calcular_raizes(a, b, c):
    delta = b ** 2 - 4 * a * c
    raiz_delta = cmath.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
    return x1, x2

a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))
c = float(input("Insira o coeficiente c: "))

x1, x2 = calcular_raizes(a, b, c)

print("As raízes da equação são:")
print("x1 =", x1)
print("x2 =", x2)


