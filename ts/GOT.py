import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from tabulate import tabulate
import bq_helper
import os
data = pd.read_csv('usa_names_data.csv')
data.shape
data.head()
data.count
data1 = data.groupby('gender')
data1
data.columns
data.groupby(['gender','name']).size().reset_index('gender')
data.drop('Unnamed: 0',axis =1).reset_index()
data.groupby(['gender','name']).agg(np.sum).sort_values('count')
