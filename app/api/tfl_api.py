import requests
import requests_cache

class TfLAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tfl.gov.uk"

    def fetch_all_stop_points(self):
        """Fetch all stop points."""
        session = requests_cache.CachedSession('stop_points_cache')
        url = f"{self.base_url}/StopPoint/Mode/tube?app_key={self.api_key}"

        # Check if the response is in the cache
        cached_response = session.cache.get_response(url)
        if cached_response:
            return cached_response.json()

        # If not in cache, make the API call
        response = session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code}")

    def fetch_arrivals(self, stop_id):
        """Fetch live arrivals for a given stop."""
        url = f"{self.base_url}/StopPoint/{stop_id}/Arrivals?app_key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching data: {response.status_code}")
