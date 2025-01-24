from pathlib import Path

from win32more.Microsoft.UI.Xaml import Window
from win32more.Microsoft.UI.Xaml.Controls import NavigationViewItem
from win32more.Windows.UI.Xaml.Interop import TypeKind
from win32more.xaml import XamlClass, xaml_typename


class MainWindow(XamlClass, Window):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
        self.Title = "WinUI Demo"
        self.NavigationView1.SelectedItem = self.NavigationView1.MenuItems[0]

    def NavigationView1_SelectionChanged(self, navigation_view, args):
        item = args.SelectedItem.as_(NavigationViewItem)
        typename = item.Tag.as_(str)
        self.Frame1.Navigate(xaml_typename(typename, TypeKind.Custom))
