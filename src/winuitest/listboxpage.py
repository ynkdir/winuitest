from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Microsoft.UI.Xaml.Media import SolidColorBrush
from win32more.Windows.UI import Colors
from win32more.xaml import XamlClass


class ListBoxPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def ListBox1_SelectionChanged(self, sender, args):
        if not self.ListBox1.SelectedItem:
            return
        if self.ListBox1.SelectedItem.as_(str) == "Blue":
            color = Colors.Blue
        elif self.ListBox1.SelectedItem.as_(str) == "Green":
            color = Colors.Green
        elif self.ListBox1.SelectedItem.as_(str) == "Red":
            color = Colors.Red
        elif self.ListBox1.SelectedItem.as_(str) == "Yellow":
            color = Colors.Yellow
        else:
            raise NotImplementedError()
        self.Rectangle1.Fill = SolidColorBrush(color)
