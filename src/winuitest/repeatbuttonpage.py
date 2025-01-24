from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass


class RepeatButtonPage(XamlClass, Page):
    def __init__(self):
        self._click_count = 0

        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def RepeatButton1_Click(self, sender, args):
        self._click_count += 1
        self.RepeatButton1.Content = f"Clicked! {self._click_count}"
