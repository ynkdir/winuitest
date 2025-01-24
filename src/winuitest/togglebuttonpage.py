from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass


class ToggleButtonPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def ToggleButton1_Click(self, sender, args):
        if self.ToggleButton1.IsChecked:
            state = "ON"
        else:
            state = "OFF"
        self.ToggleButton1.Content = f"ToggleButton ({state})"
