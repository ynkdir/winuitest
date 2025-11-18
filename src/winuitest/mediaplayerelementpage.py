from pathlib import Path

from win32more.Microsoft.UI.Xaml.Controls import Page
from win32more.winui3 import XamlClass


class MediaPlayerElementPage(XamlClass, Page):
    def __init__(self):
        super().__init__()
        # TODO: ResourceNotFound event is not triggered for MediaPlayerElement.Source
        # self.LoadComponentFromFile(Path(__file__).with_suffix(".xaml"))
        xaml_path = Path(__file__).with_suffix(".xaml")
        mp4_path = xaml_path.with_name("movie1.mp4").as_posix()
        xaml = xaml_path.read_text().replace("movie1.mp4", f"ms-appx:///{mp4_path}")
        self.LoadComponentFromString(xaml, xaml_path)
