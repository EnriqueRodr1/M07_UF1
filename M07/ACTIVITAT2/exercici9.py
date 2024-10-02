# exercici9.py
paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

nova_paraula1 = paraula2[:2] + paraula1[2:]
nova_paraula2 = paraula1[:2] + paraula2[2:]

print(f"Resultat: {nova_paraula1} {nova_paraula2}")

