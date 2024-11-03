import matplotlib.pyplot as plt

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
