# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:46:20 2019

@author: ameli
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/prepped/compiled_data.csv")
county = pd.read_csv("data/prepped/insec15-state-codes.csv")


# Food insecurity all specific to children: 

# What does food insecurity look like on a map?
plt.hist(data.FOODINSEC_CHILD_01_07)

# How does food insecurity relate to income and race?
#FOODINSEC_13_15
#MEDHHINC15
plt.figure(figsize=(20,20))
plt.scatter(data.MEDHHINC15, data.FOODINSEC_13_15)
plt.show()

#POVRATE15
plt.figure(figsize=(20,20))
plt.scatter(data.POVRATE15, data.FOODINSEC_13_15)
plt.show()

# How much food insecurity is there?

# How do types and density of stores correlate with food insecurity?
# ie more junk food -> food insecurity?

# How does the population to area ratio affect food insecurity?

# How do food programs relate to food insecurity?

# How does adult food insecurity relate to children food insecurity?
