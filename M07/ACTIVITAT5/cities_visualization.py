import matplotlib.pyplot as plt

def plot_population(resultats):
    ciutats = list(resultats.keys())
    poblacions = list(resultats.values())
    plt.bar(ciutats, poblacions)
    plt.title('Població per ciutat')
    plt.xlabel('Ciutat')
    plt.ylabel('Població')
    plt.xticks(rotation=45)
    plt.show()

def plot_density_km2(resultats):
    ciutats = list(resultats.keys())
    densitats = list(resultats.values())
    plt.bar(ciutats, densitats)
    plt.title('Densitat per KM² per ciutat')
    plt.xlabel('Ciutat')
    plt.ylabel('Densitat (persones/km²)')
    plt.xticks(rotation=45)
    plt.show()

def plot_density_m2(resultats):
    ciutats = list(resultats.keys())
    densitats = list(resultats.values())
    plt.bar(ciutats, densitats)
    plt.title('Densitat per M² per ciutat')
    plt.xlabel('Ciutat')
    plt.ylabel('Densitat (persones/m²)')
    plt.xticks(rotation=45)
    plt.show()
