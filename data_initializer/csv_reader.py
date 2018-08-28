import csv
import os


class CSVReader(object):

	"""
	Main class to read CSV file
	"""
	def __init__(self, filename):
		"""
		Initialized csv reader class
		:param filename: file path including file name
		"""
		if not isinstance(filename, basestring):
			raise ValueError("Invalid file name")
		if not os.path.isfile(filename):
			raise ValueError("Provide file is not valid file path")
		self.filename = filename
		self.csv_data = []

	def read_csv(self):
		"""
		Read csv file
		:return: list of data read from csv
		"""
		try:
			csv_fp = open(self.filename, 'rb')
			reader = csv.DictReader(csv_fp)
			for line in reader:
				self.csv_data.append(line)
			return self.csv_data
		except IOError as e:
			print e
			raise e
		finally:
			csv_fp.close() if csv_fp is not None else None
