import csv

agenda = {}
lista_dados = ["nome", "telefone", "email", "data de nascimento"]
arquivo_csv = "agenda.csv"

# Função para adicionar um novo contato à agenda
def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    datanasc = input("Data de Nascimento: ")
    contato = [nome, telefone, email, datanasc]
    agenda[nome] = contato
    print(f"Contato de {nome} foi salvo com sucesso!")

# Função para alterar um contato existente na agenda
def alterar_contato(nome):
    if nome in agenda:
        contato = agenda[nome]
        for i, parametro in enumerate(lista_dados):
            if input(f"Quer alterar o {parametro.capitalize()}? Digite Y para sim, ou N para não: ").upper() == 'Y':
                contato[i] = input(f"Qual novo {parametro.capitalize()}: ")
        apagar_contato(nome)
        agenda[nome] = contato
        print(f"O contato {nome} foi alterado: {contato}!")
    else:
        print(f"O contato {nome} não existe na agenda!")

# Função para apagar um contato da agenda
def apagar_contato(nome):
    if nome in agenda:
        contato = agenda.pop(nome)
        print(f"O contato {nome} foi apagado com sucesso!")
        return contato
    else:
        print(f"O contato {nome} não existe na agenda!")

# Função para buscar um contato na agenda
def buscar_contato(nome):
    if nome in agenda:
        return agenda[nome]
    else:
        print(f"O contato {nome} não existe na agenda!")

# Função para listar todos os contatos na agenda
def listar_contatos():
    print(f"A agenda tem {len(agenda)} contatos")
    for contato in agenda.values():
        print(contato)

# Função para salvar a agenda em um arquivo CSV
def salvar_agenda_csv():
    with open(arquivo_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(lista_dados)
        for contato in agenda.values():
            writer.writerow(contato)
    print("Agenda salva com sucesso!")

# Função para carregar a agenda de um arquivo CSV
def carregar_agenda_csv():
    try:
        with open(arquivo_csv, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            for row in reader:
                contato = row
                agenda[contato[0]] = contato
        print("Agenda carregada com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de agenda encontrado. Começando com agenda vazia.")

# Carregar a agenda do arquivo CSV ao iniciar o programa
carregar_agenda_csv()

# Loop principal do programa
while True:
    # Menu de opções
    opcao = int(input("""
        *****************************************************
        **                                                 **
        **                  Agenda Pessoal                 **
        **                                                 **
        **           1 - Adicionar Contato                 **
        **           2 - Alterar Contato                   **
        **           3 - Buscar Contato                    **
        **           4 - Apagar Contato                    **
        **           5 - Listar Contatos                   **
        **                                                 **
        **           0 - Sair                               **
        **                                                 **
        *****************************************************

    Digite o número correspondente à operação desejada: """))

    # Executar a operação escolhida pelo usuário
    if opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        nome = input("Qual contato deseja alterar? ")
        alterar_contato(nome)
    elif opcao == 3:
        nome = input("Qual contato deseja buscar? ")
        buscar_contato(nome)
    elif opcao == 4:
        nome = input("Qual contato deseja apagar? ")
        apagar_contato(nome)
    elif opcao == 5:
        listar_contatos()
    elif opcao == 0:
        salvar_agenda_csv()
        break
    else:
        print("Operação inválida!")
