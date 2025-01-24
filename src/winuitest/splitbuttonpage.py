from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass, as_runtime_class


class SplitButtonPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def SplitButton1_Click(self, sender, args):
        self.SplitButton1.Content = self.SplitButton1.Content.as_(str) + "!"

    def SplitButton1_Item_Click(self, sender, args):
        sender = as_runtime_class(sender)
        tag = sender.Tag.as_(str)
        self.SplitButton1.Content = f"SplitButton ({tag})"
        self.SplitButton1.Flyout.Hide()
