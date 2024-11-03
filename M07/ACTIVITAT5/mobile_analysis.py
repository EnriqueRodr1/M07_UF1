import pandas as pd

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
