import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
% matplotlib inline
% matplotlib qt # when use terminal


from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

import cufflinks as cf

print(__version__)

# initialize plotly and cufflinks

init_notebook_mode(connected=True)

cf.go_offline()

# create dataframe

df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())

df.head()

df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})

df2.head()

####################################
# Use iplot with jupyter-notebooks
# Use plot with terminal
####################################

###############
# pandas plot #
###############

df.plot(kind='scatter', x='A', y='B')


###############
# plotly plot #
###############

# plotly - scatter

df.iplot(kind='scatter', x='A', y='B', mode='markers') # jupyter-notebooks

# plotly - bar

df2.iplot(kind='bar', x='Category', y='Values')  # jupyter-notebooks

df.iplot(kind='bar') # jupyter-notebooks

df.count().iplot(kind='bar') # jupyter-notebooks

# plotly - boxplot

df.iplot(kind='box')

# plotly - 3d surface: only in jupyter-notebooks

df3 = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50], 'z': [5, 4, 3, 2, 1]})

df3.iplot(kind='surface')

df3.iplot(kind='surface', colorscale='rdylbu')

# plotly - spread

df[['A', 'B']].iplot(kind='spread')

# plotly - histogram

df['A'].iplot(kind='hist')

df['A'].iplot(kind='hist', bins='50')

# plotly - scatter_matrix

df.scatter_matrix()
