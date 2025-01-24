from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.xaml import XamlClass, as_runtime_class


class ToggleSplitButtonPage(XamlClass, Page):
    def __init__(self):
        self._toggle_split_button_selected = ""

        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    def ToggleSplitButton1_Click(self, sender, args):
        self._update()

    def ToggleSplitButton1_Item_Click(self, sender, args):
        self._toggle_split_button_selected = as_runtime_class(sender).Tag.as_(str)
        self.ToggleSplitbutton1.IsChecked = True
        self.ToggleSplitbutton1.Flyout.Hide()
        self._update()

    def _update(self):
        if self.ToggleSplitbutton1.IsChecked:
            state = "ON"
        else:
            state = "OFF"
        if self._toggle_split_button_selected != "":
            selected = f" ({self._toggle_split_button_selected})"
        else:
            selected = ""
        self.ToggleSplitbutton1.Content = f"ToggleSplitButton ({state}){selected}"
