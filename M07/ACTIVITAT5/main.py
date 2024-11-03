import pandas as pd
import matplotlib.pyplot as plt

# Funciones para análisis de COVID
def casos_totals_per_mes(df, paisos):
    resultats = {}
    for pais in paisos:
        dades_pais = df[df['country'] == pais].groupby('date')['total_cases'].sum()
        resultats[pais] = dades_pais
    return resultats

def morts_totals_per_mes(df, paisos):
    resultats = {}
    for pais in paisos:
        dades_pais = df[df['country'] == pais].groupby('date')['total_deaths'].sum()
        resultats[pais] = dades_pais
    return resultats

def reproduction_rate_per_mes(df, paisos):
    resultats = {}
    for pais in paisos:
        dades_pais = df[df['country'] == pais].groupby('date')['reproduction_rate'].mean()
        resultats[pais] = dades_pais
    return resultats

# Funciones de visualización para COVID
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

# Funciones para análisis de ciudades
def poblacio_per_ciutat(df, ciutats):
    resultats = {}
    for ciutat in ciutats:
        poblacio = df[df['city'] == ciutat]['population'].values[0]
        resultats[ciutat] = poblacio
    return resultats

def densitat_km2(df, ciutats):
    resultats = {}
    for ciutat in ciutats:
        densitat = df[df['city'] == ciutat]['density_km2'].values[0]
        resultats[ciutat] = densitat
    return resultats

def densitat_m2(df, ciutats):
    resultats = {}
    for ciutat in ciutats:
        densitat = df[df['city'] == ciutat]['density_m2'].values[0]
        resultats[ciutat] = densitat
    return resultats

# Funciones de visualización para ciudades
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

# Funciones para análisis de móviles
def clock_speed(df, ids):
    resultats = {}
    for id in ids:
        speed = df[df['id'] == id]['clock_speed'].values[0]
        resultats[id] = speed
    return resultats

def megapixels(df, ids):
    resultats = {}
    for id in ids:
        mp = df[df['id'] == id]['megapixels'].values[0]
        resultats[id] = mp
    return resultats

def battery_power(df, ids):
    resultats = {}
    for id in ids:
        battery = df[df['id'] == id]['battery_power'].values[0]
        resultats[id] = battery
    return resultats

# Funciones de visualización para móviles
def plot_clock_speed(resultats):
    ids = list(resultats.keys())
    speeds = list(resultats.values())
    plt.bar(ids, speeds)
    plt.title('Clock Speed per ID')
    plt.xlabel('ID')
    plt.ylabel('Clock Speed (MHz)')
    plt.show()

def plot_megapixels(resultats):
    ids = list(resultats.keys())
    megapixels_values = list(resultats.values())
    plt.bar(ids, megapixels_values)
    plt.title('Megapixels per ID')
    plt.xlabel('ID')
    plt.ylabel('Megapixels')
    plt.show()

def plot_battery_power(resultats):
    ids = list(resultats.keys())
    battery_values = list(resultats.values())
    plt.bar(ids, battery_values)
    plt.title('Battery Power per ID')
    plt.xlabel('ID')
    plt.ylabel('Battery Power (mAh)')
    plt.show()

# Función principal
def main():
    # Análisis de COVID
    df_covid = pd.read_csv('data/covid_data.csv')
    paisos = ['Spain', 'Italy', 'Germany', 'France', 'USA', 'Brazil', 'India', 'UK', 'Russia', 'Canada']
    casos = casos_totals_per_mes(df_covid, paisos)
    morts = morts_totals_per_mes(df_covid, paisos)
    reproduction = reproduction_rate_per_mes(df_covid, paisos)
    
    plot_cases(casos)
    plot_deaths(morts)
    plot_reproduction_rate(reproduction)

    # Análisis de Ciudades
    df_cities = pd.read_csv('data/cities_data.csv')
    ciutats = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai', 'Cairo', 'Dhaka', 'Mexico City', 'Beijing', 'Osaka']
    poblacio = poblacio_per_ciutat(df_cities, ciutats)
    densitat_km2_resultats = densitat_km2(df_cities, ciutats)
    densitat_m2_resultats = densitat_m2(df_cities, ciutats)
    
    plot_population(poblacio)
    plot_density_km2(densitat_km2_resultats)
    plot_density_m2(densitat_m2_resultats)

    # Análisis de Móviles
    df_mobiles = pd.read_csv('data/mobile_data.csv')
    ids = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
    clock_speeds = clock_speed(df_mobiles, ids)
    megapixels_values = megapixels(df_mobiles, ids)
    battery_values = battery_power(df_mobiles, ids)
    
    plot_clock_speed(clock_speeds)
    plot_megapixels(megapixels_values)
    plot_battery_power(battery_values)

if __name__ == '__main__':
    main()
