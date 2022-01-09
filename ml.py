#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import pylab as pl
import numpy as np #for matrix ...
import pandas as pd #for reading ...
#get_ipython().run_line_magic('matplotlib', 'inline #this is for nootBook and datas')


# In[31]:


allData = pd.read_csv("C:/Users/ASUS.PIESC/Downloads/FuelConsumption.csv",encoding = "ISO-8859-1",low_memory=False)
allData.head()#take a simple look on file


# In[11]:


allData.describe()


# In[42]:


simpleRow = allData[{'EngineSize','Cylinders','Transmission','Fuel','Smog','CO2'}]


# In[43]:


simpleRow.head(10) #take a simple view of list


# In[22]:


visualTable = allData[['EngineSize','Cylinders','Transmission','Fuel']]
visualTable.hist()
plt.show()


# In[44]:


plt.scatter(simpleRow.EngineSize, simpleRow.Cylinders , color='blue')
plt.xlabel("Engine size")
plt.ylabel("Cylinders")
plt.show()


# In[45]:


TestPart = np.random.rand(len(allData)) < 0,8 


# In[46]:


train = simpleRow[TestPart]
test = simpleRow[~TestPart]


# In[ ]: