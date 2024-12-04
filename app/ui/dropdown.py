from kivy.properties import DictProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Dropdown(BoxLayout):
    dropdown_options = DictProperty({})  # Store options as text-value pairs

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dropdown = DropDown()

    def on_dropdown_options(self, instance, options):
        """Repopulate the dropdown when options change."""
        self.dropdown.clear_widgets()  # Clear previous dropdown buttons
        for text, value in options.items():
            btn = Button(text=text, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn, t=text, v=value: self.select_option(t, v))
            self.dropdown.add_widget(btn)

    def open_dropdown(self):
        """Open the dropdown."""
        self.dropdown.open(self.ids.main_button)

    def select_option(self, text, value):
        """Handle dropdown selection."""
        self.ids.main_button.text = text  # Update main button text
        self.ids.selected_label.text = f"Selected: {text}"  # Update label text
        self.ids.selected_value_label.text = f"Value: {value}"  # Update value label
        self.dropdown.dismiss()  # Close dropdown
