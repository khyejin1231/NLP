# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:21:45 2021

@author: HYEJIN KIM

We are interested in title and abstract

Utility function:
    1. Punctuation
    2. Tokenization
    3. Stop words
    4. Lemmatize/Stem
    5. Other steps: Remove URLs, HTML tags, numbers
"""
# Packages
from pybliometrics.scopus import ScopusSearch
import pandas as pd

# Scopus search
search_result = ScopusSearch("(TITLE-ABS-KEY(machine learning) \
                             AND TITLE-ABS-KEY(marketing)) \
                              OR (TITLE-ABS-KEY(artificial intelligence) \
                               AND TITLE-ABS-KEY(marketing))")

print("Documents found:", search_result.get_results_size())

data = pd.DataFrame(search_result.results)

#Conference Paper, Book and Article
df = data.loc[data['subtypeDescription'].isin(['Article','Conference Paper','Book'])]

#Date
data.coverDate = pd.to_datetime(data.coverDate)
df = df[df['coverDate']>="2002-01-01"]

#Citation
df['citedby_count'] = pd.to_numeric(df['citedby_count'])

#Keep only those articles with at least one citation OR published after 2017-01-01
df = df[(df['citedby_count']>0) | (df['coverDate'] >= "2017-01-01")]

title = df['title']
abstract = df['description']
