#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


#importing data that was found on Kaggle
df = pd.read_csv(r"C:\Users\benja\Downloads\archive (3)\US_listed_companies.csv")
df.head()


# In[3]:


#function for finding the industries with the largest contraction and growth in earnings as a percentage of market cap
def most_change(dataframe):
    #finding the overall change in market of all companies/industries
    mean_marketcap_change = dataframe["change_in_earnings_by_marketcap_"].mean()
    print("The overall change in earnings for all companies was: " + str(mean_marketcap_change) + " percent.")
    #getting a list of the industries present on this dataset
    industries = dataframe["primary_industry"].unique().tolist()
    industry_ebit_change = pd.DataFrame(columns=['Industry', 'ebit_change'])
    #loop for iterating through the different industries 
    for index in industries: 
        #creating a dataframe containing only company data from a specific industry
        industry_stats = pd.DataFrame(dataframe[dataframe["primary_industry"] == index])
        #removing all companies without data about changes in earnings from the dataset
        industry_stats = pd.DataFrame(industry_stats.dropna(subset=['change_in_earnings_by_marketcap_']))
        #calculating the industry's change in earnings 
        ebit_mean_change = industry_stats['change_in_earnings_by_marketcap_'].mean()
        #adding the industry's change-in-earnings data to a dataframe to store all industries' data
        ebit_change_df = pd.DataFrame({'Industry':[index],'ebit_change':[ebit_mean_change]})
        industry_ebit_change = industry_ebit_change.append(ebit_change_df, ignore_index=True)
    #removing all of the empty cells 
    industry_ebit_change = pd.DataFrame(industry_ebit_change.dropna(subset=['ebit_change']))
    #sorting the change-in-earnings data and printing out the industries that had the largest contraction and growth
    industry_ebit_change = industry_ebit_change.sort_values("ebit_change")
    print("Industry that grew the most: " + str(industry_ebit_change.tail(1))  + " percent.")
    print("Industry that shrank the most: " + str(industry_ebit_change.head(1))  + " percent.")
    return industry_ebit_change

    
    


# In[4]:


most_change(df)


# In[5]:


most_change(df).hist(column='ebit_change', bins=[-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20])
plt.xlabel('Percent Change of Earnings')
plt.ylabel('Number of Industries')
plt.title('Change in Industry Earnings as a Percentage of Market Cap Between 2019 to 2020')


# In[6]:


#function that outputs the overall change in earnings marketcap of companies as well as the change in dividends by industry
def general_economic_patterns(dataframe):
    #removing all company data that didn't include dividend data or had 0 dividends
    dividend_companies = pd.DataFrame(dataframe.dropna(subset=['dps_fy2019', 'dps_fy2020']))
    dividend_companies = dividend_companies[dividend_companies['dps_fy2019'] > 0.0]
    #creating a dataframe to store the change in divident percentages
    dividend_change_df = pd.DataFrame(columns=['Industry', 'change_in_dividends'])
    #iterating through the companies with dividends and calculating their percentage change in dividends
    for index, series in dividend_companies.iterrows():
        dividend_change = (series['dps_fy2020'] - series['dps_fy2019'])*100 / series['dps_fy2019']
        dividend_change = pd.DataFrame({'Industry': [series['primary_industry']], 'change_in_dividends': [dividend_change]})
        dividend_change_df = dividend_change_df.append(dividend_change, ignore_index=True)
    #printing the percentage change in dividends
    print(dividend_change_df.mean())
    #returning the dataframe with the percent change in dividends for each dividend-yielding company
    return dividend_change_df
        


# In[7]:


general_economic_patterns(df)


# In[8]:


general_economic_patterns(df).hist(column='change_in_dividends', bins = [-100,-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90,100])
plt.xlabel('Percent Change of Dividends')
plt.ylabel('Number of Companies')
plt.title('Percent Change in Company Dividends From 2019 to 2020')


# In[ ]:




