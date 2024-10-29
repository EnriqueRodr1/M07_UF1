# exercici3.py
num = int(input("Introdueix un número de l'1 al 10: "))
if 1 <= num <= 10:
    taula = [num * i for i in range(1, 11)]
    print("Taula de multiplicar de", num, ":", taula)
else:
    print("Número no vàlid.")
