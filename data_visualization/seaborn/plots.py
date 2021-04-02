import seaborn as sns
from typing import Optional, Any

####################
# Distribution plots
####################

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


def kdeplot(
	df, 
	column: str, 
	*args, **kwargs) -> sns.kdeplot:
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


###################
# Categorical plots
###################

def barplot(
	df, 
	x: Optional[str] = None, 
	y: Optional[str] = None,	
	*args, **kwargs) -> sns.barplot:
	"""barplot function

	Arguments
	---------

	df : pandas dataframe

	x : column in dataframe

	y : column in dataframe

	args : arguments

	kwargs : keyword arguments

	-> return sns.barplot

	"""
	return sns.barplot(
		x=x,
		y=y,
		data=df,
		*args,
		**kwargs)	


def countplot(
	df,
	x: str,
	*args, **kwargs) -> sns.countplot:
	"""countplot function

	Arguments
	---------

	df : pandas dataframe

	x : column in df
	
	args : arguments

	kwargs : keyword arguments

	-> return : sns.countplot
	"""

	return sns.countplot(
		data=df,
		x=x,
		*args,
		**kwargs)


def boxplot(
	df,
	x: Optional[str] = None,
	y: Optional[str] = None,
	palette: Optional[str] = None,
	hue: Optional[str] = None,
	orient: Optional[str] = None,
	*args, **kwargs) -> sns.boxplot:
	"""boxplot function

	Arguments
	---------

	df : pandas dataframe

	x : column in df

	y : column in df

	palette : color scheme

	hue : column in df

	orient: v (vertical) or h (horizontal)

	args : arguments

	kwargs : keyword arguments

	-> return : sns.boxplot
	"""
	
	return sns.boxplot(
		x=x,
		y=y,
		data=df,
		palette=palette,
		hue=hue,
		orient=orient,
		*args,
		**kwargs)


def violinplot(
	df,
	x: str,
	y: str,
	hue: Optional[str] = None,
	split: Optional[bool] = False,
	*args,
	**kwargs) -> sns.violinplot:
	"""violinplot function
	
	Arguments
	---------

	df : pandas dataframe

	x : column in df

	y : column in df

	hue : column in df

	args : arguments

	kwargs : keyword arguments

	-> return : sns.violinplot
	"""
	return sns.violinplot(
		data=df,
		x=x,
		y=y,
		hue=hue,
		split=split,
		*args,
		**kwargs)


def stripplot(
	df,
	x: str,
	y: str,
	jitter: Optional[bool] = False,
	hue: Optional[str] = None,
	dodge: Optional[bool] = False,
	*args, **kwargs) -> sns.stripplot:
	"""stripplot function
	
	Arguments
	---------

	df : pandas dataframe

	x : column in df

	y : column in df

	jitter : to sparse points, or not

	hue : column in df

	dodge : to sparse points (util when use hue)

	args : arguments

	kwargs : keyword arguments

	-> return : sns.stripplot
	"""
	return sns.stripplot(
		data=df,
		x=x,
		y=y,
		jitter=jitter,
		hue=hue,
		dodge=dodge,
		*args,
		**kwargs)


def swarmplot(**kwargs) -> sns.swarmplot:
	"""swarmplot function

	Arguments
	---------

	data : pandas dataframe

	x : column in df

	y : column in df

	hue : column in df	

	dodge : to sparse points (util when use hue)

	color : color of points

	kwargs : keyword arguments

	-> return : sns.swarmplot
	"""

	return sns.swarmplot(**kwargs)


def catplot(
	df,
	x: str,
	y: str,
	kind: Optional[str] = None,
	**kwargs) -> sns.catplot:
	"""factorplot function
	
	Arguments
	---------

	df : pandas dataframe

	x : column in df

	y : column in df

	kind : kind of plot. Egg: 'bar'
	"""

	return sns.catplot(
		data=df,
		x=x,
		y=y,
		kind=kind,
		**kwargs)