#!/usr/bin/env python
# coding: utf-8

# In[27]:


# ADLER
from adler import Adler


# In[28]:


adlerich = Adler("adlerich", "männlich", 4, "Ja", "Säugetier")


# In[29]:


adlerich.typ()


# In[30]:


adlerich.eat()


# In[31]:


# TIGER
from tiger import Tiger


# In[32]:


tigerlein = Tiger("Tigerlein", "männlich", 12, "Ja", "Säugetier")


# In[33]:


tigerlein.eat()


# In[34]:


tigerlein.sleep()


# In[35]:


tigerlein.grow(5)


# In[36]:


# GORILLA
from gorilla import Gorilla


# In[37]:


gori = Gorilla("Jonny", "männlich", 18, "Ja", "Säugetier")


# In[38]:


gori.klettern()


# In[39]:


gori.eat()


# In[40]:


gori.sleep()


# In[41]:


# ELEFANT
from elefant import Elefant


# In[42]:


eli = Elefant("Lilly", "weiblich", 20, "Ja", "Säugetier")


# In[43]:


eli.eat()


# In[44]:


eli.grow(7)


# In[45]:


eli.typ()


# In[ ]:




