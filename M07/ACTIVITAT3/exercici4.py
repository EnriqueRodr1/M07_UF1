# exercici4.py
numeros = input("Introdueix 10 números separats per espai: ").split()
if len(numeros) == 10:
    tupla = tuple(sorted(map(int, numeros)))
    print("Tupla ordenada:", tupla)
else:
    print("Has d'introduir exactament 10 números.")
