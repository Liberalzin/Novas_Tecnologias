pessoa1 = {
    "first_name": "Arthur",
    "last_name": "Liberal",
    "age": 25,
    "city": "Rio de Janeiro"
}

pessoa2 = {
    "first_name": "Bia",
    "last_name": "Perereira",
    "age": 30,
    "city": "Goiania"
}

people = [pessoa1, pessoa2]

for pessoa in people:
    print(f"Nome completo: {pessoa['first_name']} {pessoa['last_name']}")
    print(f"Idade: {pessoa['age']} anos")
    print(f"Cidade: {pessoa['city']}\n")