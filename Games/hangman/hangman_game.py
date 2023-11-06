#!/usr/bin/env python
# coding: utf-8

# In[17]:


def zufällig_wort(zahl_buchst):
    
    mögliche_wörter = []
    for i in cur.execute(f"SELECT * FROM words WHERE letters = {zahl_buchst}"):
        
            mögliche_wörter.append(i[0])
    return choice(mögliche_wörter)


# In[18]:


def buchst_tausch(such_wort, user_buchst, user_wort):
    
    akt_wort_liste = [] 
    
    for a in range(len(such_wort)):
        if not such_wort[a] == "_":
            akt_wort_liste.append(such_wort[a])
        elif such_wort[a] == "_" and user_buchst == user_wort[a]:
            akt_wort_liste.append(user_buchst)            
        else:
            akt_wort_liste.append("_") 
    
    word = ""
    for i in akt_wort_liste:
        word+= i
    
    return word


# In[19]:


def hängen(fehler):
    if fehler == 1:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| ")
        print("| ")
        
    elif fehler == 2:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("|  | ")
        print("| ")
        
    elif fehler == 3:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| ")
        
    elif fehler == 4:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| / ")
        
    elif fehler == 5:
        print("________ ")
        print("|  | ")
        print("|  0 ")
        print("| /|\ ")
        print("| / \ ")
        print("Du hast das Spiel leider verloren....")
        


# In[20]:


from random import choice
import sqlite3

connection = sqlite3.connect("my_database.db")
cur = connection.cursor()

aktiv = True

while aktiv:
    
    print("Eine neue Runde Hangman!\nWähle die Anzahl der Buchstaben, die das Wort enthalten soll,\noder gib EXIT ein, wenn das Spiel beendet werden soll.")
    user_wahl = input("Wie viele Buchstaben soll das Wort haben?")
    if user_wahl.upper() == "EXIT":
        print("Das Spiel wurde beendet!")
        aktiv = False
        connection.close()
        
    else:
        print("Ein Wort wurde ausgewählt...\nDie Raterunde beginnt!\nDu hast 5 Versuche, das Wort herauszufinden!\nViel Spaß!")
        user_wort = zufällig_wort(int(user_wahl))
        
        such_wort = "_" * len(user_wort)
        print(f"{such_wort} , {len(user_wort)} Buchstaben sind gesucht.\n")

        fehler = 1
        
        while fehler < 6:
            
            user_buchst = input("Welchen Buchstaben wählst Du?").upper()
            
            if user_buchst in user_wort and not user_buchst in such_wort:
                
                such_wort = buchst_tausch(such_wort,user_buchst,user_wort)
                print(such_wort)
                if user_wort == such_wort:
                    print("Geschafft!")
                    fehler = 6
                    
            elif user_buchst.upper() == "EXIT":
                print("Das Spiel wurde beendet.")
                aktiv = False
                fehler = 6
                                
            elif not user_buchst in user_wort:
                if fehler == 5:
                    hängen(fehler)
                    break                    
                print(f"{user_buchst} ist leider nicht vorhanden, du kannst dir noch {5 - fehler} Fehler erlauben!")
                hängen(fehler)
                fehler += 1
               
                print(such_wort)


# In[10]:





# In[ ]:




