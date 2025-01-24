import importlib

from win32more.Windows.UI.Xaml.Interop import TypeKind
from win32more.xaml import XamlApplication, XamlType

from .mainwindow import MainWindow


class App(XamlApplication):
    def OnLaunched(self, args):
        self._window = MainWindow()
        self._window.Activate()

    def GetXamlTypeByFullName(self, typename):
        if typename.startswith("winuitest."):
            namespace, name = typename.rsplit(".", 1)
            module = importlib.import_module(namespace)
            activator = getattr(module, name)
            return XamlType(typename, TypeKind.Custom, activate_instance=activator)
        return super().GetXamlTypeByFullName(typename)


def start():
    XamlApplication.Start(App)
