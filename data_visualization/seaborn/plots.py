import seaborn as sns
from typing import Optional


def distplot(
	df, 
	column: str, 
	*args, 
	**kwargs) -> sns.displot:
	"""Distplot function

	Arguments
	---------

	df : pandas dataframe

	columns: column of df

	args: arguments

	kwargs: keyword arguments

	-> return : sns.distplot
	"""

	return sns.displot(
		df[column], 
		*args, 
		**kwargs)


def jointplot(
	df, 
	x: str, 
	y: str, 
	*args, **kwargs) -> sns.jointplot:
	"""jointplot function

	Arguments
	---------

	df : pandas dataframe

	x : column in df

	y : column in df

	args: arguments

	kwargs: keyword arguments

	-> return : sns.jointplot
	"""

	return sns.jointplot(x=x, y=y, data=df, *args, **kwargs)
	

def pairplot(
	df, 
	hue: Optional[str] = None, 
	palette: Optional[str] = None, 
	*args, **kwargs) -> sns.pairplot:
	"""pairplot function

	Arguments
	---------
	
	df : pandas dataframe

	hue : column in df

	palette : color scheme

	-> return : sns.pairplot
	"""

	return sns.pairplot(
		df,
		hue=hue,
		palette=palette,
		*args,
		**kwargs)


def rugplot(
	df, 
	column: str, 
	*args, **kwargs) -> sns.rugplot:
	"""rugplot function

	Arguments
	---------

	df : pandas dataframe

	column : column in df

	args : arguments

	kwargs : keyword arguments

	-> return : sns.rugplot

	"""
	return sns.rugplot(
		df[column], 
		*args, 
		**kwargs)


def kdeplot(df, column: str, *args, **kwargs) -> sns.kdeplot:
	"""kdeplot function

	Arguments
	---------

	df : pandas dataframe

	column : column in df

	args : arguments

	kwargs : keyword arguments

	-> return : sns.kdeplot
	"""

	return sns.kdeplot(
		df[column],
		*args,
		**kwargs)
