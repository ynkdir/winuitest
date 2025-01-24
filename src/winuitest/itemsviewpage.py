from pathlib import Path

from win32more._winrt import box_value
from win32more._winrtrt import Vector
from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Windows.Win32.System.WinRT import IInspectable
from win32more.xaml import XamlClass


class ItemsViewPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
        # FIXME: self.ItemsView1.ItemsSource = ["item1", "item2"]
        self.ItemsView1.ItemsSource = Vector[IInspectable]([box_value("item1"), box_value("item2")])

    def ItemsView1_SelectionChanged(self, sender, args):
        if not self.ItemsView1.SelectedItem:
            return
        self.Output.Text = "Select: " + self.ItemsView1.SelectedItem.as_(str)
