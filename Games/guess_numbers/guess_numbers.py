#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

a = randint(1,100)                     

gamer = input("Welche Zahl zwischen 1 und 100 hat der Computer gewählt? ")  

active = True                         

durchgang = 0                         

while active:
   
    durchgang = durchgang + 1
    
    if int(gamer) < a:                                                       
        print("Die Zahl ist leider zu niedrig!")
        gamer = input("Rate noch einmal! ")                                 
        
    elif int(gamer) > a:                                                    
        print("Die Zahl ist leider zu groß!")
        gamer = input("Rate noch einmal! ")
        
    else:                                                                    
        print("Richtig :-), du hast", durchgang, "Versuche gebraucht")
        neues_spiel = input("Möchtest du das Spiel beenden: 'j' oder' n'")
            
        if neues_spiel == "j":
            active = False
            print("Das Spiel ist beendet!") 
            
        else:
            gamer = input("Weiter gehts! ")                                  
            durchgang = 0                                                    
            a = randint(1,100)
        
    

