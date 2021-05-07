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
pd.set_option("display.max_rows", None, "display.max_columns", None)

data.head()
print(data['description'][1]) #See that there is no hyperlinks, numbers, HTML tags, URLs.

title = data['title']
abstract = data['description']
