sandwich_orders = ["Atum", "Frango", "Vegetariano", "Queijo", "Presunto"]

finished_sandwiches = []

for pedido in sandwich_orders:
    print(f"Preparando seu sanduíche de {pedido}...")
    finished_sandwiches.append(pedido)

print("\nSanduíches prontos:")
for sanduiche in finished_sandwiches:
    print(f"- {sanduiche}")