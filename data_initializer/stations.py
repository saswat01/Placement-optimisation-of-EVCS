import os
from data_initializer import SingletonClass, csv_reader


class Stations(object):
	"""
	A class which hold existing stations information like address, latitude and longitude etc..
	"""
	FUEL_TYPE = "Fuel Type Code"
	STREET = "Street Address"
	CITY = "City"
	STATE = "State"
	ZIP = "ZIP"
	LAT = "Latitude"
	LONG = "Longitude"
	FULL_ADDRESS = "Full Address"

	def __init__(self):
		"""
		Initialized existing gas or EV stations
		"""
		current_path = os.path.abspath(os.path.dirname(__file__))
		singleton_csv_reader = SingletonClass(csv_reader.CSVReader)
		self.resource_folder = os.path.join(current_path, "..", "resources")
		# Store csv reader reference
		self.csv_reader_instance = singleton_csv_reader(os.path.join(self.resource_folder, "alt_fuel_stations.csv"))
		self.simplified_csv = []
		self.fields_to_save = [Stations.FUEL_TYPE, Stations.STREET, Stations.CITY,
							    Stations.STATE, Stations.ZIP, Stations.LONG, Stations.LAT]

	def simplified_data(self):
		"""
		Read csv data and simplified as well for better usages
		:return: list of simplified data
		"""
		self.csv_reader_instance.read_csv()
		for cdata in self.csv_reader_instance.csv_data:
			data = {}
			for field in self.fields_to_save:
				data[field] = cdata[field]
			full_address = "{0} {1} {2} {3}".format(data[Stations.STREET], data[Stations.CITY],
													data[Stations.STATE], data[Stations.ZIP])
			data[Stations.FULL_ADDRESS] = full_address
			self.simplified_csv.append(data)
		return self.simplified_csv
