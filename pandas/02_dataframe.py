import numpy as np
import pandas as pd
from typing import Tuple, List

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


#######################
# Multi level indexes #
#######################

# Levels of index

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']

inside = [1, 2, 3, 1, 2, 3]

list_tuples: List[Tuple] = list(zip(outside, inside))

hier_index = pd.MultiIndex.from_tuples(list_tuples)

# Creating dataframe

data = np.random.randn(6, 2)

df = pd.DataFrame(data=data, index=hier_index, columns=['A', 'B'])

# Acessing index levels

df.loc['G1']

df.loc['G2']

# Naming index levels

df.index.names

df.index.names = ['Group', 'Number']

df.index.names

df

# -> Cross sections

# outside level

df.xs(key='G1', axis=0, level='Group')

df.xs('G1')

# inside level

df.xs(key=1, axis=0, level='Number')

df.xs(1, level='Number')
