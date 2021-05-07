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
import numpy as np
import sys

from pybliometrics.scopus import ScopusSearch

import pandas as pd

search_result0 = ScopusSearch("KEY(artificial intelligence) AND KEY(marketing)")
search_result1 = ScopusSearch("KEY(machine learning) AND KEY(marketing)")

print("Documents found:", search_result0.get_results_size())

data0 = pd.DataFrame(search_result0.results)
data1 = pd.DataFrame(search_result1.results)

frames = [data0, data1]
data = pd.concat(frames).drop_duplicates()

#Conference Paper, Book and Article
df = data.loc[data['subtypeDescription'].isin(['Article','Conference Paper','Book'])]

#Date
df['coverDate'].astype(str).str[0:4]
df['coverDate'] = df['coverDate'].astype(str).str[0:4]
df['coverDate'] = pd.to_numeric(df['coverDate'])
df = df[df['coverDate']>=2002]

#citation
df['citedby_count'] = pd.to_numeric(df['citedby_count'])
df = df[(df['citedby_count']>0) | (df['coverDate'] >= 2017)]

title = df['title']
abstract = df['description']
