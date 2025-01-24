from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass, as_runtime_class


class RadioButtonPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def RadioButton_Checked(self, sender, args):
        self.Result.Text = as_runtime_class(sender).Content.as_(str) + " selected"
