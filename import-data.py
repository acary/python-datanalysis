# Data Analysis with Python

# Importing Datasets

# 1. Python Package Libraries

# pandas
# numpy
# scipy

# 2. Visualization Libraries

# Matplotlib
# Seaborn

# 3. Algorithmic Libraries

# scikit-learn
# statsmodels

##################

# Importing

# Format (.csv, .json, .xlsx)
# Path

##################

import pandas as pd

url = ""

df = read_csv(path,header=None) # read_csv assumes a header, set to None if applicable

# See shape

dataframe.head # shows first n rows of data frame
dataframe.tail

# Assign column names using pandas

# Put column names in a list called headers

headers = []

# set df.columns = headers

df.columns = headers

# Export

# to_csv

# specify file path with name
