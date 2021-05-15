# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:54:34 2021

@author: HYEJIN KIM
About: v2. looking at top 50 journals
"""
search_result0 = ScopusSearch("TITLE-ABS-KEY(artificial intelligence)")

print("Documents found:", search_result0.get_results_size())

data = pd.DataFrame(search_result0.results)

#Conference Paper, Book and Article
df = data.loc[data['subtypeDescription'].isin(['Article','Conference Paper','Book'])]

df = df.loc[df['publicationName'].isin(['Academy of Management Journal','Academy of Management Review',
                                        'Accounting, Organizations and Society', 'Administrative Science Quarterly','American Economic Review',
                                        'Contemporary Accounting Research','Econometrica',
                                        'Entreprenership Theory and Practice','Harvard Business Review','Human Relations','Human Resource Management',
                                        'Information Systems Research',
                                        'Journal of Accounting Research','Journal of Applied Psychology','Journal of Business Ethics',
                                        'Journal of Business Venturing','Journal of Consumer Psychology','Journal of Consumer Research',
                                        'Journal of Finance','Journal of Financial and Quantitative Analysis','Journal of Financial Economics',
                                        'Journal of International Business Studies','Journal of Management','Jornal of Management Information Systems',
                                        'Journal of Management Studies','Journal of Marketing','Journal of Marketing Research','Journal of Operations Management',
                                        'Journal of Political Economy','Journal of the Academy of Marketing Science','Management Science',
                                        'Manufacturing and Service Operations Management','Marketing Science','MIS Quarterly',
                                        'Operations Research','Organization Studies','Organizational Behavior and Human Decision Processes',
                                        'Production and Operations Management','Quarterly Journal of Economics','Research Policy','Review of Accounting Studies',
                                        'Review of Economic Studies','Review of Finance','Review of Financial Studies','Sloan Management Review',
                                        'Strategic Entrepreneurship Journal','Strateigic Management Journal','The Accounting Review'])]
