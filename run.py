import argparse

from data_initializer import stations, SingletonClass
from graph_lib import path


class Runner(object):
	"""
	Main class which is used to run this project
	"""

	def __init__(self, distance_threshold, api_key):
		"""
		:param distance_threshold: distance threshold which is being used by algorithm to calculate
			right distance for
		"""
		if not (isinstance(distance_threshold, float) and distance_threshold > 0):
			raise ValueError("Invalid threshold value (needs float value)")
		if not isinstance(api_key, basestring):
			raise ValueError("Invalid api key, refer help (-h) for more information")
		self.distance_threshold = distance_threshold
		self.api_key = api_key

	def run(self):
		"""
		Running algorithm here
		:return: None
		"""
		singleton_stations = SingletonClass(stations.Stations)
		existing_stations = singleton_stations()
		# read sample data
		data = existing_stations.simplified_data()
		# TODO - change me (Sample code to calculate path)
		# Calculate path between two points
#		print path.Path.get_direction(data[0]["Full Address"], data[1]["Full Address"],
#									  self.api_key)


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--threshold', help="threshold distance between points",
						required=True, type=float)
	parser.add_argument('-a', '--api_key', help="Google api key for distance matrix,"
												" refer - https://developers.google.com/maps/documentation/distance-matrix/get-api-key for more infromation",
						required=True, type=str)
	args = parser.parse_args()
	return args


if __name__ == "__main__":
	args = parse_args()
	runner = Runner(args.threshold, args.api_key)
	runner.run()
