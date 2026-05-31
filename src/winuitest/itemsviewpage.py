from pathlib import Path

from win32more import List
from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.winui3 import XamlClass


class ItemsViewPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
        self.ItemsView1.ItemsSource = List(["item1", "item2"])

    def ItemsView1_SelectionChanged(self, sender, args):
        if not self.ItemsView1.SelectedItem:
            return
        self.Output.Text = "Select: " + self.ItemsView1.SelectedItem.as_(str)
