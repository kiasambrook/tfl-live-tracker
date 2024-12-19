from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from ui.dropdown import Dropdown
from api.tfl_api import TfLAPI
from config import TFL_API_KEY


class MainWindow(App):
    def build(self):
        # Load the KV file
        Builder.load_file("ui/main_window.kv")
        main_layout = BoxLayout(orientation="vertical")

        api = TfLAPI(TFL_API_KEY)
        stop_points = api.fetch_all_stop_points()

        # Create the DropDown widget
        dropdown_widget = Dropdown()
        dropdown_options = {}

        for stop_point in stop_points.get("stopPoints", []):
            dropdown_options[stop_point.get("commonName")] = stop_point.get("id")

        dropdown_widget.dropdown_options = dropdown_options

        # Add the DropDown widget to the main layout
        main_layout.add_widget(dropdown_widget)

        return main_layout


if __name__ == "__main__":
    MainWindow().run()
