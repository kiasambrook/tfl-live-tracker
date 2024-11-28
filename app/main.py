from config import TFL_API_KEY
from api.tfl_api import TfLAPI
from ui.cli_ui import CLIUI

def main():
    # Initialise the TfL API and UI
    tfl_api = TfLAPI(TFL_API_KEY)
    ui = CLIUI(tfl_api)

    # Example: Display arrivals for a hardcoded stop ID
    stop_id = "490008660N"  # Replace with a real stop ID
    ui.display_arrivals(stop_id)

if __name__ == "__main__":
    main()
