from pathlib import Path

from win32more._winrt import box_value
from win32more._winrtrt import Vector
from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Windows.Win32.System.WinRT import IInspectable
from win32more.xaml import XamlClass


class ItemsRepeaterPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
        self.ItemsRepeater1.ItemsSource = Vector[IInspectable]([box_value("item1"), box_value("item2")])
