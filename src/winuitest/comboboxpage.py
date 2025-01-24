from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Microsoft.UI.Xaml.Media import SolidColorBrush
from win32more.Windows.UI import Colors
from win32more.xaml import XamlClass


class ComboBoxPage(XamlClass, Page):
    def __init__(self):
        self._initializing = True

        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

        self._initializing = False

    def ComboBox1_SelectionChanged(self, sender, args):
        if self._initializing:
            return

        color_name = args.AddedItems[0].as_(str)
        if color_name == "Blue":
            color = Colors.Blue
        elif color_name == "Green":
            color = Colors.Green
        elif color_name == "Red":
            color = Colors.Red
        elif color_name == "Yellow":
            color = Colors.Yellow
        else:
            raise NotImplementedError()
        self.Rectangle1.Fill = SolidColorBrush(color)
