#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def find_duplicate_rows(df):
    
    duplicates = df[df.duplicated()]
    return duplicates

