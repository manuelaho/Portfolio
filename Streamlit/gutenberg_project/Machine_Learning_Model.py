#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

# um Text in numerische Werte umzuwandeln(Vektorisierung des Textes) verwendet man CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
# gut geeignet für Textklassifizierung
from sklearn.naive_bayes import MultinomialNB


# In[5]:


def analyze(data):
    
    # leeres dataframe erstellen:
    df = pd.DataFrame()
    # wir iterieren über data(von info-Variable aus der Funktion scrape_autor):
    for i in data.values():
        df = pd.concat([df, i["data"]], ignore_index= True)
        # Nullwerte sicherheitshalber löschen
        df = df.dropna()
        
        # CountVectorizer:
        vect = CountVectorizer()
        # Wörter in Zahlen umwandeln:
        wordsCountArray = vect.fit_transform(df["Satz"])
        
        # x = wordsCountArray, y = df["Autor"]
        X_train, X_test, y_train, y_test = train_test_split(wordsCountArray,df["Autor"],test_size=0.2,random_state=0)
        
        # trainieren:
        model = MultinomialNB
        model.fit(X_train, y_train)
        
        # Modell trainiert für Autoren als Ausgabe bei streamlit:
        autoren = data.keys()
        s = f"Modell trainiert für Autoren: \n\n"
        
        # Autoren bei streamlit ausgeben, die analysiert werden:(\t ist Tabulator):
        for i in autoren:
            s+= f"\t{i}\n"
            
        # Ausgabe wie viele Sätze wir haben in streamlit:
        s+= f"Mit {X_train.shape[0]} Sätzen. \n\n"
        
        # Ausgabe Modellgenauigkeit in streamlit:
        s+= f"Modellgenauigkeit: {model.score(X_test, y_test)*100:.2f}%."
        
        # s in streamlit übergeben:
        st.markdown(s)
        
        return model, vect


# In[ ]:




