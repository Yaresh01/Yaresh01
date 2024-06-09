#!/usr/bin/env python
# coding: utf-8

# In[1]:


def find_missing_values(df):
   
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    if missing_values.empty:
        print("No missing values found.")
    else:
        print("Missing values found:")
        print(missing_values)
    return missing_values

