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

#import diabetes.csv file
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
plt.rcParams['axes.grid'] = True
plt.rcParams.update({'font.size': 12})
sns.set(style="darkgrid")

# Multi-plot grid
# Histograms to study data distribution per parameter
# Lineplots and probability density function (KDE) plots
# to study relationships between parameters

plt.figure()
g = sns.PairGrid(stats, hue="Outcome")
g.map_diag(sns.histplot, kde=True)
g.map_upper(sns.kdeplot, fill=True)
g.map_lower(sns.scatterplot)
blue_patch = mpatches.Patch(color='blue', label='No diabetes')
red_patch = mpatches.Patch(color='orange', label='Diabetes')
g.add_legend(loc="upper right", handles=[blue_patch, red_patch])
plt.suptitle("General data analysis - per parameter and between parameters", y=1, fontsize=18)
plt.savefig("general_analysis.png", dpi=300, bbox_inches="tight");
plt.show()

# Correlation matrix
plt.figure()
matrix = stats.corr().round(1)
sns.heatmap(matrix, annot=True)
plt.title('Data Correlation Matrix', fontsize=18)
plt.savefig("corr_matrix.png", dpi=300, bbox_inches="tight");
plt.show()

col=stats.columns
stats.Outcome = stats.Outcome.astype('category')

# Histograms
plt.figure()
fig2, axes2 = plt.subplots(nrows=4, ncols=2, figsize=(20,10))
axes2 = fig2.add_subplot()
plt.tight_layout()
for i in range(len(col)-1):
    for outcome in stats.Outcome.cat.categories:
        plt.subplot(2,4,i+1)
        sns.distplot(stats[stats.Outcome == outcome][col[i]])
plt.subplot(2,4,4).legend(['No diabetes', 'Diabetes'], loc='upper right')
plt.suptitle("Data analysis per parameter and diagnosis - histograms", y=1, fontsize=18)
fig2.tight_layout(pad=1.2)
plt.savefig("histograms.png", dpi=300, bbox_inches="tight");
plt.show()

# Boxplots 
plt.figure()
fig4, ax4 = plt.subplots(nrows=2, ncols=4, figsize=(12,10))
ax4 = fig4.add_subplot()
plt.tight_layout()
for i in range(len(col)-1):
    plt.subplot(2,4,i+1)
    sns.boxplot(data=stats, x='Outcome', y=col[i])
    plt.xticks([0, 1], ['No diabetes', 'Diabetes'])
    plt.xlabel('Diagnosis')    
plt.suptitle("Data analysis per parameter and diagnosis - boxplots", y=1, fontsize=18)
fig4.tight_layout(pad=1.2)
plt.savefig("boxplots.png", dpi=300, bbox_inches="tight");
plt.show(fig4)

# Violinplots
plt.figure()
fig5, ax5 = plt.subplots(nrows=2, ncols=4, figsize=(12,10))
ax5 = fig5.add_subplot()
plt.tight_layout()
for i in range(len(col)-1):
    plt.subplot(2,4,i+1)
    sns.violinplot(data=stats, x='Outcome', y=col[i]) 
    plt.xticks([0, 1], ['No diabetes', 'Diabetes'])
    plt.xlabel('Diagnosis') 
plt.suptitle("Data analysis per parameter and diagnosis - violinplots", y=1, fontsize=18)
fig5.tight_layout(pad=1.2)
plt.savefig("violinplots.png", dpi=300, bbox_inches="tight");      
plt.show(fig5)

# STUDYING GLUCOSE
# Histogram
plt.figure()
list1 = list()
mylabels=list()
for outcome in stats.Outcome.cat.categories:
    list1.append(stats[stats.Outcome == outcome].Glucose)
    mylabels.append(outcome)

mylabels[0] = 'No diabetes'
mylabels[1] = 'Diabetes'
h = plt.hist(list1, bins=30, stacked=True, label = mylabels)
plt.legend(loc="upper left")
plt.title('Blood glucose levels per diagnosis')
plt.savefig("glucose_distribution.png", dpi=300, bbox_inches="tight");  
plt.show(h)
# most people has glucose~100


"""
CONCLUSIONS

COMPARING PARAMETERS we see linear relationships between: 
- Insulin and Skin Thickness
- BMI and Skin Thickness
- Glucose and Insulin

STUDYING THE RELATIONSHIP BETWEEN DIABETES AND EACH PARAMETER, 
we can conclude that diabetes is mainly related with:
- High glucose levels
"""










