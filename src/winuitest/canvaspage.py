from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.winui3 import XamlClass


class CanvasPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
