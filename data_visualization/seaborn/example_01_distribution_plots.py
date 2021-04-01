from datasets import load_dataframe_tips
from plots import distplot, jointplot, pairplot, rugplot, kdeplot
import matplotlib.pyplot as plt


# load dataset

df = load_dataframe_tips()

# distplots

distplot(df, 'total_bill')
distplot(df, 'total_bill', kde=True)
distplot(df, 'total_bill', kde=False)
distplot(df, 'total_bill', bins=50)

# jointplots

jointplot(df, 'total_bill', 'tip')
jointplot(df, 'total_bill', 'tip', kind='reg')
jointplot(df, 'total_bill', 'tip', kind='hex')

# pairplot

pairplot(df)
pairplot(df, hue='sex')

# rugplot

rugplot(df, 'total_bill')

# kdeplot

kdeplot(df, 'total_bill')
rugplot(df, 'total_bill')

# show plots

plt.show()
