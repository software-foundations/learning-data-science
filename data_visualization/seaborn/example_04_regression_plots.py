from datasets import load_dataframe_tips
from plots import lmplot
import matplotlib.pyplot as plt


# load dataset

tips = load_dataframe_tips()

# lmplot - linear model plot

# lmplot(tips, x='total_bill', y='tip')
# lmplot(tips, x='total_bill', y='tip', hue='sex')
# lmplot(tips, x='total_bill', y='tip', palette='coolwarm')
# lmplot(tips, x='total_bill', y='tip', hue='sex', palette='coolwarm')
# lmplot(tips, x='total_bill', y='tip', markers=['v'])
# lmplot(tips, x='total_bill', y='tip', hue='sex', markers=['o', 'v'])
# lmplot(tips, x='total_bill', y='tip', scatter_kws={'s': 1})
# lmplot(tips, x='total_bill', y='tip', hue='sex', col='sex')
# lmplot(tips, x='total_bill', y='tip', hue='sex', col='sex', row='time')
# lmplot(tips, x='total_bill', y='tip', col='sex', row='time')
# lmplot(tips, x='total_bill', y='tip', hue='sex', col='day')
lmplot(tips, x='total_bill', y='tip', hue='sex', col='day', aspect=0.6, height=16)

plt.show()
