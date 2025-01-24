from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Microsoft.UI.Xaml.Shapes import Rectangle
from win32more.xaml import XamlClass


class FlipViewPage(XamlClass, Page):
    def __init__(self):
        self._initializing = True

        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

        self._initializing = False

    def FlipView1_SelectionChanged(self, sender, args):
        if self._initializing:
            return

        self.Output.Text = self.FlipView1.SelectedItem.as_(Rectangle).Tag.as_(str)
