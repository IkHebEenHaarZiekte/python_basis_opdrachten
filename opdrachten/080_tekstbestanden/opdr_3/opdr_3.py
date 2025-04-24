# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encrypt_tekst(tekst, verschuiving):
    resultaat = ""

    for teken in tekst:
        if teken.isalpha():
            basis = ord('A') if teken.isupper() else ord('a')
            verschoven = (ord(teken) - basis + verschuiving) % 26 + basis
            resultaat += chr(verschoven)
        else:
            resultaat += teken

    return resultaat

invoer = input("Geef de tekst die je wilt encrypten..\n")

gecodeert = encrypt_tekst(invoer, 5)

print("\nGeëncrypte tekst:")
print(gecodeert)
