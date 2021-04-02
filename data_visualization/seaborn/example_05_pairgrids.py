from datasets import load_dataframe_iris, load_dataframe_tips
from plots import PairGridMap, PairGridMapDiag, PairGridMapUpper, PairGridMapLower
from plots import pairplot
from plots import FacetGridMap
import matplotlib.pyplot as plt
import seaborn as sns


# load dataset

iris = load_dataframe_iris()
tips = load_dataframe_tips()

# dataset analysis

# iris.head()
# iris.info()
# iris.head(20)
# iris['species'].value_counts()

# pairgrid plot

# obj1 = PairGridMap(iris).plot()
# obj2 = PairGridMapDiag(iris).plot()
# obj3 = PairGridMapUpper(iris).plot()
# obj4 = PairGridMapLower(iris).plot()

# pairplot - comparison

# pairplot(iris, hue='species')

# facegrid

# grid = sns.FacetGrid(tips, col='time', row='smoker')
# grid.map(plt.hist, 'total_bill')

FacetGridMap(tips, col='time', row='smoker').plot(y='total_bill')

plt.show()
