import pandas as pd

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
