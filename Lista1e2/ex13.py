#O fatorial de um inteiro não negativo n é escrito como n! (pronuncia-se “n fatorial”) e é definido como segue:
#n! = n · (n – 1) · (n – 2) · ... · 1 (para valores de n maiores ou iguais a 1) e n! = 1 (para n = 0)

#Por exemplo, 5! = 5 · 4 · 3 · 2 · 1, o que dá 120.

#Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu fatorial.

from math import factorial
n = int(input('Digite um numero: '))
f = 1
c = n
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))