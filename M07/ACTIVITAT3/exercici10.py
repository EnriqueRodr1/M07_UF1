# exercici10.py
abecedari = list("abcdefghijklmnopqrstuvwxyz")
abecedari_filtrat = [lletra for i, lletra in enumerate(abecedari) if (i + 1) % 3 != 0]
abecedari_tupla = tuple(abecedari_filtrat)
print("Llista sense múltiples de 3:", abecedari_filtrat)
print("Tupla sense múltiples de 3:", abecedari_tupla)
