from config import TFL_API_KEY
from api.tfl_api import TfLAPI
from ui.main_window import MainWindow

def main():
    # Initialise the TfL API and UI
    tfl_api = TfLAPI(TFL_API_KEY)
    ui = MainWindow()
    ui.run()

if __name__ == "__main__":
    main()
