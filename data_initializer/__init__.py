"""
Singleton Decorator to define singleton class
"""


class SingletonClass(object):
	"""
		A decorator class to define any class as singleton
	"""

	def __init__(self, class_name):
		"""
		Init method
		:param class_name: class name
		"""
		self.class_name = class_name
		self.instance = None

	def __call__(self, *args, **kwargs):
		"""
		Overwrite __class__ method
		:param args: list of arguments
		:param kwargs: list of key, value args
		:return: class instance
		"""
		if self.instance is None:
			self.instance = self.class_name(*args, **kwargs)
		return self.instance
