from datasets import load_dataframe_tips
from plots import barplot, countplot, boxplot, violinplot, stripplot, swarmplot, catplot
import matplotlib.pyplot as plt
import numpy as np


df = load_dataframe_tips()

# barplot(df, x='sex', y='total_bill')
# barplot(df, x='sex', y='total_bill', estimator=np.std)

# countplot(df, x='sex')

# boxplot(df, x='day', y='total_bill')
# boxplot(df, x='day', y='total_bill', palette='rainbow')
# boxplot(df, x='day', y='total_bill', hue='sex')
# boxplot(df, orient='h')

# violinplot(df, x='day', y='tip')
# violinplot(df, x='day', y='tip', hue='sex')
# violinplot(df, x='day', y='tip', hue='sex')
# violinplot(df, x='day', y='tip', hue='sex', split=True)

# stripplot(df, x='day', y='total_bill')
# stripplot(df, x='day', y='total_bill', jitter=True)
# stripplot(df, x='day', y='total_bill', jitter=True, hue='sex')
# stripplot(df, x='day', y='total_bill', jitter=True, hue='sex', dodge=True)

# swarmplot(data=df, x='day', y='total_bill')
# swarmplot(data=df, x='day', y='total_bill', hue='sex', dodge=True)
# swarmplot(data=df, x='day', y='total_bill', hue='sex', dodge=True, color='black')

# violin + swarmplot

# swarmplot(data=df, x='day', y='total_bill', color='black')
# violinplot(df, x='day', y='total_bill')

catplot(df, x='sex', y='total_bill', kind='bar')

plt.show()

