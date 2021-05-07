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

search_result = ScopusSearch("KEY(artificial intelligence) AND KEY(marketing)")

print("Documents found:", search_result.get_results_size())

data = pd.DataFrame(search_result.results)
data.subtypeDescription.drop_duplicates()

#Conference Paper, Book and Article
df = data.loc[data['subtypeDescription'].isin(['Article','Conference Paper','Book'])]

title = data['title']
abstract = data['description']
