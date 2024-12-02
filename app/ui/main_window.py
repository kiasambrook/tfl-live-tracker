import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the subfolder containing the .kv files
kv_folder = os.path.join(current_dir, 'widgets')

# Load all .kv files in the subfolder
for file_name in os.listdir(kv_folder):
    if file_name.endswith(".kv"):
        kv_file = os.path.join(kv_folder, file_name)
        Builder.load_file(kv_file)


class TitleLabel(Label):
    pass


class MainWindow(App):
    def build(self):
        root = BoxLayout(orientation="vertical")
        root = TitleLabel()
        return root
