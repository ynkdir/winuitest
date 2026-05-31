from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import MenuFlyoutItem, Page
from win32more.winui3 import XamlClass


class MenuBarPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def Menu_Click(self, sender, args):
        menu_flyout_item = sender.as_(MenuFlyoutItem)
        self.Output.Text = "You clicked: " + menu_flyout_item.Text
