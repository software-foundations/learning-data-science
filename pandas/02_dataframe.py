import numpy as np
import pandas as pd


np.random.seed(101)

data = np.random.randn(5, 4)

index = "A B C D E".split()

columns = "W X Y Z".split()

# -> Creating dataframe

df = pd.DataFrame(data, index, columns)

# -> Slicing dataframe

df['W']

df[['W', 'Z']]

df.W

# -> Creating nem column

df['new'] = df['W'] + df['X']

# -> deleting axis
# 0 - line
# 1 - column

df.drop('new', axis=1, inplace=True)

df = df.drop('new', axis=1)

# -> Types

type(df['W']) # pandas.core.series.Series

type(df) # pandas.core.frame.DataFrame

# -> filter by df.loc[line, column]

df.loc['A', 'W']

df.loc[['A', 'B'], ['X', 'Y', 'Z']]

# -> filter by df.iloc[]
# same way as numpy goes

df.iloc[0:2, 1:]

##################################
# Condition selection, set_index #
##################################

bol = df > 0

df[bol]

df[df['W'] > 0]

bol2 = df['W'] > 0

df2 = df[bol2]

df2['Y']

bol3 = (df['W'] > 0) & (df['Y'] > 1)

df[bol3]

bol4 = (df['W'] > 0) | (df['Y'] > 1)

# -> Reset Index
# reset_index

df.reset_index()

df.reset_index(inplace=True)

df = pd.DataFrame(data, index, columns)

col = 'RS RJ SP AM SC'.split()

df['Country'] = col

df.set_index('Country')

df.set_index('Country', inplace=True)
