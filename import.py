import pandas as pd
import numpy as np
pd.set_option('max_rows',20)
data = pd.read_csv('denco data.csv')
dd = data 
dd
data.index
data.dtypes
data.columns
dd.describe()
dd.sortby('revenue')
x = dd.groupby('custname')
x.sort_values()
dd.groupby('custname').agg(np.sum).sort_values('revenue')
n1 = {5,6,7}
type(n1)
n1.intersection_update({7,10,3,5})
n1
