from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.winui3 import XamlClass


class PopupPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def ShowPopupOffsetClicked(self, sender, args):
        if not self.StandardPopup.IsOpen:
            self.StandardPopup.IsOpen = True

    def ClosePopupClicked(self, sender, args):
        if self.StandardPopup.IsOpen:
            self.StandardPopup.IsOpen = False
