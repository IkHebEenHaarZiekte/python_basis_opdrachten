# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizza_list = ["margharita", "calzone", "verdi", "olivio", "quattro stagioni"]

pizza_list.sort()
print(pizza_list)

pizza_list.append("yo-favorito")
print(pizza_list)

pizza_list.remove("olivio")
print(pizza_list)

print(pizza_list[:3])

middle_index = len(pizza_list) // 2
print([pizza_list[middle_index]])

print(pizza_list[-3:])