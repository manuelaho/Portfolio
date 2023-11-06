#!/usr/bin/env python
# coding: utf-8

# In[29]:


import sqlite3
connection = sqlite3.connect("my_database.db")
cur = connection.cursor()

aktiv = True

while aktiv:

    user_eingabe = input("Welches Wort soll der Datenbank hinzugefügt werden: (oder EXIT)\n")
    wort = user_eingabe.upper()
    länge_wort = len(user_eingabe)
    
    user_tuple = (wort, länge_wort)
   
    if wort == "EXIT":
        print("Die aktuelle Datenbank beinhaltet folgende Wörter:\n")
        for w in cur.execute("SELECT * FROM words"):
            print(w[0], "\n")
            
        print("Die Datenbank wurde geschlossen!")
        connection.close()
        aktiv = False 
        
    elif not user_tuple in cur.execute("SELECT * FROM words"): 
        print(f"Das Wort {wort} wurde der Datenbank hinzugefügt!")
        cur.execute("INSERT INTO words VALUES(?,?)", (wort, länge_wort))
        connection.commit()
        
    else:
        print(f"Das Wort {wort} befindet sich schon in der Datenbank!")


# In[ ]:




