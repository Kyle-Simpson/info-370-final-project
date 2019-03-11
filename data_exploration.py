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
data = data.drop(["FOODINSEC_CHILD_03_11", "FOODINSEC_CHILD_01_07", "PERCHLDPOV10", "PERPOV10", "FOODINSEC_10_12",
                  "VLFOODSEC_10_12", "PCT_LACCESS_HHNV10", "PCT_NHBLACK10", "FOODINSEC_13_15", "VLFOODSEC_13_15",
                  "MILK_PRICE10", "REDEMP_WICS08", "PCT_NHNA10", "SNAP_CAP09", "PCT_LACCESS_LOWI10", "PCT_HISP10",
                  "ORCHARD_ACRES07", "Unnamed: 0"], 1)
# Food insecurity all specific to children: 

# What does food insecurity look like on a map?

# How does food insecurity relate to income and race?



def plot_food_insec(type_insec, label):
    fig, ax = plt.subplots(1, 3)
    fig.set_figheight(5)
    fig.set_figwidth(20)

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
    plt.show()

def plot_adult_food_insec():
    plot_food_insec("Food_Insec", "Adult")
    
def plot_child_food_insec():
    plot_food_insec("Food_Insec_Children", "Child")


correl = abs(data.corr()['Food_Insec_Children'])
correl = correl.drop(['Food_Insec_Children', 'Food_Insec'], 0)
correl = correl[correl >= .1]

def plot_income():
    fig, ax = plt.subplots(1, 3)
    fig.set_figheight(5)
    fig.set_figwidth(20)
    
    sns.distplot(data.MEDHHINC15.dropna(), kde=False, ax=ax[0])
    ax[0].set_title("Histogram of Median Income")
    ax[0].set_xlabel("Median Household Income")
    
    sns.distplot(data.POVRATE15.dropna(), kde=False, ax=ax[1])
    ax[1].set_title("Histogram of Poverty Rate")
    ax[1].set_xlabel("Poverty Rate")
    
    sns.regplot(data.MEDHHINC15, data.POVRATE15, ax=ax[2], 
                scatter_kws={'alpha':0.3}, line_kws={"color": "black"})
    ax[2].set_title("Median Income versus Poverty Rate")
    ax[2].set_xlabel("Median Household Income")
    ax[2].set_ylabel("Poverty Rate")
    ax[2].set_ylim(0, 60)
    plt.show()
    

# How much food insecurity is there?

# How do types and density of stores correlate with food insecurity?
# ie more junk food -> food insecurity?

# How does the population to area ratio affect food insecurity?

# How do food programs relate to food insecurity?

# How does adult food insecurity relate to children food insecurity?
