from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass, as_runtime_class


class ListViewPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def ListView1_SelectionChanged(self, sender, args):
        self.Output.Text = as_runtime_class(self.ListView1.SelectedItem).Content.as_(str)
