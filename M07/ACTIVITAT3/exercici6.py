# exercici6.py
areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Segon element:", areas_pis[1])
print("Últim element:", areas_pis[-1])
print("Àrea de la terrassa:", areas_pis[7])
print("Del primer al tercer element:", areas_pis[:3])
print("Del tercer element a l'últim:", areas_pis[2:])
print("Total àrea de les dues habitacions:", areas_pis[5] + areas_pis[11])

areas_pis[9] = 8.5  # Modificant l'àrea del lavabo
print("Nova àrea:", areas_pis)

areas_pis.extend(["Pati interior", 2.78])
print("Nova àrea amb pati:", areas_pis)

total_area = sum(area for area in areas_pis if isinstance(area, (int, float)))
print("Àrea total del pis:", total_area)
