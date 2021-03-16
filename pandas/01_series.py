import numpy as np
import pandas as pd


labels = ['a', 'b', 'c']

my_list = [10, 20, 30]

my_arr = np.array(([10, 20, 30]))

my_dict = {'a': 10, 'b': 20, 'c': 30}

# -> Creating a pd.Series from a list
# pd.Series structure seams like a dict

series = pd.Series(data=my_list, index=labels)

# -> Acessing series items
# seams like access item in a dictionary

item = series['b']

# -> Creating a pd.Series from a numpy array

series = pd.Series(data=my_arr, index=labels)

# -> Storage function definitions in a pd.Series

series = pd.Series(data=[print, sum])

# -> examples

# -> sum series by its index
# When index not mach from each other, return NaN
# index can be at different places

ser1 = pd.Series(data=[1, 2, 3, 4], index=['USA', 'Germany', 'URSS', 'Japan'])

ser2 = pd.Series(data=[1, 2, 3, 4], index=['Germany', 'USA', 'Italy', 'Japan'])

ser1 + ser2