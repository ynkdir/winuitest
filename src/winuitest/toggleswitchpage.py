from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass


class ToggleSwitchPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def ToggleSwitch1_Toggled(self, sender, args):
        if self.ToggleSwitch1.IsOn:
            self.Output.Text = self.Output.Text + " ON"
        else:
            self.Output.Text = self.Output.Text + " OFF"
