# -*- coding: utf-8 -*-
"""

We are interested in title, keywords and abstract

"""
# Packages
from pybliometrics.scopus import ScopusSearch
import pandas as pd
from pybliometrics.scopus import AuthorRetrieval
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
df = df[(df['coverDate'] <= "2020-06-01")]

title = df['title']
abstract = df['description']

author = df['author_ids']

first_author = author.astype(str).str[0:11]
first_author = first_author.replace({';':''}, regex = True)

second_author = author.astype(str).str[12:23]

# convert first_author to dataframe
first_author = pd.DataFrame(first_author) # Create a new column of None
first_author["h_index"] = [None] * first_author.shape[0]    

for i in range(len(df)):
        print(i)
        try:
            first_author.iloc[i,1] = int(AuthorRetrieval(first_author.iloc[i,0]).h_index)
    # If a ValueError expection is raised, we put a np.nan
        except ValueError:
            first_author.iloc[i,1] = pd.NA
    # If a TypeError expection is raised, we put a np.nan
        except TypeError:
            first_author.iloc[i,1] = pd.NA
            
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
df[pd.isna(df.h_index)]
df = df[df.h_index.notna()]

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

# df.to_pickle("C:/Users/USER/Documents/Python/NLP/extracted_data.pkl")
df.to_pickle(r"C:\Users\marco\Desktop\NLP\extracted_data.pkl")