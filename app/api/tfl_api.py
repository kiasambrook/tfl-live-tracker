import requests

class TfLAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.tfl.gov.uk"

    def fetch_all_stop_points(self):
        """Fetch all stop points."""
        url = f"{self.base_url}/StopPoint/Mode/tube?app_key={self.api_key}"
        response = requests.get(url)

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
