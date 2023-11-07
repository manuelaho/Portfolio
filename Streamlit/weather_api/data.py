# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 10:15:09 2023
@author: Fujitsu
"""

import pandas as pd

# für json - Daten Funktionen schreiben

# Funktion tägliche Wetterdaten (Option 1):
    
def get_daily_data(data):
    
    if not isinstance(data, dict):                    # Überprüfung: Daten müssen Bestandteil eines dictionary sein
        print("Hier ist etwas schief gelaufen!")
        return None
    
    indices = []     # für Tage
    temp = []        # für Temperatur
    
    # drüber iterieren in days von json-Datei von "weather query builder"
    # https://www.visualcrossing.com/weather/weather-data-services/innsbruck?v=api
    for d in data["days"]:
       indices.append(d['datetime'])
       temp.append(d['temp'])
       
    # dataframe machen
    df = pd.DataFrame(data = {f"{data['address']}" : temp}, index = indices)
    
    return df



# Funktion stündliche Wetterdaten (Option 2):
    
def get_hourly_data(data):
    
    if not isinstance(data, dict):                    # Überprüfung: Daten müssen Bestandteil eines dictionary sein
        print("Hier ist etwas schief gelaufen!")
        return None
    
    indices = []     # für Tage
    temp = []        # für Temperatur
    
    for d in data["days"]:
        for h in d["hours"]:
            indices.append(f"{d['datetime']} {h['datetime']}")
            temp.append(h['temp'])
            
    df = pd.DataFrame(data = {f"{data['address']}" : temp}, index = indices)
    
    return df

