#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint

def würfeln():
    
    würfe = int(input("Wie viele Würfe sollen simuliert werden? "))
    print("Simuliere", würfe, "Würfe....... ") 
    
    list_würfe = []
    summe = 0
    
    for i in range(würfe):                                     # Würfe in Liste füllen
        list_würfe.append(randint(1,6))
    
    for b in list_würfe:                                       # Würfe aufsummieren
        summe += b
    
    mittelwert = summe / len(list_würfe)                       # Mittelwert bilden
    
    return print("Der Mittelwert der Würfe ist: ", mittelwert, "\nDer theoretische Mittelwert ist 3.5!") 
    
        
            
würfeln()


# In[ ]:

    # JE GRÖSSER N, DESTO NÄHER IST DIE ZAHL AM THEORETISCHEN MITTELWERT 3.5 DRAN!!


