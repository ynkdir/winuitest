from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass, as_runtime_class


class TreeViewPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def TreeView1_SelectionChanged(self, sender, args):
        # self.TreeView1.SelectedItem seems to refer previous item
        self.Output.Text = as_runtime_class(args.AddedItems[0]).Content.as_(str)
