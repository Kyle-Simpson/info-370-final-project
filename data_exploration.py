# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:46:20 2019

@author: ameli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/prepped/compiled_data.csv")

# Food insecurity all specific to children: 

# What does food insecurity look like on a map?

# How does food insecurity relate to income and race?
fig, ax = plt.subplots(1, 3)
fig.set_figheight(10)
fig.set_figwidth(20)

def plot_food_insec(type_insec, label):
    label = label + " Food Insecurity"
    ax[0].set_title("Median Household Income versus " +  label)
    sns.regplot(data.MEDHHINC15, data[type_insec], line_kws={"color": "black"}, 
                scatter_kws={'alpha':0.3}, ax=ax[0])
    ax[0].set_xlabel("Median Household Income")
    ax[0].set_ylabel(label)
    
    ax[1].set_title("Poverty Rate versus " + label)
    sns.regplot(data.POVRATE15, data[type_insec], line_kws={"color": "black"}, 
                scatter_kws={'alpha':0.3}, ax=ax[1])
    ax[1].set_xlabel("Poverty Rate")
    ax[1].set_ylabel(label)
    
    ax[2].set_title("Percent White versus " + label)
    sns.regplot(data.PCT_NHWHITE10, data[type_insec], line_kws={"color": "black"}, 
                scatter_kws={'alpha':0.3}, ax=ax[2])
    ax[2].set_xlabel("Percent White of Population")
    ax[2].set_ylabel(label)
    
    ax[0].set_ylim(0, 40)
    ax[1].set_ylim(0, 40)
    ax[2].set_ylim(0, 40)
    ax[2].set_xlim(0, 100)

def plot_adult_food_insec():
    plot_food_insec("Food_Insec", "Adult")
    
def plot_child_food_insec():
    plot_food_insec("Food_Insec_Children", "Child")


'''
plt.figure(figsize=(20,20))
plt.scatter(data.PCT_NHWHITE10, data.Food_Insec)
plt.title("Percent white versus food insecurity")
plt.show()

# Snap versus food insecurity
plt.figure(figsize=(20,20))
plt.scatter(data.REDEMP_SNAPS16, data.Food_Insec)

corr = data.corr()[['Food_Insec', 'Food_Insec_Children']]
'''

# How much food insecurity is there?

# How do types and density of stores correlate with food insecurity?
# ie more junk food -> food insecurity?

# How does the population to area ratio affect food insecurity?

# How do food programs relate to food insecurity?

# How does adult food insecurity relate to children food insecurity?
