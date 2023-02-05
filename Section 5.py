# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
stats = pd.read_csv('C:\\Users\\abeatrir\\Python\\DemographicData.csv')
stats

len(stats)
stats.columns
len(stats.columns)

#Top rows
stats.head(6)

#Bottom rows
stats.tail(6)

#stats on the columns
stats.describe()

#reverse the dataframe
stats[::-1]

# de 20 em 20
stats[::20]

"Renaming coluns of a dataset"
stats.columns=['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']


#Seaborn package
import matplotlib.pyplot as plt
import seaborn as sns
plt.show()
import warnings
warnings.filterwarnings('ignore')

vis1 = sns.distplot(stats["InternetUsers"])
vis2 = sns.boxplot(data=stats, x="IncomeGroup", y="BirthRate")
vis3 = sns.lmplot(data=stats, x="InternetUsers", y="BirthRate", fit_reg = False, hue="IncomeGroup", size = 8, scatter_kws = {"s":200})


