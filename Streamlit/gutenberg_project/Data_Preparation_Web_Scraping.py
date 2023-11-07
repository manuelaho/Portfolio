
import streamlit as st
import pandas as pd
import requests

from bs4 import BeautifulSoup
 # fürs Encoden für html Dokumente
from bs4.dammit import EncodingDetector          


# In[37]:


BASE_URL = "https://www.projekt-gutenberg.org/"

# PRIVATE FUNKTIONEN


# Funktion, um Sätze mit weniger als 4 Wörtern zu ignorieren(_correction)

def _correction(string):
    
    if len(string) < 4:
        return None
    else:
        return string
    

# Bild scrapen(_find_image)

def _find_image(author_site):
    try:
        return f"{BASE_URL}autoren/{author_site.find('img', src = True, title = True)['src'][3:]}"
        
    except:
        return None



# Biographie scrapen(_find_info_bio)

# s = author_site.find_all("p")[1].text
# return s

def _find_info_bio(author_site):
    try:
        s = ""
        for para in author_site.find_all("p",{"class":None}):
            s += para.text
        return s

    except:
        return None

# HAUPTFUNKTION

# um Fehlermeldungen und Warnungen zu unterdrücken in streamlit
#st.cache_data()   
#@st.cache(suppress_st_warning=True)



def scrape_autor(author):
    
    url = f"{BASE_URL}autoren/namen/{author.lower()}.html"
    print(f"Scrape Autor {author} {url}")
    
    # html skript:
    res = requests.get(url)                                    
    
    # wenn unser Autor nicht gefunden wurde:
    if res.status_code != 200:
        print(f"Autor {author} wurde nicht gefunden!")
        return None
    
    # Scraping mit beautiful soup um html skript übersichtlicher zu machen mit Encoder "lxml"
    # und weiter encoden mit EncodingDetector from_encoding:
    try:
        print(f"Autor {author} wurde gefunden!")
        author_site = BeautifulSoup(res.content, 'lxml', 
                      from_encoding=EncodingDetector.find_declared_encoding(res.content, is_html=True))
        
    # Decoding Fehler angeben    
    except Exception:
        print("Error während dem Decoden")
        return None
 
    # Wörterbuch(dict) erstellen mit allen Informationen über unseren Autor:
    infos = {"data"      : None, 
             "books"     : _find_books(author_site),    # Funktion dafür bauen
             "info_bio"  : _find_info_bio(author_site), 
             "image_url" : _find_image(author_site)}    # Funktion dafür bauen
    
    
    # dataframe bauen und unsere gebauten Funktionen nutzen(siehe unter infos):
    df_all = pd.DataFrame()
    
    for title, url in infos["books"]:
        st.markdown(f"[{title}] ({url})")
        print(f"Scrape buch '{title}' [{url}]")
    
        # Buch scrapen:
        df_temp = _scrape_book(url)
        
        # jetzt in df_all packen:
        df_all = pd.concat([df_all, df_temp], ignore_index=True)
        
    # Autor noch hinzufügen:
    df_all["Autor"] = author.upper() 
    
    # fertiger Dataframe:
    infos["data"] = df_all
    
    print(f" Gefundene Sätze: {df_all.shape}")
    
    return infos


# Text der Unterkapitel scrapen(_find_text)

def _find_text(books):
    
    text = ""
    # findet alle HTML Paragraphe mit dem Tag <\p>:
    for paragraph in books.find_all("p"):
        if paragraph.string:
            text = text + paragraph.text
            
    return text






# In[39]:


# Liste an Buchtiteln und Url's scrapen(_find_book)

def _find_books(books):
    tag = books.find("div", {"class" : "archived"})
    if tag == None:
        return []
    
    book_url = []
    # die Bücher findet man unter der Liste mit dem Tag <li>
    for l in tag.find_all("li"):
        # wir greifen nur auf den Link zu
        tag = l.find("a", href = True) 
        book_title = tag.string
        # ab Index 6
        url = f"{BASE_URL}{tag['href'][6:]}"
        # aufhören hinten beim letzen Slash
        url = url[:url.rfind("/")]
        
        book_url.append((book_title, url))
        
    return book_url





# Liste an Unterkapiteln scrapen(_scrape_book)

def _scrape_book(url):
    
    res = requests.get(url) 
    
    book_site = BeautifulSoup(res.content, 'lxml', 
                from_encoding=EncodingDetector.find_declared_encoding(res.content, is_html=True))
    
    # alle li(Kapitel) im html code finden
    subchapters = book_site.find_all("li")
    print(f"\tAnzahl Unterkapitel: {len(subchapters)}")
    
    # nun brauchen wir jeden link von jedem Kapitel
    subchapters_links = []
    for sub in subchapters:
        link = sub.find("a", href = True)
        subchapters_links.append(url +  link["href"])
    
    # dataframe zusammenbauen für die einzelnen Sätze (muss dann noch gefüllt werden):
    df = pd.DataFrame(columns = ["Satz"])    
    
    # progressbar machen um das running auf streamlit(während die Bücher laden) anzuzeigen:
    # progressbar startet bei (0)
    progressbar = st.progress(0)
    
    # durch alle chapter durchgehen und progressbar damit füllen:
    for index, temp_url in enumerate(subchapters_links):
        progressbar.progress((index + 1)/len(subchapters_links))
        
        # homepage nochmal abrufen:
        res = requests.get(url) 
    
        books = BeautifulSoup(res.content, 'lxml', 
                from_encoding=EncodingDetector.find_declared_encoding(res.content, is_html=True))
        
        data = _find_text(books)           # diese Funktion müssen wir noch schreiben
        
        # nicht den ganzen Text reinladen, sondern einzelne Sätze:
        for satz in data.split("."):
            df.loc[len(df)] = satz        # loc macht jede Zeile ran, iloc hingegen in der Spalte
        
    # löschen der progressbar
    progressbar.empty()
    
    df["Satz"] = df["Satz"].map(_correction).dropna()
    
    return df







