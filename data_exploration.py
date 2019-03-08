# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:46:20 2019

@author: ameli
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/prepped/compiled_data.csv")

# Food insecurity all specific to children: 

# What does food insecurity look like on a map?

# How does food insecurity relate to income and race?
plt.figure(figsize=(20,20))
plt.scatter(data.MEDHHINC15, data.Food_Insec)
plt.title("Median household income versus food insecurity")
plt.show()

plt.figure(figsize=(20,20))
plt.scatter(data.POVRATE15, data.Food_Insec)
plt.title("Poverty rate versus food insecurity")
plt.show()

plt.figure(figsize=(20,20))
plt.scatter(data.PCT_NHWHITE10, data.Food_Insec)
plt.title("Percent white versus food insecurity")
plt.show()

# Snap versus food insecurity
plt.figure(figsize=(20,20))
plt.scatter(data.REDEMP_SNAPS16, data.Food_Insec)

corr = data.corr()[['Food_Insec', 'Food_Insec_Children']]

# How much food insecurity is there?

# How do types and density of stores correlate with food insecurity?
# ie more junk food -> food insecurity?

# How does the population to area ratio affect food insecurity?

# How do food programs relate to food insecurity?

# How does adult food insecurity relate to children food insecurity?
