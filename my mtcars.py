import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
mtcars = data('mtcars')
mtcars.head()
df = mtcars
df
type(df)
df.columns
df.shape
df.describe
df.dtypes()
catcolumns = ['cyl','hp','carb','gear','vs']
catcolumns
df[catcolumns] = df[catcolumns].astype('category')
df.dtypes
len(df)
df[df['cyl'] == 8]
len(df[df['am'] == 0])
df.head(2)
df.iloc[0:3,0:5]
df.iloc[-1,0:2]
df.iloc[0:10:2,0::2]
mtcars = df
mtcars.loc[(mtcars['mpg'] > 23) | (mtcars['wt'] < 2)]
pd.set_option('display.max_columns', 15)
df.query('mpg > 23')
df.loc[lambda x: x['mpg'] > 24]
df.loc[lambda x: x['mpg'] > 24].loc[lambda x: x['wt'] < 2]
df.drop_duplicates()
mtcars.loc[:,['cyl','am', 'gear']]
mtcars.loc[:,['cyl','am', 'gear']].drop_duplicates()
fakecars = df
fakecars['mpg'] = fakecars['mpg']*1.5
fakecars.describe
