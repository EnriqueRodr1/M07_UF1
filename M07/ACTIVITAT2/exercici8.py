# exercici8.py
paraules = input("Introdueix entre 1 i 3 paraules: ").split()

if 1 <= len(paraules) <= 3:
    for paraula in paraules:
        print(f"Paraula: {paraula}")
        print(f"Nombre de caràcters: {len(paraula)}")
        print(f"Primer caràcter: {paraula[0]}")
        print(f"Últim caràcter: {paraula[-1]}")
else:
    print("Has d'introduir entre 1 i 3 paraules.")

