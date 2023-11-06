#!/usr/bin/env python
# coding: utf-8

# In[51]:


aktiv = True

while aktiv:
   
    user_text = input("Gib einen Text ein (oder quit): ").lower()
    if user_text == "quit":
        print("Das Verschlüsseln ist beendet!")
        break
        
    user_zahl = int(input("Um wie viele Zeichen soll der Text verschlüsselt werden: "))
   
    zeichen = "" 
    
    for i in range(len(user_text)):
        if user_text[i] == " ":
            zeichen += " "
            continue
        if ord(user_text[i]) < 97 or ord(user_text[i]) > 123:
            zeichen += user_text[i]
            continue
            
        buchstabe = user_text[i]
        zeichen += chr((ord(buchstabe) + user_zahl - 97) % 26 + 97)
        
    print("Der verschlüsselte Text ist: ", zeichen)



# In[ ]:




