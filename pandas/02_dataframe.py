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


###############
# Absent Data #
###############

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(d)

# Remove rows with absent data

df.dropna()

df.dropna(axis=0)

# Remove rows with at least 2 nan

df.dropna(thresh=2)

# replace nan values

df.fillna(value='Fill na')

# replace nan values of a colum by its mean

df['A'].fillna(value=df['A'].mean())

# replace nan values with foward fill method
# util in time series

df.fillna(method='ffill')


###########
# GroupBy #
###########

# creating df

data = {'Enterprise': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Name': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sale': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

# creating group

group = df.groupby('Enterprise')

# operate in the group

group.sum() # ignore text content in the column

group.count() # doesn't ignore text content

group.mean()

group.describe()

group.describe()['Sale']['mean']

# creating another group

group_name = df.groupby('Name')

group_name.sum()

# filter by line

group_name.sum().loc['Amy']


#########################################
# Concatenate, Merge, and Join Daframes #
#########################################

df1 = pd.DataFrame(data={
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']},
    index=[0, 1, 2, 3])

df2 = pd.DataFrame(data={
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']},
    index=[4, 5, 6, 7])

df3 = pd.DataFrame(data={
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']},
    index=[8, 9, 10, 11])


# Concatenate

list_df = [df1, df2, df3]

pd.concat(list_df)

pd.concat(list_df, axis=0)

pd.concat(list_df, axis=1)

# Merge

left = pd.DataFrame(data={
    'key': ['k0', 'k1', 'k2', 'k3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame(data={
    'key': ['k0', 'k1', 'k2', 'k3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(left=left, right=right)

pd.merge(left, right, how='inner', on='key')

# Merge 02

left = pd.DataFrame(data={
    'key1': ['k0', 'k0', 'k1', 'k2'],
    'key2': ['k0', 'k1', 'k0', 'k1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame(data={
    'key1': ['k0', 'k1', 'k1', 'k2'],
    'key2': ['k0', 'k0', 'k0', 'k0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']})

list_keys = ['key1', 'key2']

pd.merge(left, right, on=list_keys)

pd.merge(left, right, how='outer', on=list_keys)

pd.merge(left, right, how='right', on=list_keys)

pd.merge(left, right, how='left', on=list_keys)


# Join
# used when indexes are keys

left = pd.DataFrame(data={
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']},
    index=['k0', 'k1', 'k2'])

right = pd.DataFrame(data={
    'C': ['C0', 'C1', 'C2'],
    'D': ['D0', 'D1', 'D2']},
    index=['k0', 'k2', 'k3'])

# only join right rows which have indexs present in left

left.join(right)

# join all rows considering keys present in both left and right
# join all rows considering all indexes

left.join(right, how='outer')
