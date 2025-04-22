# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Jij", "Kees", "Marie", "Hilda"]

gasten.insert(0, "jij")
print(gasten)

gasten.remove("Marie")
print(gasten)

index_kees = gasten.index ("Kees")
gasten.insert(index_kees + 1, "George")
print(gasten)
