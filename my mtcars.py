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
