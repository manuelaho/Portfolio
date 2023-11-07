import streamlit as st
from random import randint


st.header("ZUFALLSZAHLEN ERZEUGEN")


mini = st.slider("Minimaler Wert:", 0, 10, key = 1)

maxi = st.slider("Maximaler Wert:", 0, 20, key = 2)

anzahl = st.slider("Wieviele Zufallszahlen möchtest du erzeugen?", 1, 12, key = 3)


zufallszahlen = []


btn = st.button("Zufallszahlen erzeugen:")
if btn:     
    for i in range(1, anzahl + 1):
        st.write("•", randint(mini, maxi), ":sunglasses:")

