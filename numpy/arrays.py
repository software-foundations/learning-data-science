import numpy as np

# Creating an 1d - array
li = [1, 2, 3]
arr = np.array(li)
print(arr)

# Creating an 2d - array
li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(li)
print(arr)

# Creating an array of a number sequence
arr = np.arange(0, 10)
print(arr)
arr = np.arange(0, 10, step=2)
print(arr)

# Creating an 1-d array with zeros
arr = np.zeros(3)
print(arr)
print(max_value)
print(min_value)
# Creating an 2-d array with zeros
my_tuple = ((5,5))
arr = np.zeros(my_tuple)
print(arr)

# Creating an 1-d array with ones
arr = np.ones(8)
print(arr)

# Creating an 2-d array with ones
arr = np.ones((3,5))
print(arr)

# Creating identity matrix
arr = np.eye(5)
print(arr)

# Creating an array
# initialize in a number
# finalizes in a number
# specifying the numbers of elements between initial and final number
initial = 0
final = 1
n_numbers = 3

arr = np.linspace(initial, final, n_numbers)
print(arr)

# Creating random numbers
# between 0 and 1
# with equal problably to be selected
# extrated from a uniform distribution

# 1-dimensional
n_numbers = 5
arr = np.random.rand(n_numbers)
print(arr)

# n-dimensional
arr = np.random.rand(10, 5)
print(arr)

# Creating random numbers
# between 0 and 1
# extracted from a normal distribution

# 1-dimensional
arr = np.random.rand(5)
print(arr)

# n-dimensional
arr = np.random.rand(10, 5)
print(arr)

# Creating random numbers
# integers
print(max_value)
print(min_value)
# 10 random integers between 0 and 99
arr = np.random.randint(0, 100, 10)

# Round the numbers of the arrays
arr = np.random.rand(5) * 100
arr_2 = np.round(arr, decimals=0)
prtin(arr_2)

# Reshape
arr = np.random.rand(25)
print(arr)

tpl: tuple = (5,5)
arr_2 = arr.reshape(tpl)

print(arr_2)
print(arr_2.shape) # shape attribute

# Find the max/min value of an array
arr = np.random.rand(2)
max_value = arr.max()
min_value = arr.min()
print(arr)
print(max_value)
print(arr, min_value)

# Find the index of the max/min value of an array
arr = np.random.rand(2)
max_value = arr.argmax()
min_value = arr.argmin()
print(arr)
print(max_value)
print(min_value)
print(max_value)
print(min_value)
