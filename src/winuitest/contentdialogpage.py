from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import (
    ContentDialog,
    ContentDialogResult,
    Page,
)
from win32more.xaml import XamlClass


class ContentDialogPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

    async def Button1_Click(self, sender, args):
        dialog = ContentDialog()
        dialog.XamlRoot = self.XamlRoot
        dialog.Title = "title"
        dialog.Content = "content dialog"
        dialog.PrimaryButtonText = "Ok"
        dialog.CloseButtonText = "Cancel"
        result = await dialog.ShowAsync()
        if result == ContentDialogResult.Primary:
            self.Output.Text = "Result: Ok"
        elif result == ContentDialogResult.None_:
            self.Output.Text = "Result: Cancel"
        else:
            raise NotImplementedError()
