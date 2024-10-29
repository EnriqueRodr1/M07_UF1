# exercici9.py
assignatures = ["Matemàtiques", "Català", "Anglès", "Història", "Ciències", "Educació Física"]
notes = []

# Versió 1
for assignatura in assignatures:
    nota = float(input(f"Introdueix la nota de {assignatura}: "))
    notes.append(nota)

for i, assignatura in enumerate(assignatures):
    print(f"A {assignatura} ha tret {notes[i]}.")

# Versió 2 amb diccionari
notas_dict = {assignatura: float(input(f"Introdueix la nota de {assignatura}: ")) for assignatura in assignatures}
for assignatura, nota in notas_dict.items():
    print(f"A {assignatura} ha tret {nota}.")
