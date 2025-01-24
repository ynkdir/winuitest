from tempfile import NamedTemporaryFile

from win32more.Microsoft.UI.Xaml import Application
from win32more.Windows.Foundation import Uri


def LoadComponentFromString(obj, xaml: str) -> None:
    with NamedTemporaryFile(delete_on_close=False) as f:
        f.write(xaml.encode("utf-8"))
        f.close()
        xaml_path = f.name.replace("\\", "/")
        resource_locator = Uri(f"ms-appx:///{xaml_path}")
        Application.LoadComponent(obj, resource_locator)
