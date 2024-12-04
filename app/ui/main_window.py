from kivy.app import App
from kivy.lang import Builder
from ui.dropdown import Dropdown


class MainWindow(App):
    def build(self):
        # Load the KV file
        Builder.load_file("ui/main_window.kv")

        # Create the DropDown widget
        dropdown_widget = Dropdown()

        # Define options as text-value pairs
        dropdown_options = {
            "Oxford": "1",
            "Cambridge": "2",
            "London": "3",
            "Manchester": "4",
        }

        # Set the dropdown options dynamically
        dropdown_widget.dropdown_options = dropdown_options

        return dropdown_widget


if __name__ == "__main__":
    MainWindow().run()
