# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
from operator import truediv

prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

pogingen = 0
geraden = False

while not geraden:
    gok = int(input(prompt))
    pogingen += 1

    if gok < geheim_getal:
        print("Hoger")
    elif gok > geheim_getal:
        print("Lager")
    else:
        print(f"Je hebt het getal geraden het is {geheim_getal}")
        print(f"Je hebt het in {pogingen} keer gedaan")
        geraden = True

# De rest moet jij doen.....

