# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:46:20 2019

@author: ameli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.figure_factory as ff

data = pd.read_csv("data/prepped/compiled_data.csv")
data = data.drop(["FOODINSEC_CHILD_03_11", "FOODINSEC_CHILD_01_07", "PERCHLDPOV10", "PERPOV10", "FOODINSEC_10_12",
                  "VLFOODSEC_10_12", "PCT_LACCESS_HHNV10", "PCT_NHBLACK10", "FOODINSEC_13_15", "VLFOODSEC_13_15",
                  "MILK_PRICE10", "REDEMP_WICS08", "PCT_NHNA10", "SNAP_CAP09", "PCT_LACCESS_LOWI10", "PCT_HISP10",
                  "ORCHARD_ACRES07", "Unnamed: 0"], 1)

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

# Snap versus food insecurity
plt.figure(figsize=(10,10))
plt.scatter(data.REDEMP_SNAPS16, data.Food_Insec)

corr = data.corr()[['Food_Insec', 'Food_Insec_Children']]

def plot_snap():
    fig, ax = plt.subplots()
    fig.set_figheight(7)
    fig.set_figwidth(14)
    
    ax.set_title("SNAP Distribution vs. Child Food Insecurity")
    sns.regplot(data.REDEMP_SNAPS16, data.Food_Insec_Children, line_kws={"color": "black"}, 
                scatter_kws={'alpha':0.3}, ax=ax)
    ax.set_xlabel("SNAP Distribution")
    ax.set_ylabel("Child Food Insecurity")

def draw_map():
    
    #set_creds()
    init_notebook_mode(connected=True)
    data = pd.read_csv("data/prepped/compiled_data.csv")
    
    colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
                  "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
                  "#08519c","#0b4083","#08306b"]
    endpts = list(np.linspace(1, 25, len(colorscale) - 1))
    fips = data['FIPS'].tolist()
    values = data['Food_Insec_Children'].tolist()
    
    fig = ff.create_choropleth(
        fips=fips, values=values,
        binning_endpoints=endpts,
        colorscale=colorscale,
        show_state_data=True,
        show_hover=True, centroid_marker={'opacity': 0},
        asp=2.9, title='Child Food Insecurity',
        legend_title='Child Food Insecuirty %'
    )
    plotly.offline.iplot(fig, filename='choropleth_full_usa')

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
def plot_insec_distribution():
    fig, ax = plt.subplots()
    fig.set_figheight(7)
    fig.set_figwidth(14)
    label = ["Children", "Adult"]
    for i, a in enumerate([data.Food_Insec_Children, data.Food_Insec]):
        sns.distplot(a, bins=range(1, 40, 2), ax=ax, kde=False, label=label[i])
    ax.set_xlim([0, 40])
    ax.legend()
    ax.set_title("Food Insecurity")
    ax.set_xlabel("Food Insecurity Percentage")
    ax.set_ylabel("Count")

# How do types and density of stores correlate with food insecurity?
# ie more junk food -> food insecurity?

# How does the population to area ratio affect food insecurity?

# How do food programs relate to food insecurity?

# How does adult food insecurity relate to children food insecurity?
