from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Microsoft.UI.Xaml.Media import SolidColorBrush
from win32more.Windows.UI import Colors
from win32more.winui3 import XamlClass, as_runtime_class


class RadioButtonPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def RadioButton_Checked(self, sender, args):
        self.Result.Text = as_runtime_class(sender).Content.as_(str) + " selected"

    def BackgroundColor_SelectionChanged(self, sender, args):
        if not self.BackgroundRadioButtons.SelectedItem:
            # When radiobutton selected, None is selected before new one.
            return
        name = self.BackgroundRadioButtons.SelectedItem.as_(str)
        if name == "Green":
            color = Colors.Green
        elif name == "Yellow":
            color = Colors.Yellow
        elif name == "White":
            color = Colors.White
        self.ControlOutput.Background = SolidColorBrush(color)

    def BorderBrush_SelectionChanged(self, sender, args):
        if not self.BorderRadioButtons.SelectedItem:
            return
        name = self.BorderRadioButtons.SelectedItem.as_(str)
        if name == "Green":
            color = Colors.Green
        elif name == "Yellow":
            color = Colors.Yellow
        elif name == "White":
            color = Colors.White
        self.ControlOutput.BorderBrush = SolidColorBrush(color)
