num = int(input("Introdueix un número entre 10 i 100: "))
if 10 <= num <= 100:
    tupla = tuple(range(1, num + 1))
    print("Tupla:", tupla)
else:
    print("El número no és vàlid.")
