# -*- coding: utf-8 -*-
"""
Retrive author information

Author: HyeJin Kim
"""

import pandas as pd
from pybliometrics.scopus import AuthorRetrieval

unpickled_df = pd.read_pickle(r"C:\Users\marco\Desktop\NLP\extracted_data.pkl")
df = unpickled_df[unpickled_df['description'].notna()]

print(df['author_ids'])

author = df['author_ids']

first_author = author.astype(str).str[0:11]
first_author = first_author.replace({';':''}, regex = True)

second_author = author.astype(str).str[12:23]

# convert first_author to dataframe
first_author = pd.DataFrame(first_author)

# Create a new column of None
first_author["h_index"] = [None] * first_author.shape[0]

# Loop to populate the columns h_index with the h-index dowloaded from Scopus
for i in range(first_author.shape[0]):
    print(i)
    try:
        first_author.iloc[i,1] = int(AuthorRetrieval(first_author.iloc[i,0]).h_index)
    # If a ValueError expection is raised, we put a np.nan
    except ValueError:
        first_author.iloc[i,1] = pd.NA
    # If a TypeError expection is raised, we put a np.nan
    except TypeError:
        first_author.iloc[i,1] = pd.NA

# Merging the h index with the dataframe
df = pd.merge(df, first_author.h_index, left_index=True, right_index=True)

# Check the Nan
df[pd.isna(df.h_index)]




