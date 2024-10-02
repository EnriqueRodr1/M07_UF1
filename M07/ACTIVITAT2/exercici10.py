# exercici10.py
import random

numero_secret = random.randint(1, 100)
intents = 0

while True:
    intents += 1
    numero = int(input("Endevina el número (entre 1 i 100): "))

    if numero < numero_secret:
        print("Més gran!")
    elif numero > numero_secret:
        print("Més petit!")
    else:
        print(f"Has encertat! El número era {numero_secret}. Nombre d'intents: {intents}")
        break

