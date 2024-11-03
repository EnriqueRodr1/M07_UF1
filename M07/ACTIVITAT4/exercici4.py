import numpy as np
from exercici2 import crear_matriu1, crear_matriu2, crear_matriu3

def crear_matriu_aleatoria():
    return np.random.randint(0, 80, size=(3, 4))

def modificar_matriu(matriu):
    nova_matriu = np.transpose(matriu)
    nova_matriu = np.column_stack((nova_matriu, nova_matriu[:, -1]))
    return nova_matriu

if __name__ == "__main__":
    matriu1 = crear_matriu_aleatoria()
    print("Matriu inicial aleatòria:")
    print(matriu1)

    matriu_modificada = modificar_matriu(matriu1)
    print("Matriu modificada:")
    print(matriu_modificada)
