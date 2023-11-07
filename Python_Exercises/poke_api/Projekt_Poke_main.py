# -*- coding: utf-8 -*-



import streamlit as st
from Projekt_Poke_api import fetch_data

st.set_page_config(layout = "wide")

st.header("POKEMONS")
st.write("Hier kannst du verschiedene Pokemons sehen!", ":sunglasses:")

btn1 = st.button("Drück mich!")
if btn1:     
    st.info("Gib links dein gewünschtes Pokemon ein!")
    st.balloons()

# Input des Users
name = st.sidebar.text_input("Name des Pokemons von Interesse:")


# Daten von der API abfragen
data = fetch_data(name)


# Daten visualisieren
st.header("Informationen zu deinem gewählten Pokemon:")

st.sidebar.write(data)
st.write(f"NAME DES POKEMON:   {name}")

st.image(data["sprites"]["versions"]["generation-i"]["red-blue"]["front_default"])


st.subheader("Fähigkeiten:")
st.write("1.", data["abilities"][0]["ability"]["name"])
st.write("2.", data["abilities"][1]["ability"]["name"])   
    
    
st.subheader("Eigenschaften:")
col1, col2 = st.columns([1, 2])

with col1:
    st.write("Gewicht")
    st.subheader(data["weight"])

with col2:
    st.write("Größe")
    st.subheader(data["height"])