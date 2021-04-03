from datasets import load_dataframe_tips
from plots import countplot, lmplot
from styles import *
import matplotlib.pyplot as plt


tips = load_dataframe_tips()


#########
# Seaborn
#########

# sns_style_grid_darkgrid()
# sns_style_grid_white()
# sns_style_grid_ticks()
# sns_style_grid_whitegrid()
# sns_style_grid_dark()

# sns_style_spine_remove()
# sns_style_spine_remove(left=True)

# sns_context(context='poster')
# sns_context_context_poster()
sns_context_context_poster_font_scale_2()

############
# Matplotlib
############

# plt_figure()
# plt_figure_size(12, 8)

#########
# plots
#########

# countplot(tips, x='sex')

# lmplot(
# 	tips, 
# 	x='total_bill', 
# 	y='tip', hue=None, 
# 	palette=None, markers="o", 
# 	scatter_kws=None, col=None, 
# 	row=None, 
# 	aspect=4, 
# 	height=2)

# lmplot(
# 	tips, 
# 	x='total_bill', 
# 	y='tip', hue='sex', 
# 	palette='coolwarm', markers="o", 
# 	scatter_kws=None, col=None, 
# 	row=None, 
# 	aspect=4, 
# 	height=2)

lmplot(
	tips, 
	x='total_bill', 
	y='tip', hue='sex', 
	palette='inferno', markers="o", 
	scatter_kws=None, col=None, 
	row=None, 
	aspect=4, 
	height=2)

plt.show()
