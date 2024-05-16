# Escreva um aplicativo que exibe uma caixa, uma oval, uma seta e um losango utilizando asteriscos (*). 

def exibir_caixa():
    print("Caixa:")
    print("******")
    print("*    *")
    print("*    *")
    print("******")
    print()

def exibir_oval():
    print("Oval:")
    print("  ***  ")
    print(" *   * ")
    print(" *   * ")
    print("  ***  ")
    print()

def exibir_seta():
    print("Seta:")
    print("   *   ")
    print("  ***  ")
    print(" ***** ")
    print("*******")
    print("   *   ")
    print()

def exibir_losango():
    print("Losango:")
    print("   *   ")
    print("  ***  ")
    print(" ***** ")
    print("  ***  ")
    print("   *   ")
    print()

if __name__ == "__main__":
    exibir_caixa()
    exibir_oval()
    exibir_seta()
    exibir_losango()