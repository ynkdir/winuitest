from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass


class XamlUICommandPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def CustomXamlUICommand_ExecuteRequested(self, sender, args):
        self.XamlUICommandOutput.Text = "You fired the custom command"
