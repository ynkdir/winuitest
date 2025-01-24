from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Microsoft.UI.Xaml.Media import SolidColorBrush
from win32more.xaml import XamlClass


class ColorPickerPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def ColorPicker1_ColorChanged(self, sender, args):
        self.Background = SolidColorBrush(args.NewColor)
