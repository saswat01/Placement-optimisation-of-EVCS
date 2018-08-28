import requests


class Path(object):
	"""
	Library to calculate distance between two destination
	"""
	GOOGLE_URI = "https://maps.googleapis.com/maps/api/directions/json"

	@classmethod
	def get_direction(cls, origin, dest, api_key):
		req = requests.get(cls.GOOGLE_URI, {"origin": origin, "destination": dest, "key": api_key})
		if req.status_code == 200:
			return req.json()
		else:
			msg = "Failed to get path origin={0}, dest={1}, reason={2}, response_code={3}".format(origin, dest, req.reason, req.status_code)
			print msg
			raise RuntimeError(msg)


