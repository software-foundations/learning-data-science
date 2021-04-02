from datasets import load_dataframe_tips, load_dataframe_flights
from plots import heatmap, clustermap
import matplotlib.pyplot as plt
import numpy as np


# load datasets

flights = load_dataframe_flights()
tips = load_dataframe_tips()

# general data analysis

flights.head()
tips.head()
flights.info()

# heatmap - data analysis
# pivot table is the ideal format to plot heatmap

corr = tips.corr()
pvt_passengers_month_year = flights.pivot_table(
	values='passengers',
	index='month',
	columns='year')

# heatmap - plot

# heatmap(corr)
# heatmap(corr, cmap='coolwarm')
# heatmap(corr, annot=True)
# heatmap(pvt_passengers_month_year)
# heatmap(pvt_passengers_month_year, cmap='magma')
# heatmap(pvt_passengers_month_year, linecolor='white', linewidths=1)
# heatmap(pvt_passengers_month_year, linecolor='#FFFFFF', linewidths=1)
# heatmap(pvt_passengers_month_year, linecolor='gray', linewidths=1, annot=True)

# clustermap

# clustermap(pvt_passengers_month_year)
clustermap(pvt_passengers_month_year, standard_scale=1)

plt.show()
