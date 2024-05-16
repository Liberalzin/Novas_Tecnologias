# Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = str(input('''Qual Opçao Deseja?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do programa 
Digite: '''''))
while menu not in '5':
   if menu == '1':
       print('A soma entre {} + {} = {}'.format(n1,n2,n1+n2))
       menu = str(input('''Qual Opçao Deseja realizar agora?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do programa 
Digite: '''''))
   if menu == '2':
       print('A Multiplicacao entre {} x {} = {}'.format(n1,n2,n1*n2))
       menu = str(input('''Qual Opçao Deseja realizar agora?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do programa 
Digite: '''''))
   if menu == '3':
       if n1 > n2:
           print('O maior numero e {} '.format(n1))
       elif n1 == n2:
           print('Nenhum dos dois numeros e o maior os dois sao iguais')
       else:
           print('O maior numero e {} '.format(n2))
           menu = str(input('''Qual Opçao Deseja realizar agora?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do programa 
Digite: '''''))
   if menu == '4':
       n1 = int(input('Digite um novo valor: '))
       n2 = int(input('Digite um novo valor: '))
       menu = str(input('''Qual Opçao Deseja realizar agora?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do programa 
Digite: '''''))
print('Obrigado por usar nosso programa!')