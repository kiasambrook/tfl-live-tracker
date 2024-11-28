class CLIUI:
    def __init__(self, tfl_api):
        self.tfl_api = tfl_api

    def display_arrivals(self, stop_id):
        """Fetch and display arrivals for a specific stop."""
        try:
            arrivals = self.tfl_api.fetch_arrivals(stop_id)
            print(f"Arrivals for Stop ID {stop_id}:")
            for arrival in arrivals:
                print(f"- {arrival['lineName']} to {arrival['destinationName']} in {arrival['timeToStation'] // 60} mins")
        except Exception as e:
            print(f"Error: {e}")
