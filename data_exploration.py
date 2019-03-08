# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:46:20 2019

@author: ameli
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly as py
import plotly.figure_factory as ff
import geopandas
import shapely

data = pd.read_csv("data/prepped/compiled_data.csv")

# Food insecurity all specific to children: 

# What does food insecurity look like on a map?
plt.hist(data.Food_Insec)

# How does food insecurity relate to income and race?
#FOODINSEC_13_15
#MEDHHINC15
#plt.figure(figsize=(20,20))
#plt.scatter(data.MEDHHINC15, data.FOODINSEC_13_15)
#plt.show()

#POVRATE15
#plt.figure(figsize=(20,20))
#plt.scatter(data.POVRATE15, data.FOODINSEC_13_15)
#plt.show()

# How much food insecurity is there?

# How do types and density of stores correlate with food insecurity?
# ie more junk food -> food insecurity?

# How does the population to area ratio affect food insecurity?

# How do food programs relate to food insecurity?

# How does adult food insecurity relate to children food insecurity?
#%%

colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
endpts = list(np.linspace(1, 12, len(colorscale) - 1))
fips = data['FIPS'].tolist()
values = data['Food_Insec_Children'].tolist()

fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='Child Food Insecurity',
    legend_title='Child Food Insecuirty %'
)
py.offline.plot(fig, filename='choropleth_full_usa')