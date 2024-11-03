import numpy as np

def generar_matriu(dimensions):
    matriu = np.random.randint(0, 100, size=dimensions)
    print("Matriu original:")
    print(matriu)
    return matriu

def max_valor(matriu):
    return np.max(matriu)

def min_valor(matriu):
    return np.min(matriu)

if __name__ == "__main__":
    rows = int(input("Introdueix el nombre de files: "))
    cols = int(input("Introdueix el nombre de columnes: "))
    
    matriu = generar_matriu((rows, cols))
    
    print("Valor màxim:", max_valor(matriu))
    print("Valor mínim:", min_valor(matriu))
