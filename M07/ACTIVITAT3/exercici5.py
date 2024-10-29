# exercici5.py
frase = input("Introdueix una frase: ")
sense_espais = ''.join(frase.split())
tupla_frase = tuple(sense_espais)
sense_repetits = ''.join(sorted(set(sense_espais), key=sense_espais.index))
print("Tupla sense espais:", tupla_frase)
print("Frase sense caràcters repetits:", sense_repetits)
