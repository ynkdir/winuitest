from pathlib import Path

from win32more import List
from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.Microsoft.UI.Xaml.Input import StandardUICommand, StandardUICommandKind
from win32more.winui3 import XamlClass


class StandardUICommandPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))

        delete_command = StandardUICommand(StandardUICommandKind.Delete)
        delete_command.ExecuteRequested += self.DeleteCommand_ExecuteRequested

        self.DeleteFlyoutItem.Command = delete_command

        self._items = List()

        for i in range(15):
            self._items.append({"Text": f"List item {i}", "Command": delete_command})

        self.ListView1.ItemsSource = self._items

    def DeleteCommand_ExecuteRequested(self, sender, args):
        if args.Parameter is not None:
            # AppBarButton in ListView item selected
            for i, item in enumerate(self._items):
                if item["Text"] == args.Parameter.as_(str):
                    del self._items[i]
                    return

        # Delete menu selected
        if self.ListView1.SelectedIndex != -1:
            del self._items[self.ListView1.SelectedIndex]
