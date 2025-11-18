from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.winui3 import XamlClass, as_runtime_class


class DropDownButtonPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def DropDownButton1_Item_Click(self, sender, args):
        sender = as_runtime_class(sender)
        text = sender.Text
        self.DropDownButton1.Content = f"DropDownButton ({text})"
