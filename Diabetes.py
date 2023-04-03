# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

stats = pd.read_csv('diabetes.csv')

"""
DATA EXPLORATION
"""

stats.head(6)

# Data statistics
stats.describe()

stats_len = len(stats)

# Percentage of people in dataset that has diabetes
has_diabetes_perc = (len(stats[stats.Outcome == 1])/stats_len)*100 #~34.9%

# DATA VALIDATION
# remove last column (diabetes classification as 0 or 1) - Stats without outcome
stats_no_outcome = stats[stats.columns[0:7]]

# Count valid values (non-zero) for each parameter (column)
# (for these variables, having values = 0 does not make sense)
valid_values_perc = ((stats_no_outcome.astype(bool).sum(axis=0))/stats_len) * 100

# Count invalid values (zero) for each parameter (column)
invalid_values_perc = (((stats_no_outcome==0).sum(axis=0))/stats_len)*100

# For all of them, DiabetesPedigree and age were registered
# For some of them, blood pressure, skin thickness and BMI were not registered 

# GLUCOSE
# People with normal glucose levels - between 72 to 99 (when fasting)
normal_glucose = (len(stats[(stats.Glucose>72) & (stats.Glucose<99)])/stats_len)*100

# Percentage of people with high glucose that have diabetes 
high_glucose_diabetes = len(stats[(stats.Glucose>99) & (stats.Outcome==1)])/len(stats[stats.Glucose>99])*100 
#44% of people with high blood glucose levels have diabetes

# BLOOD PRESSURE
# Invalid blood pressure
invalid_blood_pressure_perc = (len(stats[stats.BloodPressure == 0])/stats_len)*100

# Percentage of people with high blood pressure that have diabetes 
high_bloodpressure_diabetes = len(stats[(stats.BloodPressure>70) & (stats.Outcome==1)])/len(stats[stats.BloodPressure>70])*100 
#40% of people with high blood pressure levels have diabetes

"""
DATA VISUALIZATION
"""

stats.Outcome = stats.Outcome.astype('category')
#col = list(stats.columns[0:8])
plt.rcParams['axes.grid'] = True
plt.rcParams.update({'font.size': 12})

# STUDY RELATIONS BETWEEN PARAMETERS
# Histograms to study data distribution per parameter
# Linear plots to see relationships between parameters

plt.figure(1)
g = sns.PairGrid(stats, hue="Outcome")
g.map_diag(sns.histplot, kde=True)
g.map_upper(sns.kdeplot, fill=True)
g.map_lower(sns.scatterplot)
blue_patch = mpatches.Patch(color='blue', label='No diabetes')
red_patch = mpatches.Patch(color='orange', label='Diabetes')
g.add_legend(loc="upper right", handles=[blue_patch, red_patch])
plt.suptitle("Dataset parameters distribution and relationships", y=1.01, fontsize=20)

plt.savefig("general_analysis.png", dpi=300, bbox_inches="tight");
plt.show()

"""
From histograms we see that diabetes is mainly related with:
- High glucose levels

From linear plots we see linear relationships between: 
- BMI and Skin Thickness
- Glucose and Insulin
"""

# Subplots with histograms (comparison for the different parameters between diabetes and no diabetes)
col=stats.columns

plt.figure(2)
fig2, axes2 = plt.subplots(nrows=2, ncols=4, figsize=(20,10))
axes2 = fig2.add_subplot()
plt.tight_layout()
for i in range(len(col)-1):
    plt.subplot(2,4,i+1)
    sns.distplot(stats[stats.Outcome == 0][col[i]], label='No diabetes')
    sns.distplot(stats[stats.Outcome == 1][col[i]], label='Diabetes')       
plt.subplot(2,4,4).legend(loc='upper right')
plt.suptitle("Dataset parameters distribution", y=1.01, fontsize=20)
fig2.tight_layout(pad=1.2)
plt.savefig("distribution.png", dpi=300, bbox_inches="tight");
plt.show()

"""
From histograms we see that diabetes is mainly related with:
- High glucose levels
"""

"""
plt.figure(4)
fig4, ax4 = plt.subplots(nrows=4, ncols=2, figsize=(10,20))
ax4 = fig4.add_subplot()
plt.tight_layout()
for i in range(len(col)):
    plt.subplot(4,2,i+1)
    sns.boxplot(data=stats, x='Outcome', y=col[i])       
plt.show(fig4)

plt.figure(5)
fig5, ax5 = plt.subplots(nrows=4, ncols=2, figsize=(10,20))
ax5 = fig5.add_subplot()
plt.tight_layout()
for i in range(len(col)):
    plt.subplot(4,2,i+1)
    sns.violinplot(data=stats, x='Outcome', y=col[i])       
plt.show(5)
"""

# STUDY GLUCOSE
# Histogram
"""
plt.figure(2)
list1 = list()
mylabels=list()
for outcome in stats.Outcome.cat.categories:
    list1.append(stats[stats.Outcome == outcome].Glucose)
    mylabels.append(outcome)

mylabels[0] = 'No diabetes'
mylabels[1] = 'Diabetes'
h = plt.hist(list1, bins=30, stacked=True, label = mylabels)
plt.legend()
plt.title('Glucose distribution')
plt.show(h)
# most people has glucose~100

# Glucose expressed in terms of age
# Linear model plot
plt.figure(3)
vis1 = sns.lmplot(data=stats, x='Age', y='Glucose', hue='Outcome', size=5)
plt.title('Glucose VS Age')
plt.show(vis1)
# The higher the age, the higher the glucose levels.
# The diabetes outcome seems to be related with higher glucose levels

# Kdeplot - heatmap
plt.figure(4)
k1=sns.kdeplot(stats.Age, stats.Glucose, shade=True, shade_lowest=False, cmap='Reds')
k1b=sns.kdeplot(stats.Age, stats.Glucose, shade=True, cmap='Reds')
plt.title('Glucose VS Age')
plt.show()
# The higher the age, the higher the glucose levels.
"""











