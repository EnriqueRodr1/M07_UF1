import numpy as np

def crear_matriu():
    matriu = np.zeros((50, 50))  # Creem una matriu de 50x50 plena de zeros
    np.fill_diagonal(matriu, range(50))  # Afegim els números de la diagonal
    np.save('exercici1.py', matriu)  # Guardem la matriu en un arxiu
    return matriu

if __name__ == "__main__":
    matriu = crear_matriu()
    print("Matriu creada:")
    print(matriu)
    print("Dimensions de la matriu:", matriu.shape)
    print("Tamany de la matriu:", matriu.size)
    print("Número total d'elements:", matriu.size)
    print("Tipus d'elements interns:", matriu.dtype)
