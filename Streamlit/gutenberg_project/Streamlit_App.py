# FUNDAMENT BAUEN

import streamlit as st

from Data_Preparation_Web_Scraping import scrape_autor
from Machine_Learning_Model import analyze
#from scraping import scrape_autor
#from model import analyze



# Größe und Verteilung(layout)
st.set_page_config(layout = "wide")

# Titel mit Text und Link:
st.header("[PROJEKT GUTENBERG](https://www.projekt-gutenberg.org/)")
# zwei Streamlit-columns
col1, col2 = st.columns(2)

# session state - speichert alle Daten ab über Durchläufe bei streamlit

# bezieht sich auf den vectorizer unseres ML-Models


if "vect" not in st.session_state:
    st.session_state.vect = None
    
# bezieht sich auf das Modell Naive Bayes unseres ML-Models
if "model" not in st.session_state:
    st.session_state.model = None
    
# bezieht sich auf data unseres Scrapings:
if "data" not in st.session_state:
    st.session_state.data = {}


# LINKEN TEIL DER APP BAUEN - SIDEBAR

# Autor einfügen vom Nutzer mit vorausgeführten Autor und Hilfe:
autor = st.sidebar.text_input("Welche/r Autor/in interessiert dich?", value = "Kafka", help = "Der Nachname ist ausreichend!").upper()


# sidebar markdown zur session state
st.sidebar.markdown("""Durch die Verwendung der [session_state](https://docs.streamlit.io/library/api-reference/session-state) werden die Daten eines Autors nur **einmal** gescrapt. 
Bei nochmaliger Abfrage werden automatisch die schon existierenden Daten geladen.""")

# erster button für Starte Scraping mit Funktion scrape_autor
if st.sidebar.button("Starte Scraping...", help = "zum Scrapen button drücken"):
    
    # wenn sich Autor nicht in session_state befindet:
    if autor not in st.session_state.data.keys():
        
        data = scrape_autor(autor)
        
        if data == None:
            st.error("Der Autor ist in der Datenbank nicht vorhanden!")
            
        # wenn Autor drinnen ist: Daten speichern    
        else:
            st.session_state.data[autor.upper()] = data
    else:
        print("Autor ist bereits extrahiert worden!")
            
# zweiter button für Daten löschen:
if st.sidebar.button("Lösche Daten", help = "löscht alle extrahierten Daten", disabled=len(st.session_state.data.keys())==0):
    st.session_state.data = {}
    

# MITTLEREN TEIL DER APP BAUEN

with col1:
    
    # Informationen über den Autor:(Text und Bild):
    if autor in st.session_state.data.keys():
        
        st.subheader("Biographie")
        st.write(st.session_state.data[autor.upper()]["info_bio"])  ######

        if st.session_state.data[autor.upper()]["image_url"]:
            st.image(st.session_state.data[autor.upper()]["image_url"])
            
        # alle Sätze der Bücher - gesamtes dataframe angeben:
        st.dataframe(st.session_state.data[autor.upper()]["data"],width=600)
        # Bücher anzeigen lassen:
        # Link immer in runden Klammer anzeigen lassen
        st.subheader("Bücher")
        
        for b in st.session_state.data[autor.upper()]["books"]:
            st.markdown(f"[{b[0]}]({b[1]})") 
            

# RECHTEN TEIL DER APP BAUEN - DATA SCIENCE

with col2:

    # Box zum Auswählen der Autoren:
    selection = st.multiselect("Autoren", st.session_state.data.keys())
    # Analyze button:
    analyse = st.button("Analysiere ausgewählte Autoren", help="Erstellt ein Modell mit den ausgewählten Autoren.")

    if analyse and selection!= []:
        m={}    

        for sel in selection:
            m[sel] = st.session_state.data[sel]
    
        if m!={}:
            st.session_state.model, st.session_state.vect = analyze(m)

    text = st.text_input("Wer hat es (wahrscheinlich) geschrieben?" )
    
    # machine learning model durchlaufen lassen:
    if st.session_state.model != None and st.session_state.vect != None:
        propas = st.session_state.model.predict_proba(st.session_state.vect.transform([text]))

        for i in range(len(st.session_state.model.classes_)):
            st.markdown(f"**{st.session_state.model.classes_[i]}**: {propas[0][i]*100:.2f} % ")
            


