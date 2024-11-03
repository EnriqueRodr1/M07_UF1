import matplotlib.pyplot as plt

def plot_cases(resultats):
    for pais, dades in resultats.items():
        plt.plot(dades.index, dades.values, label=pais)
    plt.title('Total de casos per mes per país')
    plt.xlabel('Data')
    plt.ylabel('Total de casos')
    plt.legend()
    plt.show()

def plot_deaths(resultats):
    for pais, dades in resultats.items():
        plt.plot(dades.index, dades.values, label=pais)
    plt.title('Morts totals per mes per país')
    plt.xlabel('Data')
    plt.ylabel('Morts totals')
    plt.legend()
    plt.show()

def plot_reproduction_rate(resultats):
    for pais, dades in resultats.items():
        plt.plot(dades.index, dades.values, label=pais)
    plt.title('Reproduction rate per mes per país')
    plt.xlabel('Data')
    plt.ylabel('Reproduction rate')
    plt.legend()
    plt.show()
