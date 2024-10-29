# exercici8.py
numeros = list(map(int, input("Introdueix 10 números separats per espai: ").split()))
if len(numeros) == 10:
    suma_total = sum(numeros)
    mitjana = suma_total / len(numeros)
    numeros.extend([suma_total, mitjana])
    print("Números de l'usuari:", numeros[:10])
    print("Suma total:", suma_total)
    print("Mitjana:", mitjana)
    print("Llista completa:", numeros)
else:
    print("Has d'introduir exactament 10 números.")
