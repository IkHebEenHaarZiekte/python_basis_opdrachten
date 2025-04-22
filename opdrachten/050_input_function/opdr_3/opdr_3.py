# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

mylist = []

for i in range(5):
    object = input(f"Vul object {i+1} in: ")
    mylist.append(object)

    mylist_sorted = sorted(mylist, reverse=True)
    print(mylist_sorted)