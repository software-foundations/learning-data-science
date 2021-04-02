import seaborn as sns

def load_dataframe_tips():
	"""load tips dataframe"""	
	return sns.load_dataset('tips')


def load_dataframe_flights():
	"""load flights dataframe"""
	return sns.load_dataset('flights')


def load_dataframe_iris():
	"""load iris dataframe"""
	return sns.load_dataset('iris')
