# -*- coding: utf-8 -*-
"""
Retrive author information

Author: HyeJin Kim
"""

from pybliometrics.scopus import AuthorRetrieval

print(df['author_ids'])

author = df['author_ids']

first_author = author.astype(str).str[0:11]
first_author = first_author.replace({';':''}, regex = True)

second_author = author.astype(str).str[12:23]

au = pd.Series()
for i in first_author:
    au.add(AuthorRetrieval(i).h_index)
    