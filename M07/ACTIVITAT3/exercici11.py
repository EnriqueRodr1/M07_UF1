# exercici11.py
divises = {"Euro": "€", "Dòlar": "$", "Ien": "¥", "Lliura": "£"}
divisa = input("Introdueix una divisa: ").capitalize()
if divisa in divises:
    print(f"El símbol de {divisa} és {divises[divisa]}")
else:
    print("La divisa no està al diccionari.")
