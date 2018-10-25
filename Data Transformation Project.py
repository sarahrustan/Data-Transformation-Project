
# coding: utf-8

# ## Data Transformation Project

# #### Objective

# To transform categorical data to facilitate visualization and cluster analysis using k-modes clustering algorithm.

# #### Method

# Preprocess categorical variables using scikit-learn's LabelEncoder and merge transformed variables into existing dataset.

# #### Datasource

# Proprietary survey, n = 1,200
#     
# Variables for transformation: var9, var11, var12, var13, var16, var217, var230, var231, var232, var233, var234, var235, var236, var246

# In[1]:


import pandas as pd
import numpy as np
from sklearn import preprocessing


# In[101]:


# Create dataframe
df = pd.read_csv("OpioidsMerged.csv")
df.head()


# In[76]:


# View dataset shape
df.shape


# In[100]:


# Select variables for transformation
ds = df[['Vrid','var9', 'var11', 'var12', 'var13', 'var16', 'var217', 'var230', 'var231', 'var232', 'var233', 'var234', 
        'var235', 'var236', 'var246']]
ds.head()


# In[107]:


# View value counts of variables for transformation
ds.iloc[:, 1:].apply(pd.value_counts)


# In[99]:


# Create new dataframe with transformed variables
dsr = 0
for i in ds:
    if i=="Vrid":
        dsr=ds
    if i != "Vrid":
        dsr= ds.apply(preprocessing.LabelEncoder().fit_transform)
dsr.head()


# In[109]:


# View value counts of transformed variables
dsr.iloc[:, 1:].apply(pd.value_counts)


# In[71]:


# Validate transformation by checking that each transformed variable contains the right number of values and the same variance
for i in ds:
    count = ds[i].value_counts()
    rcount = dsr[i].value_counts()
    if len(count) == len(rcount) and np.var(count) == np.var(rcount):
        print(i, "True")
    else:
        print(i, "False")


# In[72]:


# Merge transformed variables with original dataset based on Vrid
df_merged = pd.merge(df, dsr, how='left', on='Vrid')
df_merged.head()


# In[103]:


# List new variables
df_merged.iloc[:, -(len(dsr.columns)-1):].columns.tolist()


# In[91]:


# Validate merge by checking shape of merged dataset
if (len(df_merged) == len(df)) and (len(df_merged.columns) == len(df.columns)+len(dsr.columns)-1):
    print("True")
else:
    print("False", df.shape, df_merged.shape)


# In[90]:


# Save df_merged as a new csv file
df_merged.to_csv("OpioidsRecodes.csv", index=False)

