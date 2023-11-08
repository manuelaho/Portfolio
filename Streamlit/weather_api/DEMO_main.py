# -*- coding: utf-8 -*-
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from io import BytesIO                 # ein Hack, um Schaubild darzustellen

import api                                         # unser Modul zur Kommunikation mit api
from data import get_hourly_data, get_daily_data    # unser Modul zur Verarbeitung der API-Daten


st.set_page_config(layout = "wide")                       # Befehl um layout - Typ zu erstellen

sns.set_theme(style = "whitegrid")

st.header("WETTERAPP")                                                       # header erstellen
st.write("Hier kannst du die Temperatur an beliebigen Orten vergleichen!")   # Erklärung

# Sidebar bauen (seitlich links) um anzuwählen:
st.sidebar.header("Informationen")

map = st.sidebar.checkbox("Weltkarte anzeigen")

cities = st.sidebar.text_input("Wähle eine Stadt aus:", placeholder = "bitte Namen der Stadt eintragen")

datestart = st.sidebar.date_input("Start")

dateend = st.sidebar.date_input("Ende")

intervall = st.sidebar.selectbox("Genauigkeit der Daten", ["Stunden", "Tage"])

dataframes = []                                    # für jede Stadt ein Dataframe
gps = pd.DataFrame(columns = ["lat", "lon"])       # speichern Städte für st.map, lat + lon = Längen- und Breitengrade


# Daten anzeigen in streamlit in 2 Spalten(Daten Visualisierung + Karte)
col1, col2 = st.columns([2, 1])     # Größe 2 für Daten Visualisierung und 1 für Karte

with col1:
    
    if cities:
        for city in cities.split():
            data = api_Kopie.fetch_data_for_city(city, datestart, dateend)
            gps.loc[len(gps) + 1] = [data["latitude"], data["longitude"]]


        if intervall == "Stunden":              # stündliche Darstellung
            df = get_hourly_data(data)
        elif intervall == "Tage":               # tägliche Darstellung
            df = get_daily_data(data)
        
        dataframes.append(df)                   # speichern der Daten
        

    # Plotten der Daten in einer Matplotlib-Figure

    fig, ax1 = plt.subplots(figsize = (6, 6))
    
    for d in dataframes:
        d.plot(kind = "line", ax = ax1, ylabel = "Temperatur", xlabel = "Datum", rot = 90, fontsize = 8)
        
        if intervall == "Stunden":
            ticks = range(0, len(d), 24)
        elif intervall == "Tage":
            ticks = range(0, len(d))
            
        
    
    # als Bild abspeichern
    buf = BytesIO()
    fig.savefig(buf, format = "png")

    st.image(buf)

    

with col2:
    
    if map:
        st.header("Landkarte")
        st.map(gps)
