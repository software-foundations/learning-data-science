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

# Creating an 2-d array with zeros
my_tuple = ((5, 5))
arr = np.zeros(my_tuple)
print(arr)

# Creating an 1-d array with ones
arr = np.ones(8)
print(arr)

# Creating an 2-d array with ones
arr = np.ones((3, 5))
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

# 10 random integers between 0 and 99
arr = np.random.randint(0, 100, 10)

# Round the numbers of the arrays
arr = np.random.rand(5) * 100
arr_2 = np.round(arr, decimals=0)
print(arr_2)

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

"""
Indexing and Slicing arrays
"""


# Select element by index
arr = np.arange(0, 30, 3)
number = arr[4]
print(number)

# Slicing: selecet multiple elements
# like a list
arr = np.arange(0, 30, 3)

numbers = arr[0:4] # first 4 - 0 == 4 index elements
print(numbers)

numbers = arr[:4] # first 4 index elements
print(numbers)

numbers = arr[4:] # elements grather or equal than 4 index
print(numbers)

# attributing values to a slice of an array
arr_2 = arr.copy()
arr_2[4:] = 100
print(arr_2)
arr_2 = arr.copy()
arr_2[4:] = 100
print(arr_2)

# Slicing n-dim arrays
arr = np.arange(50).reshape(5, 10)
print(arr)
print(arr.shape)

def compare_arrays(arr, arr_2, arr_3):
	print(arr_2, id(arr_2))
	print(arr_3, id(arr_3))

	arr_boolean = arr_2 == arr_3 # compara values
	boolean: bool = arr_boolean.all() # true if all is true
	print(arr_boolean)
	print(boolean)

	arr_2[:] = 100 # setting 100 to all array elements
	print(arr_2)
	print(arr)


# way 01: arr.[lines][columns]
arr_2 = arr.copy()[:3][:] # copy function to avoid point to arr when alter arr_2 or arr_3
arr_3 = arr.copy()[:3]

compare_arrays(arr, arr_2, arr_3)

# way 02:
# comma notation
arr_2 = arr.copy()[1:4, ]
arr_3 = arr.copy()[1:4, :]

compare_arrays(arr, arr_2, arr_3)

# Select items by Logic operations in arrays
arr = np.arange(100).reshape(10, 10)
bol = arr > 50
arr_2 = arr.copy()[bol]

print(arr)
print(bol)
print(arr_2)

"""
Numpy Array Operations
"""

arr = np.arange(0, 16)

# sum
arr_2 = arr + arr
print(arr_2)

# sub
arr_2 = arr - arr
print(arr_2)

# multiplication
arr_2 = arr * arr
print(arr_2)

# division
arr_2 = arr / arr
"""
Error message equivalent to ZeroDivisionError in array operation (which not raise an error, and returns nan instead in 0/0)
<ipython-input-105-1a13d9f299b5>:1: RuntimeWarning: invalid value encountered in true_divide        
  arr_2 = arr / arr                               
[nan  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.] 
"""

# Index by index division
arr_3 = 1 / arr
"""
Error message equivalent to ZeroDivisionError in array operation (which not raise an error, and returns inf instead in 1/0)
"""
print(arr_2)

# Exponentiation: index by index
# Are the same with +, - * and / operations
arr_2 = arr ** 2
print(arr_2)

# square root
arr_2 = np.sqrt(arr)

# exponentiation of all array
arr_2 = np.exp(arr)

# mean
mean: np.float64 = np.mean(arr)

# standard deviation
std: np.float64 = np.std(arr)

# sin
arr_2: np.float64 = np.sin(arr)

# the major value of the array
max_value: np.int64 = np.max(arr)
max_value: np.int64 = arr.max()

# the mininum value of the array
min_value: np.int64 = np.min(arr)
min_value: np.int64 = arr.min()