def verifica_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == "(":
            pilha.append(char)
        elif char == ")":
            if not pilha or pilha.pop() != "(":
                return "Erro"
    return "OK" if not pilha else "Erro"

print(verifica_parenteses("(())"))  
print(verifica_parenteses("()()(()())"))  
print(verifica_parenteses("( ) )"))  