# import matplotlib.pyplot as plt
# %matplotlib inline # doesn't work in ipython kernel

import PyQt5
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

import numpy as np
import pandas as pd

######################
# Matplotlib - part 01
######################

x = np.linspace(0, 5, 11)

y = x * x

# -> Functional

plt.plot(x, y, color='r')

plt.xlabel('Axis x')

plt.ylabel('Axis y')

plt.title('Title')

plt.show()


# -> Subplots

plt.subplots(nrows=1, ncols=2)

plt.show()


# -> Subplot 02

plt.subplot(1, 2, 1)

y = x * x

plt.plot(x, y, color='r')

plt.subplot(1, 2, 2)

y = - np.e ** x

plt.plot(x, y, color='g')

plt.show()


# -> Figure and its axes

fig = plt.figure()

left, bottom = 0.1, 0.1

width, height = 0.8, 0.8

rect = [left, bottom, width, height]

axes = fig.add_axes(rect=rect)

axes.plot(x, y)

axes.set_xlabel('Axis x')

axes.set_ylabel('Axis y')

axes.set_title('Title')

plt.show()


#-> Figure and its axes


# figure

fig = plt.figure()

# axes

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes2 = fig.add_axes([0.2, 0.5, 0.3, 0.3])

# axes1

axes1.plot(x, y)

axes1.set_xlabel('Axis x')

axes1.set_ylabel('Axis y')

axes1.set_title('Title')

# axes 2

axes2.plot(x, y, color='r')

plt.show()