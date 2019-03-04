import pandas as pd

# Read in data file
xls = pd.ExcelFile('./data/raw/DataDownload.xls')
variables = pd.read_excel(xls, 'Variable List')
county_supp_data = pd.read_excel(xls, 'Supplemental Data - County')
state_supp_data = pd.read_excel(xls, 'Supplemental Data - State')
access = pd.read_excel(xls, 'ACCESS')
stores = pd.read_excel(xls, 'STORES')
restaurants = pd.read_excel(xls, 'RESTAURANTS')
assistance  = pd.read_excel(xls, 'ASSISTANCE')
insecurity = pd.read_excel(xls, 'INSECURITY')
prices_taxes = pd.read_excel(xls, 'PRICES_TAXES')
local = pd.read_excel(xls, 'LOCAL')
health = pd.read_excel(xls, 'HEALTH')
socioeconomic = pd.read_excel(xls, 'SOCIOECONOMIC')

# Explore variables


# Scope variables
scoped = pd.DataFrame()

# Write scoped variables to new csv
scoped.to_csv('./data/prepped/compiled_data.csv', sep=",")