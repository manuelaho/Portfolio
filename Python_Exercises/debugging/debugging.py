#!/usr/bin/env python
# coding: utf-8

# In[2]:


import logging
logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")


# In[3]:


# Funktion 1
def input_email():
    '''                                                   
    Fragt den User nach seiner Email-Adresse

        Returns:
            email(str)
    '''
    user_email = input("Gib bitte deine Email-Adresse ein: ")
    
    return user_email


# In[4]:


# Funktion 2
def input_age():
    '''                                                   
    Fragt den User nach dem Alter

        Returns:
            age(int)
    '''
    user_age = input("Gib bitte dein Alter ein: ")
    
    return user_age


# In[5]:


active = True

while active:
    
    try:
        user_input = input(f"Drücke '?' um Hilfe zu bekommen!\nDrücke 'q' um die App zu verlassen!\nDrücke 'w' um weiterzumachen!\n")
        assert user_input == "?" or user_input == "q" or user_input == "w"
        
    except AssertionError:
        logging.error("Gib bitte einen korrekten Input an!")
         
    if user_input == "q":
        active = False
        logging.info("Die App wurde geschlossen!")
        
    elif user_input == "?":
        logging.info("Die doc_strings werden aufgerufen!")
        print(input_email.__doc__)
        print(input_email.__doc__)
        
    elif user_input == "w":
        
        try:
            logging.info("Die Funktion 'input_email' wurde aufgerufen!")
            user_email = input_email()
            logging.info(f"Die Email-Adresse lautet {user_email}!")
            assert "@" in user_email and "." in user_email and len(user_email) > 5
            
        except AssertionError:
            logging.error("Gib bitte eine korrekte Email-Adresse an!")
            user_email = input_email()
            
        try:
            logging.info("Die Funktion 'input_age' wurde aufgerufen!")
            user_age = input_age()
            logging.info(f"Eingegebenes Alter ist {user_age}!")
            assert int(user_age) > 10 and  int(user_age)  < 100
            
        except AssertionError:
            logging.error("Gib bitte ein korrektes Alter an!")
            user_age = input_age()
            


# In[ ]:




