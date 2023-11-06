#!/usr/bin/env python
# coding: utf-8

# In[50]:


def weiter():
    weitermachen = input("Willst du weitermachen? (['y'/'n']Ja/Nein) ")
    if weitermachen == "y":
        taschenrechner()
        
def begrüßen():
    print("Hallo!\nIch bin ein Taschenrechner!\nIch kann +, -, *, /, // und % berechnen!")   

def add(zahl01, zahl02):
    print("Das Ergebnis der Addition von ",zahl01," + ",zahl02," lautet: ",zahl01 + zahl02)

def sub(zahl01, zahl02):
    print("Das Ergebnis der Subtraktion von ",zahl01," - ",zahl02," lautet: ",zahl01 - zahl02)

def mul(zahl01, zahl02):
    print("Das Ergebnis der Multiplikation von ",zahl01," * ",zahl02," lautet: ",zahl01 * zahl02)

def div(zahl01, zahl02):
    print("Das Ergebnis der Division von ",zahl01," / ",zahl02," lautet: ",zahl01 / zahl02)

def ganzdiv(zahl01, zahl02):
    print("Das Ergebnis der Ganzdivision von ",zahl01," // ",zahl02," lautet: ",zahl01 // zahl02)

def mod(zahl01, zahl02):
    print("Das Ergebnis von Modulo von ",zahl01," % ",zahl02," lautet: ",zahl01 % zahl02)

begrüßen()

def taschenrechner():

    zahl01 = input("Tippe eine Zahl ein: ")
    operation = input("Was willst du mit dieser Zahl tun? ")
    zahl02 = input("Tippe eine zweite Zahl ein: ")
    
    
    if operation == "+":
        add(int(zahl01), int(zahl02))
        weiter()
        
    elif operation == "-":
        sub(int(zahl01), int(zahl02))
        weiter()
        
    elif operation == "*":
        mul(int(zahl01), int(zahl02))
        weiter()
        
    elif operation == "/":
        div(int(zahl01), int(zahl02))
        weiter()
        
    elif operation == "//":
        ganzdiv(int(zahl01), int(zahl02))
        weiter()
        
    elif operation == "%":
        mod(int(zahl01), int(zahl02))
        weiter()
        
taschenrechner()


# In[ ]:





# In[ ]:




