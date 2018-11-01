
# coding: utf-8

# ## OneHotEncoder Data Transformation Project

# #### Objective

# To transform nominal data using OneHotEncoder to facilitate visualization and cluster analysis using k-modes clustering algorithm.

# #### Method

# Transform LabelEncoded nominal variables into one-hot numeric arrays using scikit-learn's OneHotEncoder.

# #### Datasource

# Proprietary survey, n = 1,200
#     
# Variables for transformation: var9, var11, var13, var16, var217, var234, var235, var236, var246

# In[2]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder


# In[3]:


# Create dataframe
df = pd.read_csv("OpioidsRecodes.csv")
df.head()


# In[5]:


df.tail()


# In[6]:


# View dataset shape
df.shape


# In[7]:


type(df)


# In[147]:


# Create list of variables for transformation
ds_list = ['var9_y', 'var11_y', 'var13_y', 'var16_y', 'var217_y', 'var234_y', 'var235_y', 'var236_y', 'var246_y']


# In[148]:


# Create subset for transformation
ds = df[ds_list]
ds


# In[149]:


ds.dtypes


# In[150]:


# View value counts of variables for transformation
ds.apply(pd.value_counts)


# In[151]:


# Transform nominal variables
encoder = OneHotEncoder()
ohe_array = encoder.fit_transform(ds).toarray()
print(ohe_array)

