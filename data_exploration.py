# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:46:20 2019

@author: ameli
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/prepped/compiled_data.csv")
county = pd.read_csv("data/prepped/insec15-state-codes.csv")
county["County"] = county.COUNTY

sorted_data = data.sort_values(['County', 'State'])
sorted_data = sorted_data.reset_index(drop=True)
sorted_data = sorted_data.drop(index=123, axis=0) # drop duplicate Baltimore
sorted_data = sorted_data.reset_index(drop=True)

sorted_county = county.sort_values(['County', 'STATE'])
sorted_county = sorted_county.reset_index(drop=True)
sorted_county = sorted_county.drop(index=797, axis=0) # drop Dona Ana
sorted_county = sorted_county.reset_index(drop=True)


sorted_data['county_food_insec'] = sorted_county.FOOD_INSEC
sorted_data['test_county'] = sorted_county.County
sorted_data['test_state'] = sorted_county.STATE

sort_data = sorted_data[['State','County', 'test_county', 'county_food_insec', 'test_state']]

print("start")

i = 0
for row in sorted_data.iterrows():
    row = row[1]
    if (row['County'] != row['test_county']):
        print(i)
        print(str(row['County']) + "    |    " + str(row['test_county']))
        break
    i += 1



# Food insecurity all specific to children: 

# What does food insecurity look like on a map?
#plt.hist(data.FOODINSEC_CHILD_01_07)

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
