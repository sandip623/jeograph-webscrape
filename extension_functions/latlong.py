import googlemaps
from .internal_errors import LengthMismatchError
from typing import List, Dict

class LatLong:
    def __init__(self, job_list : List[Dict], api_key : str):
        self.job_list = job_list
        self.locations = [job['job_location'] for job in job_list]
        self.api_key = api_key

    # method to retrieve and assign, the latitude and longitude of a location
    def get_latlng(self):
        try:
            if len(self.job_list) == len(self.locations):
                gmaps = googlemaps.Client(key=self.api_key)
                for index, location in enumerate(self.locations):
                    self.job_list[index]['latlng'] = (gmaps.geocode(location+", UK"))[0]['geometry']['location']
                return self.job_list
            else:
                raise LengthMismatchError(expected_length=len(self.job_list), actual_length=len(self.locations))
        except Exception:
            return Exception