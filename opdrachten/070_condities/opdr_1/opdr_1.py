# Opdracht 1 condities
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

# Hier start de for-loop....

my_list = []

for i in range (1, 11):
    my_list.append(i)

    groter_dan_vier = []

    for getal in my_list:
        if getal > 4:
            groter_dan_vier.append(getal)

            print(groter_dan_vier)

#for loop
#if statement