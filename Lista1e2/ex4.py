# Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, separa o número em seus dígitos individuais e imprime os dígitos separados uns dos outros por três espaços cada. Por exemplo, se o usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.

def separar_digitos(numero):
    numero_str = str(numero)
    for digito in numero_str:
        print(digito, end="   ")

numero_usuario = input("Por favor, insira um número de cinco dígitos: ")
if len(numero_usuario) != 5 or not numero_usuario.isdigit():
    print("Por favor, insira um número válido de cinco dígitos.")
else:
    numero_int = int(numero_usuario)
    print("Dígitos separados por três espaços:")
    separar_digitos(numero_int)