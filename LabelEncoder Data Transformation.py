
# coding: utf-8

# ## LabelEncoder Data Transformation Project

# #### Objective

# To transform categorical data to facilitate visualization and cluster analysis using k-modes clustering algorithm.

# #### Method

# Preprocess categorical variables into range(0 to n_categories-1) using scikit-learn's LabelEncoder and merge transformed variables into existing dataset.

# #### Datasource

# Proprietary survey, n = 1,200
#     
# Variables for transformation: var9, var11, var12, var13, var16, var217, var230, var231, var232, var233, var234, var235, var236, var246

# In[1]:


import pandas as pd
import numpy as np
from sklearn import preprocessing


# In[2]:


# Create dataframe
df = pd.read_csv("OpioidsMerged.csv")
df.head()


# In[3]:


df.tail()


# In[4]:


# View dataset shape
df.shape


# In[5]:


type(df)


# In[112]:


# Create subset for transformation
ds = df[['Vrid','var9', 'var11', 'var12', 'var13', 'var16', 'var217', 'var230', 'var231', 'var232', 'var233', 
         'var234', 'var235', 'var236', 'var246']]
ds.head()


# In[114]:


ds.set_index('Vrid')


# In[115]:


ds.head()


# In[116]:


ds.tail()


# In[117]:


ds.dtypes


# In[118]:


# View value counts of variables for transformation
ds.iloc[:, 1:].apply(pd.value_counts)


# In[122]:


# Create new dataframe with transformed variables
dsr = pd.DataFrame()
dsr= ds.apply(preprocessing.LabelEncoder().fit_transform)
dsr['Vrid'] = ds['Vrid']
dsr.head()


# In[123]:


dsr.tail()


# In[125]:


# View value counts of transformed variables
dsr.iloc[:, 1:].apply(pd.value_counts)


# In[126]:


# Validate transformation by checking that each transformed variable contains the right number of values and the same variance
for i in ds:
    count = ds[i].value_counts()
    rcount = dsr[i].value_counts()
    if len(count) == len(rcount) and np.var(count) == np.var(rcount):
        print(i, "True")
    else:
        print(i, "False")


# In[143]:


# Merge transformed variables with original dataset based on Vrid
df_merged = pd.merge(df, dsr, how='left', on='Vrid', indicator=True)
df_merged.head()


# In[144]:


df_merged.tail()


# In[145]:


# Validate merge by checking that values for each Vrid were present in both dataframes
pd.value_counts(df_merged._merge)


# In[146]:


# Validate merge by checking shape of merged dataset
if (len(df_merged) == len(df)) and (len(df_merged.columns) == len(df.columns)+len(dsr.columns)):
    print("True")
else:
    print("False", df.shape, df_merged.shape)


# In[147]:


# Drop _merge column
df_merged.drop("_merge", axis=1, inplace=True)
df_merged.head()


# In[148]:


# Save df_merged as a new csv file
df_merged.to_csv("OpioidsRecodes.csv", index=False)

