pet1 = {
    "nome": "Toddy",
    "tipo": "Cachorro",
    "dono": "Arthur"
}

pet2 = {
    "nome": "Miau",
    "tipo": "Gato",
    "dono": "Pedro"
}

pet3 = {
    "nome": "Fufu",
    "tipo": "Papagaio",
    "dono": "Clara"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Nome do animal: {pet['nome']}")
    print(f"Tipo do animal: {pet['tipo']}")
    print(f"Dono do animal: {pet['dono']}\n")