from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import AppBarButton, Page
from win32more.winui3 import XamlClass


class CommandBarPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def OnElementClicked(self, sender, args):
        app_bar_button = sender.as_(AppBarButton)
        self.Output.Text = "You clicked: " + app_bar_button.Label
