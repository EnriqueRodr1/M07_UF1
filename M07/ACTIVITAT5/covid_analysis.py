import pandas as pd

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
