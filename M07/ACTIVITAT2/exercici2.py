valor = float(input("Introdueix el valor en €: "))
while True:
    iva = float(input("Introdueix el % d'IVA (4, 10 o 21): "))
    if iva in [4, 10, 21]:
        break
    else:
        print("Si us plau, introdueix un IVA vàlid (4, 10 o 21).")

iva_total = valor * (iva / 100)
valor_final = valor + iva_total

print(f"Valor original: {valor}€, IVA aplicat: {iva}%, Valor final: {valor_final}€")
