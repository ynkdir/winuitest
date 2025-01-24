from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass


class ButtonPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def Button1_Click(self, sender, args):
        content = self.Button1.Content.as_(str)
        self.Button1.Content = f"[{content}]"
