from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass


class CheckBoxPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def CheckBox1_Click(self, sender, args):
        if self.CheckBox1.IsChecked:
            state = "Checked"
        else:
            state = "Unchecked"
        self.CheckBox1.Content = f"CheckBox ({state})"

    def CheckBox2_Click(self, sender, args):
        if self.CheckBox2.IsChecked is None:
            state = "Indeterminate"
        elif self.CheckBox2.IsChecked:
            state = "Checked"
        else:
            state = "Unchecked"
        self.CheckBox2.Content = f"CheckBox (ThreeState) ({state})"
