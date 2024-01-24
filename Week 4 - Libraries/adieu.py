import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except (EOFError, KeyError, TypeError):
        break

list_of_names = p.join(names)
print(f"Adieu, adieu, to {list_of_names}")
