# Escreva um programa que leia um número e verifique se é ou não um número primo.

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num +1):
    if num % c == 0:
        print('\033[33m', c, end=' ')
        tot += 1
    else:
        print('\033[31m', c, end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
