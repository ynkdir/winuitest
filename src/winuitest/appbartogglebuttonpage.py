from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.winui3 import XamlClass


class AppBarToggleButtonPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def AppBarButton_Click(self, sender, args):
        if self.AppBarToggleButton1.IsChecked:
            self.Output.Text = "IsChecked = True"
        else:
            self.Output.Text = "IsChecked = False"
