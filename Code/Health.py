#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from pandas import DataFrame

Data = pd.read_csv('Data\Health.csv')
  
df = DataFrame(Data,columns=['country','year','status','life_expectancy','alcohol','percentage_expenditure','measles','bmi','polio','total_expenditure','gdp','population','schooling'])


ax = df.plot(x="schooling", y="life_expectancy", style="o")
ax.set_ylabel("life_expectancy")


# In[2]:


import statsmodels.api as sm #load the library and assigns a nickname
X = df[["schooling"]].values # the independent variable(s)
X = sm.add_constant(X)  # add the intercept term
y = df["life_expectancy"].values # the dependent variable
ols = sm.OLS(y, X).fit() # run the regression
ols.summary()


# In[3]:


X = df[['alcohol','measles','gdp','schooling']].values # the independent variable(s)
X = sm.add_constant(X)  # add the intercept term
y = df["life_expectancy"].values # the dependent variable
ols = sm.OLS(y, X).fit() # run the regression
ols.summary()


# In[ ]:




