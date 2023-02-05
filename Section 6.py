# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
os.getcwd()

movies = pd.read_csv('C:\\Users\\abeatrir\\Python\\Movie-Ratings.csv')

len(movies)

movies.columns = ['Film', 'Genre', 'CriticRating', 'AudienceRating', 'BudgetMillions', 'Year']

movies.info() #info acerca de tipos, número de colunas
movies.describe() #count, mean, std

movies['Film']

movies.Film = movies.Film.astype('category')
movies.Genre = movies.Genre.astype('category')
movies.Year = movies.Year.astype('category')

from matplotlib import pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Jointplots
j = sns.jointplot(data=movies, x='CriticRating', y='AudienceRating' )

#Histograms
m1 = sns.displot(movies.AudienceRating)

#Stacked histograms
plt.hist(movies[movies.Genre == 'Action'].BudgetMillions, bins=15)
plt.hist(movies[movies.Genre == 'Thriller'].BudgetMillions, bins=15)
plt.show()

plt.hist([movies[movies.Genre == 'Action'].BudgetMillions, movies[movies.Genre == 'Drama'].BudgetMillions,movies[movies.Genre == 'Thriller'].BudgetMillions], bins=15, stacked=True)

for gen in movies.Genre.cat.categories:
    print (gen)

list1 = list()    
mylabels=list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre == gen].BudgetMillions)
    mylabels.append(gen)
h=plt.hist(list1, bins=30, stacked=True, rwidth=1, label=mylabels)
plt.legend()
plt.show()

#KDE plot
k1=sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds')
k1b=sns.kdeplot(movies.CriticRating, movies.AudienceRating, cmap='Reds')

#Working with subplots
k2 = sns.kdeplot(movies.BudgetMillions, movies.AudienceRating)

#subplots
f,axes = plt.subplots(1,2,figsize=(12,6))
k1=sns.kdeplot(movies.BudgetMillions, movies.AudienceRating, ax=axes[0])
k2=sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[1])

#violinPlots
w = sns.boxplot(data=movies, x='Genre', y='CriticRating')
z = sns.violinplot(data=movies, x='Genre', y='CriticRating') #width indicates nb of oibservations

w = sns.boxplot(data=movies[movies.Genre == 'Drama'], x='Year', y='CriticRating')
z = sns.violinplot(data=movies[movies.Genre == 'Drama'], x='Year', y='CriticRating')

# Create a Facet grid
g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating')

#can populate with any type of chart. Example: histograms
g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
g = g.map(plt.hist, 'BudgetMillions')

# Controlling axes and adding diagonals
g = sns.FacetGrid(movies, row='Genre', col='Year', hue='Genre')
kws = dict(s=50, linewidth=0.5, edgecolor='black')
g = g.map(plt.scatter, 'CriticRating', 'AudienceRating', **kws)
g.set(xlim=(0,100), ylim=(0,100))
for ax in g.axes.flat:  #flatten the array in axes
    ax.plot((0,100), (0,100), c="gray", ls="--" )
g.add_legend()

# Building dashboards
sns.set_style('darkgrid')
f, axes = plt.subplots(2, 2, figsize =(15,15))
k1 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[0,0])
k2 = sns.kdeplot(movies.BudgetMillions, movies.CriticRating, ax=axes[0,1])
k1.set(xlim=(-20,160))
k2.set(xlim=(-20,160))
z = sns.violinplot(data=movies[movies.Genre=='Drama'], x='Year', y='CriticRating', ax=axes[1,0])
#k4 = sns.kdeplot(movies.CriticRating, movies.AudienceRating, shade=True, shade_lowest=False, cmap='Reds', ax=axes[1,1])
#k4b = sns.kdeplot(movies.CriticRating, movies.AudienceRating, cmap='Reds', ax=axes[1,1])

#Graphic that is not seaborn
axes[1,1].hist(movies.CriticRating, bins=15)








