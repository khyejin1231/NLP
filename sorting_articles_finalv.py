# -*- coding: utf-8 -*-
"""

We are interested in title, keywords and abstract

"""
# Packages
from pybliometrics.scopus import ScopusSearch
import pandas as pd

# Scopus search
search_result = ScopusSearch("(TITLE-ABS-KEY(machine learning) \
                             AND TITLE-ABS-KEY(marketing)) \
                              OR (TITLE-ABS-KEY(artificial intelligence) \
                               AND TITLE-ABS-KEY(marketing))\
                       OR (TITLE-ABS-KEY(deep learning) \
                               AND TITLE-ABS-KEY(marketing))\
                                   OR (TITLE-ABS-KEY(neural network) \
                               AND TITLE-ABS-KEY(marketing))")

print("Documents found:", search_result.get_results_size())

data = pd.DataFrame(search_result.results)

# Articles only; no conference paper or books or others
df = data.loc[data['subtypeDescription'].isin(['Article'])]

#Date
data.coverDate = pd.to_datetime(data.coverDate)
df = df[df['coverDate']>="1950-01-01"]

#Citation
df['citedby_count'] = pd.to_numeric(df['citedby_count'])

#Optionally, filtering out some of the articles. We decided not to do that. 
#Keep only those articles with at least one citation OR published after 2020-01-01
#df = df[(df['citedby_count']>0) | (df['coverDate'] >= "2020-01-01")]
df = df[(df['coverDate'] <= "2021-06-01")]

title = df['title']
abstract = df['description']

import pickle
df.to_pickle(r"C:\Users\marco\Desktop\NLP\extracted_data.pkl")
#with open("../Users/amt/Documents/0. MSc Tinbergen/block 5. NLP/extracted_data.pkl", ‘wb’) as f:
    #pickle.dump(df, f)
    