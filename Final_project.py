#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv(r"C:\Users\benja\Downloads\archive (3)\US_listed_companies.csv")
df.head()


# In[3]:


def most_change(dataframe):
    industries = dataframe["primary_industry"].unique().tolist()
    industry_ebit_change = pd.DataFrame(columns=['Industry', 'ebit_change'])
    for index in industries: 
        industry_stats = pd.DataFrame(dataframe[dataframe["primary_industry"] == index])
        industry_stats = pd.DataFrame(industry_stats.dropna(subset=['change_in_earnings_by_marketcap_']))
        industry_stats = pd.DataFrame(industry_stats.sort_values(by=['change_in_earnings_by_marketcap_'], ascending=False))
        ebit_mean_change = industry_stats['change_in_earnings_by_marketcap_'].mean()
        ebit_change_df = pd.DataFrame({'Industry':[index],'ebit_change':[ebit_mean_change]})
        industry_ebit_change = industry_ebit_change.append(ebit_change_df)
    #print(index)
    #print(ebit_mean_change)
    industry_ebit_change = pd.DataFrame(industry_ebit_change.dropna(subset=['ebit_change']))
    industry_ebit_change = industry_ebit_change.sort_values("ebit_change")
    print("Industry that grew the most: " + str(industry_ebit_change.tail(1)))
    print("Industry that shrank the most: " + str(industry_ebit_change.head(1)))
    return industry_ebit_change

    
    


# In[7]:


def general_economic_patterns(dataframe):
    mean_marketcap_change = dataframe["change_in_earnings_by_marketcap_"].mean()
    dividend_companies = pd.DataFrame(dataframe.dropna(subset=['dps_fy2019', 'dps_fy2020']))
    dividend_companies = dividend_companies[dividend_companies['dps_fy2019']>0.0]
    print(dividend_companies)
    dividend_change_df = pd.DataFrame(columns=['Industry', 'change_in_dividends'])
    for index,series in dividend_companies.iterrows():
        dividend_change = (series['dps_fy2020'] - series['dps_fy2019'])/series['dps_fy2019']
        dividend_change = pd.DataFrame({'Industry':[series['primary_industry']], 'change_in_dividends':[dividend_change]})
        dividend_change_df.append(dividend_change)
    print(dividend_change_df.head())
        


# In[8]:


general_economic_patterns(df)


# In[6]:


def 

