# -*- coding: utf-8 -*-
"""

We are interested in title, keywords and abstract

"""
# Packages
from pybliometrics.scopus import ScopusSearch
import pandas as pd
from pybliometrics.scopus import AuthorRetrieval
from scholarly import scholarly
from scholarly import scholarly, ProxyGenerator

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)


# from pybliometrics.scopus import SerialTitle
# from pybliometrics.scopus import exception
# from multiprocessing import Pool
# import author
# from pybliometrics.scopus import exception

# Scopus search
search_result = ScopusSearch("(TITLE-ABS-KEY(machine learning) \
                             AND TITLE-ABS-KEY(marketing)) \
                              OR (TITLE-ABS-KEY(artificial intelligence) \
                               AND TITLE-ABS-KEY(marketing))\
                       OR (TITLE-ABS-KEY(deep learning) \
                               AND TITLE-ABS-KEY(marketing))\
                                   OR (TITLE-ABS-KEY(neural network) \
                               AND TITLE-ABS-KEY(marketing))")
                                     
search_result2 = ScopusSearch("(TITLE-ABS-KEY(machine learning) \
                             AND TITLE-ABS-KEY(consumer)) \
                              OR (TITLE-ABS-KEY(artificial intelligence) \
                               AND TITLE-ABS-KEY(consumer))\
                       OR (TITLE-ABS-KEY(deep learning) \
                               AND TITLE-ABS-KEY(consumer))\
                                   OR (TITLE-ABS-KEY(neural network) \
                               AND TITLE-ABS-KEY(consumer))")                                       

search_result3 = ScopusSearch("(TITLE-ABS-KEY(lasso regression) \
                               AND TITLE-ABS-KEY(marketing))\
                                 OR (TITLE-ABS-KEY(augmented reality) \
                               AND TITLE-ABS-KEY(marketing))\
                                 OR (TITLE-ABS-KEY(churn prediction) \
                               AND TITLE-ABS-KEY(marketing))\
                                 OR (TITLE-ABS-KEY(reinforcement learning) \
                               AND TITLE-ABS-KEY(marketing))")
                                     
search_result4 = ScopusSearch("(TITLE-ABS-KEY(lasso regression) \
                               AND TITLE-ABS-KEY(consumer))\
                                 OR (TITLE-ABS-KEY(augmented reality) \
                               AND TITLE-ABS-KEY(consumer))\
                                 OR (TITLE-ABS-KEY(churn prediction) \
                               AND TITLE-ABS-KEY(consumer))\
                                 OR (TITLE-ABS-KEY(reinforcement learning) \
                               AND TITLE-ABS-KEY(consumer))")

print("Documents found:", search_result.get_results_size())

df1 = pd.DataFrame(search_result.results)
df2 = pd.DataFrame(search_result2.results)
df3 = pd.DataFrame(search_result3.results)
df4 = pd.DataFrame(search_result4.results)
data = pd.concat([df1, df2, df3, df4])
data.drop_duplicates(subset ="title",
                     keep = False, inplace = True)
df = data

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
df = df[(df['coverDate'] <= "2020-06-01")]

title = df['title']
abstract = df['description']

author = df.author_names.str.split(';', expand=True)
year = pd.DatetimeIndex(df['coverDate']).year
year = pd.DataFrame(year)
author = pd.concat([year, author.reset_index(drop=True)], axis = 1)
result = []
author[0][1]

for i in range(1672, len(author)):
    print(i)
    year = author['coverDate'][i] - 1
    try:
        search_query = scholarly.search_author(author[0][i])
        author1 = next(search_query)
        result1 = scholarly.fill(author1, sections=['counts']).get('cites_per_year').get(year)
        result.append(result1)
    except StopIteration:
        result.append(None)
    except TypeError:
        result.append(None)
        

#654 it stopped
#1071 it stopped
#1285 it stopped 
#1672
# =============================================================================
# # Loop to populate the columns h_index with the h-index dowloaded from Scopus
# if __name__ == '__main__':
#    
#     pool = Pool(7)         
#     pool.map(author, l)  # Create a multiprocessing Pool
# =============================================================================

# Merging the h index with the dataframe
df = pd.merge(df, first_author.h_index, left_index=True, right_index=True)

# Check the Nan
#df[pd.isna(df.h_index)]
#df = df[df.h_index.notna()]

# Convert issn column to dataframe
df = df[df['issn'].notna()]
SJR = pd.DataFrame(df.issn)

# =============================================================================
# 
# # Add a new column of None
# SJR['score'] = [None] * SJR.shape[0]
# 
# SJR
# # Loop to fill in the column score with the SNIP score
# 
# for i in range(SJR.shape[0]):
#     print(SJR.iloc[i,0])
#     print(SerialTitle(SJR.iloc[i,0]).sjrlist)
#     try: 
#         SJR.iloc[i,1] = (SerialTitle(SJR.iloc[i,0]).sjrlist)
#     except ValueError:
#         SJR.iloc[i,1] = pd.NA
#     except TypeError:
#         SJR.iloc[i,1] = pd.NA
#     except exception.Scopus404Error:
#         SJR.iloc[i,1] = pd.NA
# 
# 
# df = pd.merge(df, SJR['score'], left_index=True, right_index=True)
# 
# df = df[df['author_ids'].notna()]
# =============================================================================

df.to_pickle("C:/Users/USER/Documents/Python/NLP/extracted_data.pkl")
#df.to_pickle(r"C:\Users\marco\Desktop\NLP\extracted_data.pkl")