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
                  "ORCHARD_ACRES07", "FIPS", "FIPS"], 1)
# Food insecurity all specific to children: 

# What does food insecurity look like on a map?

# How does food insecurity relate to income and race?
plt.figure(figsize=(10,10))
plt.scatter(data.MEDHHINC15, data.Food_Insec)
plt.title("Median household income versus food insecurity")
plt.show()

plt.figure(figsize=(10,10))
plt.scatter(data.POVRATE15, data.Food_Insec)
plt.title("Poverty rate versus food insecurity")
plt.show()

plt.figure(figsize=(10,10))
plt.scatter(data.PCT_NHWHITE10, data.Food_Insec)
plt.title("Percent white versus food insecurity")
plt.show()

# Snap versus food insecurity
plt.figure(figsize=(10,10))
plt.scatter(data.REDEMP_SNAPS16, data.Food_Insec)

corr = data.corr()[['Food_Insec', 'Food_Insec_Children']]

# How much food insecurity is there?

# How do types and density of stores correlate with food insecurity?
# ie more junk food -> food insecurity?

# How does the population to area ratio affect food insecurity?

# How do food programs relate to food insecurity?

# How does adult food insecurity relate to children food insecurity?

