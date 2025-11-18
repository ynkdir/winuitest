from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.winui3 import XamlClass


class FlyoutPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def DeleteConfirmation_Click(self, sender, args):
        self.Flyout1.Hide()
