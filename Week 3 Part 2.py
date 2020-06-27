#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


# In[15]:


df = pd.read_csv('task1.csv')
df.head()


# In[9]:


pip install geocoder


# In[10]:


import geocoder


# In[11]:


def get_latlng(postal_code):
    # initialize your variable to None
    lat_lng_coords = None
    # loop until you get the coordinates
    while(lat_lng_coords is None):
        g = geocoder.arcgis('{}, Toronto, Ontario'.format(postal_code))
        lat_lng_coords = g.latlng
    return lat_lng_coords
    
get_latlng('M4G')


# In[16]:


postal_codes = df['Postcode']    
coords = [ get_latlng(postal_code) for postal_code in postal_codes.tolist() ]


# In[17]:


df_coords = pd.DataFrame(coords, columns=['Latitude', 'Longitude'])
df['Latitude'] = df_coords['Latitude']
df['Longitude'] = df_coords['Longitude']
df.head()


# In[19]:


df[df.Postcode == 'M5G']


# In[20]:


df.to_csv('task2.csv', index=False)


# In[21]:


df


# In[ ]:




