# exercici4.py
valor1 = float(input("Introdueix el primer valor: "))
valor2 = float(input("Introdueix el segon valor: "))

operacio = input("Introdueix l'operació (+, -, *, /): ")

if operacio == "+":
    resultat = valor1 + valor2
elif operacio == "-":
    resultat = valor1 - valor2
elif operacio == "*":
    resultat = valor1 * valor2
elif operacio == "/":
    if valor2 != 0:
        resultat = valor1 / valor2
    else:
        resultat = "No es pot dividir per zero."
else:
    resultat = "Operació no vàlida."

print(f"El resultat és: {resultat}")
