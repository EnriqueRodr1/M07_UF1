# exercici7.py
contactes = {}
while True:
    nom = input("Introdueix un nom (o 'no' per acabar): ")
    if nom.lower() == 'no':
        break
    edat = int(input("Introdueix l'edat: "))
    if nom not in contactes:
        contactes[nom] = edat
    else:
        print(f"El nom '{nom}' ja existeix al diccionari.")
print("Contactes:", contactes)
