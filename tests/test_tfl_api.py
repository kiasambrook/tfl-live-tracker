import pytest

from app.api.tfl_api import TfLAPI

@pytest.fixture
def tfl_api():
    return TfLAPI(api_key="test_api_key")  # Use a test API key or mock it

def test_fetch_arrivals(tfl_api, requests_mock):
    stop_id = "490008660N"
    mock_response = [{"lineName": "Bus 10", "destinationName": "Oxford Circus", "timeToStation": 300}]
    requests_mock.get(f"https://api.tfl.gov.uk/StopPoint/{stop_id}/Arrivals?app_key=test_api_key", json=mock_response)
    
    arrivals = tfl_api.fetch_arrivals(stop_id)
    assert arrivals == mock_response
