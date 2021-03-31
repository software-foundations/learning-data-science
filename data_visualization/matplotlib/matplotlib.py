# import matplotlib.pyplot as plt
# %matplotlib inline # doesn't work in ipython kernel

import PyQt5
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

import numpy as np
import pandas as pd

from typing import List

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


######################
# Matplotlib - part 02
######################

# -> fig and axes

x = np.linspace(0, 5, 11)

fig, ax = plt.subplots()

ax.plot(x, x**3, color='r')

ax.plot(x, x**4, color='b')

fig.show()


# -> fig and axes

x = np.linspace(0, 5, 11)

fig, ax = plt.subplots()

ax.plot(x, x**3, color='r')

ax.plot(x, x**4, color='b')

ax.set_xlabel('x')

ax.set_ylabel('y')

ax.set_title('title')

fig.show()


# -> fig and axes - array of axes 01

fig, ax = plt.subplots(nrows=1, ncols=2)

fig.show()

for axe in ax:
	axe.set_xlabel('x')
	axe.set_ylabel('y')
	axe.set_title('title')
	axe.plot(x, x ** 4, color='r')

fig.show()


# -> fig and axes - array of axes 02

fig, ax = plt.subplots(nrows=1, ncols=2)

ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[0].set_title('title')
ax[0].plot(x, x ** 4, color='r')

ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[1].set_title('title')
ax[1].plot(x, x ** 4, color='r')

fig.show()


# -> tight layouts
# to avoid overlap plots

fig, ax = plt.subplots(nrows=5, ncols=5)

plt.tight_layout()

plt.show()


# -> figsize

fig = plt.figure(figsize=(8, 4), dpi=100)


# -> figsize 02

fig, axes = plt.subplots(figsize=(12, 3))

axes.plot(x, y, color='r')

axes.set_title('title')

fig.show()


# -> savefig

fig.savefig('image1.png')
fig.savefig('image2.jpg')


# -> axes.legend

fig, axes = plt.subplots(figsize=(8, 4))

axes.plot(x, y, color='r', label='Data 01')

axes.plot(y, x, color='g', label='Data 02')

# 0 - matplotlib defines
axes.legend(loc=0)

# axes.legend(loc=1)
# axes.legend(loc=2)
# axes.legend(loc=3)
# axes.legend(loc=4)
# axes.legend(loc=5)

fig.show()