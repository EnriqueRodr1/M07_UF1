import numpy as np

def crear_matriu1():
    return np.random.randint(0, 100, size=(3, 4))

def crear_matriu2():
    return np.random.randint(100, 200, size=(4, 3))

def crear_matriu3():
    return np.random.randint(200, 300, size=(2, 6))

if __name__ == "__main__":
    matriu1 = crear_matriu1()
    matriu2 = crear_matriu2()
    matriu3 = crear_matriu3()

    print("Matriu 1:")
    print(matriu1)
    print("Número total d'elements Matriu 1:", matriu1.size)
    print("Dimensions Matriu 1:", matriu1.shape)
    print("Tipus d'elements interns Matriu 1:", matriu1.dtype)
    print("Tamany Matriu 1:", matriu1.size)

    print("\nMatriu 2:")
    print(matriu2)
    print("Número total d'elements Matriu 2:", matriu2.size)
    print("Dimensions Matriu 2:", matriu2.shape)
    print("Tipus d'elements interns Matriu 2:", matriu2.dtype)
    print("Tamany Matriu 2:", matriu2.size)

    print("\nMatriu 3:")
    print(matriu3)
    print("Número total d'elements Matriu 3:", matriu3.size)
    print("Dimensions Matriu 3:", matriu3.shape)
    print("Tipus d'elements interns Matriu 3:", matriu3.dtype)
    print("Tamany Matriu 3:", matriu3.size)
