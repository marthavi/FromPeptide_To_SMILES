#!/usr/bin/env python
# coding: utf-8

# In[28]:


from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
import pandas as pd
import numpy as np


# In[29]:


data = pd.read_csv("Documents/Peptide_List.csv", sep = ";") 


# In[30]:


data


# In[31]:


peptidos = data['Peptide']
for pep in peptidos:
    if not pd.isna(pep):
        print(pep)


# In[33]:


Smiles  = []

driver = webdriver.Chrome(executable_path='Documents/chromedriver.exe')
driver.get("https://www.novoprolabs.com/tools/convert-peptide-to-smiles-string") 

for pep in peptidos:
    if pd.isna(pep): 
        Smiles.append('nan')
    else:
        driver.find_element_by_id("btn-clear").send_keys(Keys.ENTER)
        driver.find_element_by_name("sequence").send_keys(pep)  
        driver.find_element_by_name("main_submit").send_keys(Keys.ENTER)  
        time.sleep(3)
        texto = driver.find_element_by_id("output-res") 
        Smiles.append(texto.text)
        print(texto.text)
    
driver.close() 


# In[34]:


Smiles


# In[35]:


data['SMILES'] = Smiles


# In[36]:


data


# In[37]:


data.to_csv('data_smiles.csv')


# In[ ]:




