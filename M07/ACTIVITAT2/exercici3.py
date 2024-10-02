valor1 = float(input("Introdueix el primer valor: "))
valor2 = float(input("Introdueix el segon valor: "))

if valor1 > valor2:
    print(f"El valor més gran és {valor1}")
elif valor2 > valor1:
    print(f"El valor més gran és {valor2}")
else:
    print("Els dos valors són iguals")
