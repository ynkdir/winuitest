from pathlib import Path

from win32more import List
from win32more.Microsoft.UI.Xaml.Controls import Button, Page
from win32more.winui3 import XamlClass


class ItemsRepeaterPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
        self.ItemsRepeater1.ItemsSource = List(["item1", "item2"])

    def Button_Click(self, sender, args):
        self.Output.Text = sender.as_(Button).Content.as_(str)
